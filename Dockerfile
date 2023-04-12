FROM python:3-slim
WORKDIR /app
COPY ./github_action_main.py .
COPY tools /tools
RUN pip install -r /tools/requirements.txt
ENV PYTHONPATH /app
ENTRYPOINT ["/app/github_action_main.py"]

# This is for debugging the Docker image build process, ensures the container stays up
# ENTRYPOINT ["tail", "-f", "/dev/null"]
