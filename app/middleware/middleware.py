from werkzeug.wrappers import Request


# for Authenication to get the Request und send the Response 
class Middleware:

    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        request = Request(environ)
        print('Hallo' , request)
        return self.app(environ, start_response)
