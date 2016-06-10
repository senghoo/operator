import tornado.web

from utils import T, make_path

routes = [
    (r"/static/(.*)", tornado.web.StaticFileHandler, {"path": make_path("static")}),
]


class R:
    def __init__(self, route):
        self.route = route

    def __call__(self, cls):
        routes.append((self.route, cls))
        return cls


@R("/")
class MainHandler(tornado.web.RequestHandler):
    @T("index.html")
    def get(self):
        return
