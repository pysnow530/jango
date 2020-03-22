import sys
import importlib
from wsgiref.simple_server import make_server

from jango.wsgi import get_wsgi_application

host = sys.argv[1]
port = int(sys.argv[2])
settings = importlib.import_module(sys.argv[3])

wsgi_application = get_wsgi_application(settings.ROOT_URLCONF)

with make_server(host, port, wsgi_application) as httpd:
    print(f"Serving on port http://{host}:{port}...")
    httpd.serve_forever()
