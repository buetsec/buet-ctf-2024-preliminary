FROM python:slim AS app

FROM pwn.red/jail
COPY --from=app / /srv
COPY grid.py /srv/app/chal.py
COPY run.sh /srv/app/run
