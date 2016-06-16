import tornado.ioloop
from gsmmodem.modem import GsmModem


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
        for callback in self.sms_callbacks:
            tornado.ioloop.IOLoop.add_callback(callback, sms)

    def add_sms_callback(self, callback):
        self.sms_callbacks.append(callback)
