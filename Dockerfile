# Base image for Banana model builds
FROM pytorch/pytorch:1.11.0-cuda11.3-cudnn8-runtime

WORKDIR /

# Install git
RUN apt-get update && apt-get install -y git

# Install additional python packages
# torch is already installed in this image
RUN pip3 install --upgrade pip
ADD requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# Add and download your model weight files 
# (in this case we have a python script)
ADD download.py .
RUN python3 download.py

# Add the rest of your code
ADD . .

EXPOSE 8000

# Start the app in the container
CMD python3 -u app.py
