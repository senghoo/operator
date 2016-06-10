import tornado.ioloop
import tornado.web
from tornado.options import define, options

import controllers

define("host", default=8888, type=int)


def make_app():
    return tornado.web.Application(controllers.routes, debug=True)

if __name__ == "__main__":
    options.parse_command_line()
    app = make_app()
    app.listen(options.host)
    tornado.ioloop.IOLoop.current().start()
