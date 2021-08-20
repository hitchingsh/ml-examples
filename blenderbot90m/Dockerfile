# Use the official Python image.
# https://hub.docker.com/_/python
FROM python:3.7

# Allow statements and log messages to immediately appear in the Knative logs
ENV PYTHONUNBUFFERED True

# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./ 

# Install production dependencies.
RUN cd /app && \
    python3 -m venv blenderbot90m && \
    . ./blenderbot90m/bin/activate && \
    pip3 install --upgrade pip && \
    pip3 install -r /app/requirements.txt && \
    echo '[EXIT]' | parlai interactive --model-file "zoo:blender/blender_90M/model"

# Note, for true production follow the best practices such as breaking up into an executable
# for each server and removing utilities like netcat
# https://cloud.google.com/solutions/best-practices-for-building-containers
CMD ./run-blenderbot.bsh
EXPOSE 8080
