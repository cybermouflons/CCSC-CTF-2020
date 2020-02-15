FROM tiangolo/uwsgi-nginx-flask:python3.7

COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN dpkg -i google-chrome-stable_current_amd64.deb; apt-get update && apt install -fy

COPY ./flag.txt /home/flag.txt