FROM ubuntu AS app
RUN apt-get update && apt-get upgrade -y

FROM pwn.red/jail
COPY --from=app / /srv
ENV JAIL_ENV_FLAG="BUETCTF{GRExipe3756rGASYRD9DiZS}"
COPY server /srv/app/run
