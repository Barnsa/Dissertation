FROM python:3
ADD ai_server_code.py /
RUN pip3 install pyftpdlib
CMD [ "python3", "./ai_server_code.py"]