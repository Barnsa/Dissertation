#!/bin/bash
# This script is for setting up the Ubuntu VM with Docker and other environment modifications.
# I'll add oher stuff for setting up the rest of my environment too in future iterations.
# source: https://docs.docker.com/v17.09/engine/installation/linux/docker-ce/ubuntu/#set-up-the-repository
sudo apt-get -y install \
    apt-transport-https \
    ca-certificates \
    curl \
    software-properties-common

    
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo apt-key fingerprint 0EBFCD88

sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"

sudo apt-get -y update
sudo apt-get -y install docker-ce


# create a docker group and sudo the docker shenanigans
# source: https://docs.docker.com/install/linux/linux-postinstall/
# this is needed for make files
sudo groupadd docker
sudo usermod -aG docker $USER
newgrp docker

# additional packages used in static analysis of C programs
# added here for 324COM secure programming
sudo apt install llvm-9
sudo apt install clang
sudo apt install clang-tools
sudo apt install clang-9
sudo apt install clang-tools-9

# get all of the python packages we need
pip3 install torch torchvision
pip3 install matplotlib

# test everything is working well
docker run hello-world