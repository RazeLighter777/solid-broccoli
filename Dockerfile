FROM python:3.11-slim-buster

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN apt update -y && apt upgrade -y
RUN apt install -y curlftpfs
RUN pip3 install -r requirements.txt
COPY . .
RUN source .env
RUN chmod +x ./start.sh
EXPOSE 5000/tcp
CMD ["sh","./start.sh"]

