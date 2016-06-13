import logging
import tornado.ioloop
import tornado.web
from tornado.options import define, options

import controllers
from utils import make_path
from model import engine, Session

define("port", default=8888, type=int)
define("host", default="0.0.0.0" )


class Application(tornado.web.Application):
    def __init__(self):
        settings = dict(
            debug=True,
            static_path=make_path("static"),
            template_path=make_path("template")
        )
        tornado.web.Application.__init__(self, controllers.routes, **settings)
        self.db = Session

if __name__ == "__main__":
    options.parse_command_line()
    logger = logging.getLogger('main')
    app = Application()
    logger.info("listen on {0}:{1}".format(options.host, options.port))
    app.listen(options.port, address=options.host)
    tornado.ioloop.IOLoop.current().start()
