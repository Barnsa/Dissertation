from ftplib import FTP

ftp = FTP('')
ftp.connect('localhost', 1337)
ftp.login('user', '12345')
ftp.cwd('/home/username')  # directory for shenanigans
ftp.retrlines('LIST')


def uploadFile():
    filename: str = 'testfile.txt'   # replace with a created virus file
    ftp.storbinary('STOR ' + filename, open(filename, 'rb'))
    ftp.quit()


def downloadFile():
    filename: str = 'testfile.txt'  # replace with download file
    localFile = open(filename, 'wb')
    ftp.retrbinary('RETR ' + filename, localFile.write, 1024)
    ftp.quit()
    localFile.close()


if __name__ == '__main__':
    uploadFile()
    # downloadFile()
