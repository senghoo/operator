import os
from tornado import template

ROOT_DIR = os.path.dirname(os.path.realpath(__file__))

loader = template.Loader(os.path.join(ROOT_DIR, "template"))


class T:
    def __init__(self, tmp):
        self.template = loader.load(tmp)

    def __call__(self, func):
        thiz = self

        def __wrap__(self, *args, **kwargs):
            ret = func(self, *args, **kwargs)
            self.write(thiz.template.generate(**ret or {}))
        return __wrap__
