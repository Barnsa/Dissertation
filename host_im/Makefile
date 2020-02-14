#TODO: remove debug flag
NAME=dumbclient
LOC=$(shell pwd)

ALL: Dockerfile
	docker build  -t barnsa/$(NAME) .

run:
ifndef ID
	@echo
	@echo "You must set an ID. Try 'make run ID=1' for example."
	@echo
else
	docker run -h $(NAME)_$(ID) --net dummy_net -v $(LOC)/mount:/root/mount  -it --privileged=true --name $(NAME)_$(ID) barnsa/$(NAME)  /bin/bash

endif

clean:
ifndef ID
	@echo
	@echo "You must set an ID. Try 'make clean ID=1' for example."
	@echo
else
	docker kill $(NAME)_$(ID)
	docker rm $(NAME)_$(ID)
endif



net:

	docker network create --subnet=175.20.0.0/24 dummy_net
