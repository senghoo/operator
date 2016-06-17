import logging
import tornado.ioloop
from gsmmodem.modem import GsmModem

logger = logging.getLogger("GSM")
sms_receive_log_template = u'== SMS message received ==\nFrom: {0}\nTime: {1}\nMessage:\n{2}\n'

class GSM(object):
    def __init__(self, port, baudrate, pin=None):
        self.sms_callbacks = []
        self.port = port
        self.baudrate = baudrate
        self.pin = pin

    def run(self):
        self.modem = GsmModem(self.port, self.baudrate,
                              smsReceivedCallbackFunc=self.sms_callback)
        self.modem.smsTextMode = False
        self.modem.connect(self.pin)

    def sms_callback(self, sms):
        logger.info(sms_receive_log_template.format(sms.number,
                                                    sms.time, sms.text))
        for callback in self.sms_callbacks:
            tornado.ioloop.IOLoop.instance().add_callback(callback, sms)

    def add_sms_callback(self, callback):
        self.sms_callbacks.append(callback)
