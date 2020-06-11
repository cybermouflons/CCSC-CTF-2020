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
RUN CGO_ENABLED=0 go build -o /ctf/harlans-world .

# final stage
FROM alpine:3.9

# Secure against running as root
RUN adduser -D -u 10000 ctf
USER ctf

WORKDIR /
COPY --from=build-env /ctf/harlans-world /

ENV CHALLENGE_PORT=":21337"
ENV CHALLENGE_FLAG="flag{M4ke_It_R4in_fr0m_Th3_Sky}"

EXPOSE 21337

CMD ["./harlans-world"]