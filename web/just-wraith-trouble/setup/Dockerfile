
FROM golang:1.12.11-alpine3.9 AS build-env

# Allow Go to retrieve the dependencies for the build step
RUN apk add --no-cache git

RUN mkdir /ctf/ 
WORKDIR /ctf/
ADD . /ctf/

# Secure against running as root
RUN adduser -D -u 10000 ctf
RUN chown ctf -R /ctf/
USER ctf

# Compile the binary, we don't want to run the cgo resolver
RUN CGO_ENABLED=0 go build -o /ctf/just-wraith-trouble .

# final stage
FROM alpine:3.9

# Secure against running as root
RUN adduser -D -u 10000 ctf
USER ctf

WORKDIR /
COPY --from=build-env /ctf/just-wraith-trouble /

ENV CHALLENGE_PORT=":8080"
ENV CHALLENGE_FLAG="ccsc{1e963f7df02c91a5355ddc6781e033ea}"
ENV CHALLENGE_SECRET="Y_-L@W_subMAR1N3"

EXPOSE 8080

CMD ["./just-wraith-trouble"]
