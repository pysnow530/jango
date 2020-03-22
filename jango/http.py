from urllib.parse import parse_qs

from jango.utils.cookie import parse_cookie
from jango.utils.datastructure import MultiValueDict


class HttpRequest:

    def __init__(self, environ):
        self.method = environ['REQUEST_METHOD']
        self.path_info = environ['PATH_INFO']
        self.environ = environ

    @property
    def GET(self):
        dct = parse_qs(self.environ.get('QUERY_STRING', ''))
        return MultiValueDict(dct)

    @property
    def COOKIE(self):
        cookie = self.environ.get('HTTP_COOKIE', '')
        return parse_cookie(cookie)


class HttpResponse:

    def __init__(self, content, content_type='plain/text', status_code=200):
        self.content = content
        self.content_type = content_type
        self.status_code = status_code
