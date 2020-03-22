"""
该文件对外暴露一个标准wsgi接口，可以提供wsgi服务器使用。

下面是使用gunicorn启动该服务器的例子：
$ gunicorn demo.wsgi:wsgi_application
"""
import importlib

from jango.wsgi import get_wsgi_application

settings = importlib.import_module('demo.settings')
application = get_wsgi_application(settings.ROOT_URLCONF)
