FROM python:3.7

RUN apt-get update -y
RUN git clone https://github.com/emscripten-core/emsdk.git && \
    cd emsdk && \
    git pull && \
    ./emsdk install latest && \
    ./emsdk activate latest

ENV PATH="/emsdk:/emsdk/node/12.9.1_64bit/bin:/emsdk/upstream/emscripten:${PATH}"

COPY . /setup

WORKDIR /setup

RUN echo $PATH && make all

EXPOSE 8000

CMD ["python","-m","http.server","--directory","static/"]