FROM golang:1.12.11-alpine3.9 AS build-env

# Allow Go to retrirve the dependencies for the build step
RUN apk add --no-cache git

RUN mkdir /ctf/ 
WORKDIR /ctf/
ADD . /ctf/

# Secure against running as root
RUN adduser -D -u 10000 ctf
RUN chown ctf -R /ctf/
USER ctf

# Compile the binary, we don't want to run the cgo resolver
RUN CGO_ENABLED=0 go build -o /ctf/rivia-scala-aldersberg .

# final stage
FROM alpine:3.9

# Secure against running as root
RUN adduser -D -u 10000 ctf
USER ctf

WORKDIR /
COPY --from=build-env /ctf/rivia-scala-aldersberg /

ENV CHALLENGE_PORT=":8080"
ENV CHALLENGE_FLAG="ccsc{1c0ecb7028e8c6aaed7e21652e9d9ed5}"

EXPOSE 8080

CMD ["./rivia-scala-aldersberg"]