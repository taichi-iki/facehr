# coding: utf-8

# simple http server
# ローカルディレクトリのpublicディレクトリ内のファイルにアクセス

import tornado.ioloop, tornado.web, tornado.template

listen_port = 9095

if __name__ == "__main__":
    application = tornado.web.Application([
        (r"/(.*)", tornado.web.StaticFileHandler, {"path": "./public"}),
    ])
    application.listen(listen_port)
    tornado.ioloop.IOLoop.instance().start()
