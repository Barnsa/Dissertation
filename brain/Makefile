SHELL=/bin/bash
NAME=brain
LOC=$(shell pwd)

ALL: Dockerfile
	docker build  -t barnsa/$(NAME) .	


run:
	docker run -h $(NAME):latest --net dummy_net -v $(LOC)/mount:/root/mount  -it --privileged=true --name $(NAME) --ip 175.20.0.200 barnsa/$(NAME)  
#Brain is always on *.*.*.200, so it can scan from .2 to .199 for targets

clean:
#	docker kill $(NAME)
	docker rm $(NAME)

restart:
#	docker kill $(NAME)
	docker rm $(NAME)
	docker build  -t barnsa/$(NAME) .
	docker run -h $(NAME):latest --net dummy_net -v $(LOC)/mount:/root/mount  -it --privileged=true --name $(NAME) barnsa/$(NAME)
