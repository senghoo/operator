import tornado.web

from utils import T

routes = []


class R:
    def __init__(self, route):
        self.route = route

    def __call__(self, cls):
        routes.append((self.route, cls))
        return cls


class BaseHandler(tornado.web.RequestHandler):
    @property
    def db(self):
        return self.application.db


@R("/")
class MainHandler(BaseHandler):
    @T("index.html")
    def get(self):
        return{
            'name': 'world!!'
        }

@R("/sms")
class SmsHandler(BaseHandler):
    @T("sms.html")
    def get(self):
        return {}
