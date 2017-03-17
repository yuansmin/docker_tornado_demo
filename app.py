import tornado.web
import tornado.ioloop

class Main(tornado.web.RequestHandler):

    def get(self):
        self.write("hello world\n")


if __name__ == '__main__':
    app = tornado.web.Application([(r'/', Main),] )
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()

