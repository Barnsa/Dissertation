import logging 
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import os, sys

# Prototyping a subclass to handle anti-virus shenanigans.
# please don't trim unless absolutely necessary!!
class MyHandler(FTPHandler):
    """This is a subclass extension of the handler to add the 
    necessary custom anti virus functionality. Controls output
    on the commandline when it recieves a file.
    """
    def on_connect(self):
        # do somthing when a client connects
        print ("%s:%s connected" % (self.remote_ip, self.remote_port))
        #pass

    def on_disconnect(self):
        # do something when client disconnects
        print ("%s:%s disconnected" % (self.remote_ip, self.remote_port))
        #pass

    def on_login(self, username):
        # do something when user login
        pass

    def on_logout(self, username):
        # do something when user logs out
        pass

    def on_file_sent(self, file):
        # do something when a file has been sent
        pass

    def on_file_received(self, file):
        # do something when a file has been received
        # x = input("enter stuff dood!! ")
        print("Running virus-not-virus!")
        # Move this out to a separate script and call it in a sepaate process
        #exec(open(file).read())
        pid=os.fork()
        if pid!=0:
            os.system("/root/mount/executor.py " + file)
            os._exit(0)
        
    def on_incomplete_file_sent(self, file):
        # do something when a file is partially sent
        pass

    def on_incomplete_file_received(self, file):
        # remove partially uploaded files
        import os
        os.remove(file)


authorizer = DummyAuthorizer()
authorizer.add_user('user', '12345', '/tmp/stash', perm='elradfmwMT')
authorizer.add_anonymous('/tmp/stash', perm='elradfmwMT')

handler = MyHandler #FTPHandler
handler.authorizer = authorizer

# If run as main program
if __name__ == '__main__':
    # logging.basicConfig(filename='/tmp/stash/pyftpd.log', level=logging.INFO)
    logging.basicConfig(filename='/tmp/stash/pyftpd.log', level=logging.DEBUG)
    server = FTPServer(('', 21), handler)
    server.serve_forever()
