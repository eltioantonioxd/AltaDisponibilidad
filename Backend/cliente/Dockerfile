FROM python:3.7-alpine

WORKDIR /cliente

COPY ./Backend/cliente .


RUN pip3 install -r requirements.txt

RUN pip3 install grpcio-tools


CMD ["python3", "cliente.py"]