import os
import functools
from tornado import template

ROOT_PATH = os.path.dirname(os.path.realpath(__file__))
make_path = functools.partial(os.path.join, ROOT_PATH)


loader = template.Loader(make_path("template"))


class T:
    def __init__(self, tmp):
        self.template = loader.load(tmp)

    def __call__(self, func):
        thiz = self

        def __wrap__(self, *args, **kwargs):
            ret = func(self, *args, **kwargs)
            self.write(thiz.template.generate(**ret or {}))
        return __wrap__
