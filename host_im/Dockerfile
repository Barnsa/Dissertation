FROM ubuntu:bionic
# set the scene and make sure we have 
# tools to 

RUN apt-get update
RUN apt-get -y install netcat
RUN apt-get -y install e3
RUN apt-get -y install net-tools
RUN apt-get -y install openssh-server sudo
RUN apt-get -y install man
RUN apt-get -y install iputils-ping 

# important for some debugging of virus later
RUN apt-get -y install nmap python3-pip
RUN apt-get -y install curl 

# Set up a user
RUN useradd -ms /bin/bash user
RUN echo user:resu|chpasswd

# requirements for FTP server code
RUN pip3 install pyftpdlib

# requirements for AV code
RUN pip3 install pandas sklearn pefile
RUN pip3 install joblib
#RUN apt-get -y install wine-stable
#RUN sudo dpkg --add-architecture i386 && sudo apt-get -y update && sudo apt-get -y install wine32
# RUN wget https://www.python.org/ftp/python/2.7.9/python-2.7.9.amd64.msi

# # adding and running server code
# ADD /mount/AV.py /
# R UN python3 ai_server_code.py &
#JS: I moved this into the "mount" folder, so you can edit while the devices are running
# and I also moved the startup into the starter.sh script

# adding and running starter script for some 
# easy running and debugging
# RUN chmod u+x /root/mount/starter.sh

CMD ["/root/mount/starter.sh"]
