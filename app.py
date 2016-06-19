import os
import logging
import tornado.ioloop
import tornado.web
from tornado.options import define, options

import controllers
from utils import make_path
from model import engine, Session
from gsm import GSM
from handler import init_handles

define("port", default=8888, type=int)
define("host", default="0.0.0.0")
define("gsm_port", default="/dev/ttyAMA0")
define("gsm_baudrate", default=115200, type=int)
define("gsm_pin", default=None)
define("ifttt_key", default=None)


class Application(tornado.web.Application):
    def __init__(self):
        settings = dict(
            debug=True,
            static_path=make_path("static"),
            template_path=make_path("template")
        )
        tornado.web.Application.__init__(self, controllers.routes, **settings)
        self.db = Session
        self.init_gsm()

    def init_gsm(self):
        if not os.path.exists(options.gsm_port):
            return
        self.gsm = GSM(options.gsm_port, options.gsm_baudrate, options.gsm_pin)
        init_handles(self.gsm)
        self.gsm.run()
        self.gsm.process_stored_sms()

if __name__ == "__main__":
    options.parse_command_line()
    logger = logging.getLogger('main')
    app = Application()
    logger.info("listen on {0}:{1}".format(options.host, options.port))
    app.listen(options.port, address=options.host)
    tornado.ioloop.IOLoop.current().start()
