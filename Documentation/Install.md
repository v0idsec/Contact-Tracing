# Installation Guide for Contact Tracing Prototype

## Prerequisites
Ensure Python 3.7+ is installed on your machine.

## Install Dependencies
- Clone the repo: `git clone https://github.com/yourusername/contact-tracing.git`
- Install dependencies: `pip install -r requirements.txt`

## Running the Application
- Start the tracker with `python tracker.py`.
- Start the server with `python app.py`.

## Docker Setup
1. Build Docker container: `docker build -t contact-tracing .`
2. Run the container: `docker run -p 5672:5672 -p 15672:15672 contact-tracing`
