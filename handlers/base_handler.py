import tornado.web



class BaseHandle(tornado.web.RequestHandler):
    async def get(self):
        self.write("weclome to my world")