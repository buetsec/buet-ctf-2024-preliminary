FROM ubuntu AS app
RUN apt-get update && apt-get upgrade -y

FROM pwn.red/jail
COPY --from=app / /srv
COPY flag.txt /srv/app/flag.txt
COPY chall /srv/app/run
