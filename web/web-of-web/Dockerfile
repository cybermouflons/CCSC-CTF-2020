FROM buildkite/puppeteer:v1.15.0
RUN apt-get update && npm i express cors

COPY run.sh /
COPY admin.js /
COPY api-server.js /
COPY flag-server.js /
ADD build.tar.gz /

RUN chmod +x /run.sh

ENTRYPOINT ["/run.sh"]
