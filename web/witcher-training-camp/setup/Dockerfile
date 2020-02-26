FROM tiangolo/uwsgi-nginx-flask:python3.7

COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN dpkg -i google-chrome-stable_current_amd64.deb; apt-get update && apt install -fy

ENV LISTEN_PORT 8002

EXPOSE 8002

COPY ./flag.txt /home/flag.txt