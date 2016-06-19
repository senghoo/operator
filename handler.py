import json
import logging
import requests

from tornado.options import options


from model import TextMessage


class IFTTT(object):
    def __init__(self, key):
        self.key = key
        self.logger = logging.getLogger("ifttt")

    def url(self, event):
        return 'https://maker.ifttt.com/trigger/{0}/with/key/{1}'.format(event, self.key)

    def event(self, event, value1="", value2="", value3=""):
        try:
            requests.post(url=self.url(event),
                          headers={"Content-Type": "application/json; charset=utf-8"},
                          data=json.dumps({
                              "value3": value3,
                              "value2": value2,
                              "value1": value1
                          })
            )
        except requests.exceptions.RequestException:
            self.logger.error("HTTP Request failed")

    def sms_callback(self, sms):
        self.event("sms_received", sms.number, sms.text, sms.time.strftime("%Y-%m-%d %H:%M:%S"))


def init_handles(gsm):
    gsm.add_sms_callback(TextMessage.save_sms)

    # ifttt
    if options.ifttt_key:
        ifttt = IFTTT(options.ifttt_key)
        gsm.add_sms_callback(ifttt.sms_callback)
