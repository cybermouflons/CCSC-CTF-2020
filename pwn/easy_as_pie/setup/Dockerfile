
FROM ubuntu:16.04

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y socat gcc-multilib

# set workdir and transfer binary
WORKDIR /root
COPY pie .
COPY flag.txt .

EXPOSE 61337
CMD ["socat", "-vv","TCP-LISTEN:61337,reuseaddr,fork,su=root", "EXEC:'/root/pie'"]
