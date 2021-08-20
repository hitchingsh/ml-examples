# Blenderbot Google Cloud Docker Example
This example hosts the small version of Blenderbot in Google Cloud within a Docker image. It uses the smallest version, the 90 million parameter model, which does not require a GPU or lots of memory to run.  The 400M parameter and 3 billion parameter models require both.

### Blenderbot
Blenderbot is a transformer model based on the Roberta architecture that was developed by the Facebook AI team as an interactive chatbot to have engaging casual conversation with humans.  This demo uses the 400 million parameter model but there is also a 2.7 billion, which performs better. Blenderbot2 remembers previous conversations and does a web search for the latest information. 

Blenderbog2 Paper: https://parl.ai/projects/blenderbot2/
Original Blenderbot Paper: https://arxiv.org/pdf/2004.13637.pdf

### ParlAI 
ParlAI (pronounced “par-lay”) is an open source python framework for sharing, training and testing dialogue models, from open-domain chitchat, to task-oriented dialogue, to visual question answering. This bot and code were taken from parlAI.

### Modifications
Improved the UI to the bot and packaged it up for deployment on Google Cloud

### Instructions

# Create a Google Cloud project with billing enabled
# Substitute your Google Cloud project ID for blenderbot90m

gcloud auth login
gcloud config set project blenderbot-306322
gcloud config set run/region us-west1
gcloud builds submit --tag gcr.io/blenderbot-306322/blenderbot90m --timeout=3600
gcloud run deploy --image gcr.io/blenderbot-306322/blenderbot90m:latest --platform managed --memory 4G --port 8080 --cpu 2

# The deploy command will tell you the URL you can go to for an interace web page to chat with Blenderbot
# Play around.  You are now done.
#################################

### Google Cloud Run Console
https://console.cloud.google.com/run/detail/us-west1/blenderbot/logs?project=blenderbot-306322

### Google Container Registry
https://console.cloud.google.com/gcr/images/blenderbot-306322?project=blenderbot-306322&folder&organizationId=236520584141

### More Info
For details on deploying a Docker image to Google cloud see: 
https://cloud.google.com/run/docs/quickstarts/build-and-deploy

#################################

# You can also use Docker to build locally and debug on your Mac

# Very first time on your machine only
gcloud auth configure-docker

# Login to docker
docker login -u imagical -p XXXXXXXX 

docker build -t blenderbot90m . 

docker run -p 8080:8080 blenderbot90m

# In a separate terminal window run to see memory usage
docker stats

# To run docker interactively starting with an image (to build large image)
docker run -it -p  8080:8080 --name blenderbot90mb blenderbot90m /bin/bash 

source blenderbot90m/bin/activate

echo '[EXIT]' | parlai interactive --model-file "zoo:blender/blender_90M/model" 

# Get container ID and then use it in the docker commit command
docker ps

# Save the new image, from outside the docker container sheell
docker commit b4f2bd5e13d7 blenderbot2

# Tag docker image
docker tag blenderbot2 gcr.io/blenderbot-306322/blenderbot2:latest
docker push gcr.io/blenderbot-306322/blenderbot2:latest

# Deploy to Google Cloud
gcloud run deploy --image gcr.io/blenderbot-306322/blenderbot2:latest --platform managed --memory 8G --port 8080 --cpu 2

#################################

# You can also run locally


# On dev machine setup env
cd virtual-environments
python3 -m venv blenderbot90m 
source blenderbot90m/bin/activate
cd blenderbot90m

# Install files
pip3 install --upgrade pip
pip3 install -r ../../glcoud-docker-images/blenderbot90m/requirements.txt 
echo '[EXIT]' | parlai interactive --model-file "zoo:blender/blender_90M/model"

# Run interactive blenderbot2 locally (when testing)
python -m parlai interactive --model-file zoo:blenderbot2/blender_90M/model 

# Run server on dev machine
python ./ParlAI/parlai/chat_service/services/browser_chat/run.py --config-path ../../gcloud-docker-images/blenderbot90m/config.yml --port 8000 &

# Run client server on dev machine
nice python ../../gcloud-docker-images/blenderbot90m/client.py --port 8000

lsof -nP -iTCP -sTCP:LISTEN | grep 8090
#kill -9 <process_id>

Once the deploy has finished it will show a URL you can go in order to begin interacting with the Blenderbotbut you will need to wait about 20 seconds for everything to full startup

This is a demo version. For making this production ready you'd want to consider the following:
* Faster initial response rather than the 15 second delay for loading in the Docker container (15 second delay)
* Not have to send and receive two messages initially (a couple of second delay)
* Consider breaking client.py and run.py into seperate images
* Consider converting to a buildpack
* Continuous integration setup or deploying from code
* Add a custom domain, HTTPS

### Tutorial for using Google App Engine (instead of Docker images)
https://cloud.google.com/appengine/docs/standard/python3/quickstart
