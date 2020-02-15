FROM ubuntu:18.04

RUN apt update 
RUN apt install -y apt-utils xinetd build-essential gcc-multilib
RUN apt upgrade -y

RUN useradd -m ctf
WORKDIR /home/ctf
RUN cp -R /lib* /home/ctf && \
    cp -R /usr/lib* /home/ctf
RUN mkdir /home/ctf/dev && \
    mknod /home/ctf/dev/null c 1 3 && \
    mknod /home/ctf/dev/zero c 1 5 && \
    mknod /home/ctf/dev/random c 1 8 && \
    mknod /home/ctf/dev/urandom c 1 9 && \
    chmod 666 /home/ctf/dev/*
RUN mkdir /home/ctf/bin && \
    cp /bin/sh /home/ctf/bin && \
    cp /bin/ls /home/ctf/bin && \
    cp /bin/cat /home/ctf/bin 


COPY ./ctf.xinetd /etc/xinetd.d/ctf
COPY ./start.sh /start.sh
RUN echo "Blocked by ctf_xinetd" > /etc/banner_fail

RUN chmod +x /start.sh

COPY ./chall.c /home/ctf
COPY ./flag.txt /home/ctf
COPY ./Makefile /home/ctf
RUN chown -R root:ctf /home/ctf && \
    # chmod 777 /home/ctf/chall && \
    chmod -R 750 /home/ctf && \
    chmod 740 /home/ctf/flag.txt
RUN make all

CMD ["/start.sh"]
EXPOSE 2000
