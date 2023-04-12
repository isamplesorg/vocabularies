FROM python:3-slim
WORKDIR /app
COPY tools /tools
RUN pip install -r /tools/requirements.txt

ENTRYPOINT ["/github_action_main.py"]

# This is for debugging the Docker image build process, ensures the container stays up
# ENTRYPOINT ["tail", "-f", "/dev/null"]
