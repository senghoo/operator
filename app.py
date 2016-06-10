import logging
import tornado.ioloop
import tornado.web
from tornado.options import define, options

import controllers

define("port", default=8888, type=int)
define("host", default="0.0.0.0" )


def make_app():
    return tornado.web.Application(controllers.routes, debug=True)

if __name__ == "__main__":
    options.parse_command_line()
    logger = logging.getLogger('main')
    app = make_app()
    logger.info("listen on {0}:{1}".format(options.host, options.port))
    app.listen(options.port, address=options.host)
    tornado.ioloop.IOLoop.current().start()
