FROM python:3.7-alpine

WORKDIR /server

COPY ./Backend/server .


RUN pip3 install -r requirements.txt

RUN pip3 install grpcio-tools


CMD ["python3", "server.py"]