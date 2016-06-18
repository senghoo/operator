import logging
import tornado.ioloop
import tornado.web
from tornado.options import define, options

import controllers
from utils import make_path
from model import engine, Session, TextMessage
from gsm import GSM

define("port", default=8888, type=int)
define("host", default="0.0.0.0")
define("gsm_port", default="/dev/ttyAMA0")
define("gsm_baudrate", default=115200, type=int)
define("gsm_pin", default=None)


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
        self.gsm = GSM(options.gsm_port, options.gsm_baudrate, options.gsm_pin)
        self.gsm.add_sms_callback(TextMessage.save_sms)
        self.gsm.process_stored_sms()
        self.gsm.run()

if __name__ == "__main__":
    options.parse_command_line()
    logger = logging.getLogger('main')
    app = Application()
    logger.info("listen on {0}:{1}".format(options.host, options.port))
    app.listen(options.port, address=options.host)
    tornado.ioloop.IOLoop.current().start()
