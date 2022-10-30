FROM python:3.11-slim-buster

WORKDIR /python-docker

ENV SERVER_ADDRESS 10.0.211.73
ENV FTP_USER test
ENV FTP_PASS test
COPY requirements.txt requirements.txt
RUN apt update -y && apt upgrade -y
RUN apt install -y curlftpfs
RUN pip3 install -r requirements.txt
COPY . .
RUN chmod +x ./start.sh
EXPOSE 5000/tcp
CMD ["sh","./start.sh"]

