from handlers.base_handler import BaseHandle


class HelloWorldHandler(BaseHandle):
    async def get(self):
        self.write("Hello, world")
