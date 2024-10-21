FROM ubuntu AS app
RUN apt-get update && apt-get upgrade -y

FROM pwn.red/jail
COPY --from=app / /srv
ENV JAIL_ENV_FLAG="BUETCTF{G6VjZel2DYbziar516JWgWT}"
COPY server /srv/app/run
