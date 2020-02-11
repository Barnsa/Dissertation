FROM ubuntu:bionic
RUN apt-get update
RUN apt-get -y install netcat
RUN apt-get -y install e3
RUN apt-get -y install net-tools
RUN apt-get -y install openssh-server sudo
RUN apt-get -y install man
RUN apt-get -y install iputils-ping

RUN apt-get -y install nmap python3-pip

RUN useradd -ms /bin/bash user
RUN echo user:resu|chpasswd



COPY starter.sh /root/

RUN chmod u+x /root/starter.sh

CMD ["/root/starter.sh"]
