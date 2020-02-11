#!/bin/bash
# This script is for setting up the Docker environment
# I'll add oher stuff for setting up the rest of my environment too in future iterations.
# source: https://docs.docker.com/v17.09/engine/installation/linux/docker-ce/ubuntu/#set-up-the-repository


sudo apt-get install \
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

sudo apt-get update
sudo apt-get install docker-ce
sudo docker run hello-world