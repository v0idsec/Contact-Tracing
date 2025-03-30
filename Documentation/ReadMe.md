# Contact Tracing Prototype

## Overview
This is a contact tracing prototype built using RabbitMQ and Python. It tracks the movement of people across a grid and updates their contact information in real-time.

## Setup
1. Clone the repository
2. Run `pip install -r requirements.txt` to install dependencies.
3. Run the application by executing `python app.py`.

## Components
- Tracker: Monitors movements and updates contact info.
- Person: Defines the people in the system.
- Query: Allows for querying contacts.

## Docker
If you're using Docker, follow these steps:
1. Build the Docker container: `docker build -t contact-tracing .`
2. Run the container: `docker run -p 5672:5672 -p 15672:15672 contact-tracing`
