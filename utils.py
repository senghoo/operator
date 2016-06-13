import os
import functools

ROOT_PATH = os.path.dirname(os.path.realpath(__file__))
make_path = functools.partial(os.path.join, ROOT_PATH)


class T:
    def __init__(self, tmp):
        self.template_name = tmp

    def __call__(self, func):
        thiz = self

        def __wrap__(self, *args, **kwargs):
            ret = func(self, *args, **kwargs)
            self.render(thiz.template_name, **ret or {})
        return __wrap__
