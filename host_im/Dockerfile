# set the scene and make sure we have 
# tools to 
FROM ubuntu:bionic
RUN apt-get update
RUN apt-get -y install netcat
RUN apt-get -y install e3
RUN apt-get -y install net-tools
RUN apt-get -y install openssh-server sudo
RUN apt-get -y install man
RUN apt-get -y install iputils-ping 

# important for some debugging of virus later
RUN apt-get -y install nmap python3-pip

# Set up a user
RUN useradd -ms /bin/bash user
RUN echo user:resu|chpasswd

# requirements for AI server code
RUN pip3 install pyftpdlib

# adding and running server code
ADD /ai_server_code.py /
RUN python3 ai_server_code.py &

# adding and running starter script for some 
# easy running and debugging
COPY starter.sh /root/
RUN chmod u+x /root/starter.sh

CMD ["/root/starter.sh"]