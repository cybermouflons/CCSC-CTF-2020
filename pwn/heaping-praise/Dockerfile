FROM ubuntu:16.10
MAINTAINER Stelios Joannou
LABEL Description="Pentest Cyprus 0x3 - Heap Use-After-Free" VERSION=1.0

RUN apt-get update && apt-get upgrade -y
# Add additional dependencies here
RUN apt-get install -y socat

# In case a separate user is required
RUN adduser --disabled-password --gecos '' user
RUN chown -R root:user /home/user/
RUN chmod 750 /home/user

# In case the flag is online
RUN touch /home/user/flag.txt
RUN chown root:user /home/user/flag.txt
RUN chmod 440 /home/user/flag.txt
WORKDIR /home/user/

# Copy files required
COPY ./flag.txt /home/user
COPY ./heap_trouble /home/user

EXPOSE 8000
CMD socat -T10 TCP-LISTEN:31337,reuseaddr,fork EXEC:"/home/user/heap_trouble"