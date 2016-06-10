import tornado.web

from utils import T


class MainHandler(tornado.web.RequestHandler):
    @T("index.html")
    def get(self):
        return
