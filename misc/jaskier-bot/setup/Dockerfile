FROM python:3.7

COPY requirements.txt /code/requirements.txt
COPY bot.py /code/bot.py
RUN pip install -r /code/requirements.txt
RUN chown root:root /code/
RUN chmod 701 /code/
# expect a build-time variable
ARG DISCORD_BOT_TOKEN
RUN test -n "$DISCORD_BOT_TOKEN"

# use the value to set the ENV var default
ENV DISCORD_BOT_TOKEN $DISCORD_BOT_TOKEN

CMD python /code/bot.py

#Create a new user
RUN useradd -ms /bin/bash jaskier
USER jaskier
WORKDIR /home/jaskier
COPY flag.txt /home/jaskier/flag.txt