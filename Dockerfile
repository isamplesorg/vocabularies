FROM python:3.11.3-slim-bullseye
COPY entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]