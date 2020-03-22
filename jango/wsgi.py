from jango.http import HttpRequest, HttpResponse
from jango.url import resolve

STATUS_TO_DISPLAY = {
    200: '200 OK',
    400: '400 Bad Request',
    404: '404 Not Found',
}


def handle_view(request, urlconf):
    """解析执行的request，调用并返回处理结果"""
    # TODO: 请求前中间件
    resolve_match = resolve(request.path_info, urlconf)
    if not resolve_match:
        return HttpResponse(content='404 Not Found', status_code=404)

    callback, callback_args, callback_kwargs = resolve_match
    try:
        resp = callback(request, *callback_args, **callback_kwargs)
    except Exception as e:
        # TODO: 异常处理中间件
        pass

    # TODO: 请求后中间件

    return resp


def get_wsgi_application(root_urlconf):
    """
    将ROOT_URLCONF中配置的路由，包装为一个wsgi应用
    :param root_urlconf: 字符串，根url模块位置
    :return:
    """
    def wsgi_application(environ, start_response):
        """标准wsgi程序"""
        request = HttpRequest(environ)
        response = handle_view(request, root_urlconf)

        status = STATUS_TO_DISPLAY[response.status_code]
        headers = []
        start_response(status, headers)

        ret = [response.content.encode('utf-8')]
        return ret

    return wsgi_application
