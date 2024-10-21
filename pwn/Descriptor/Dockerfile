FROM python:slim AS app

FROM pwn.red/jail
COPY --from=app / /srv
COPY flag.txt /srv/app/flag.txt
COPY challenge.py /srv/app/chal.py
COPY run.sh /srv/app/run
