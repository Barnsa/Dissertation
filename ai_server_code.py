from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

authorizer = DummyAuthorizer()
authorizer.add_user('user', '12345', '/home', perm='elradfmwMT')
authorizer.add_anonymous('/home', perm='elradfmwMT')

handler = FTPHandler
handler.authorizer = authorizer

# If run as main program
if __name__ == '__main__':
    server = FTPServer(("127.0.0.1", 1337), handler)
    server.serve_forever()