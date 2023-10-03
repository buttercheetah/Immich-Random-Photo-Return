# Immich Random Photo Return Application
This repository contains the source code for the Immich Random Photo Return application. The application fetches a random image from the Immich API and serves it over a Flask web server. It is designed to be deployed using Docker.

## Getting Started
Follow the instructions below to set up and run the application.

### Setup
Docker: Make sure you have Docker installed on your system. For installation instructions, visit Docker documentation.
Building the Docker Image


### Docker Compose
1. Clone this repository to your local machine.
    ```shell
    git clone https://glcr.domain.tld/user/Immich-Random-Photo-Return
    cd Immich-Random-Photo-Return
    ```
2. Change docker-compose env variables
3. Run the Docker container using the built image.
    `docker compose up -d`

The application will now be accessible at http://localhost:9996.
### Docker Cli
`docker run -d --restart=unless-stopped -p 9996:5000 -e IMMICH_API_URL=<API_URL> -e IMMICH_API_KEY=<API_KEY> glcr.iefi.xyz/bhghdhfh/immich-random-photo-return:latest`
