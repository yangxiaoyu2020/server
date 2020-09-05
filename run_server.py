"""
Owner: yangxiaoyu
a hello world program
use the tornado web
"""

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from handlers.hello_world_handler import HelloWorldHandler
from tornado.options import define, options


options.define("port", default=8002, help="run on the given port", type=int)


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", HelloWorldHandler),
        ]
        tornado.web.Application.__init__(self, handlers)





def main():
    tornado.options.parse_command_line()
    application = Application()
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
