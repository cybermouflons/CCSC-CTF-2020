FROM debian:stable-slim
RUN apt-get update
RUN apt-get install nano apt-utils -y
RUN apt-get upgrade -y
RUN apt-get install socat -y
RUN apt-get install python3 python3-pip -y
RUN useradd ctf

COPY ./ /chall
RUN chmod +x /chall/server.py

USER ctf

CMD python3 /chall/server.py