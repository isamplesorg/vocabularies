FROM python:3-slim
ADD . /app
WORKDIR /app
COPY tools /tools
RUN pip install -f /app/tools/requirements.txt

ENTRYPOINT ["/github_action_main.py"]