FROM python:3.8.5-alpine

COPY . /cronjob
WORKDIR /cronjob

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

RUN crontab mycron

CMD crond && tail -f /cronjob/out.log 