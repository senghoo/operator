import os
from tornado import template

ROOT_DIR = os.path.dirname(os.path.realpath(__file__))

loader = template.Loader(os.path.join(ROOT_DIR, "template"))


class T:
    def __init__(self, tmp):
        self.template = loader.load(tmp)

    def __call__(self, func):
        def __wrap__(*args, **kwargs):
            ret = func(*args, **kwargs)
            return self.template.generate(**ret)
        return __wrap__
