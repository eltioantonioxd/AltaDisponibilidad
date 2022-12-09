FROM python:3.7-alpine

WORKDIR /app

COPY . .


RUN pip3 install -r requirements.txt

RUN pip3 install grpcio-tools

RUN python3 -m grpc_tools.protoc -I. --python_out=./protos --grpc_python_out=./protos ./protos/myproto.proto

CMD ["python3", "app.py"]