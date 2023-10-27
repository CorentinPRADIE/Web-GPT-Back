# Set base image (host OS)
FROM python:3.11

# By default, listen on port 5000
EXPOSE 5000/tcp

# Set the working directory in the container
WORKDIR /app

ARG BING_SEARCH_V7_SUBSCRIPTION_KEY=f0fdadbbd5784a46aca726cfcf2a14fe

ARG OPENAI_API_KEY=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

# Copy the dependencies file to the working directory
COPY requirements.txt .

RUN apt-get update && apt-get install -y gcc

# Install any dependencies
RUN pip install -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY . ./

# Specify the command to run on container start
CMD [ "python", "./app.py" ]
