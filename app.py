import tornado.ioloop
import tornado.web

import controllers


def make_app():
    return tornado.web.Application([
        (r"/", controllers.MainHandler),
    ], debug=True)

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
