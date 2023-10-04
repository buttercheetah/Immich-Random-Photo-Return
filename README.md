# Immich Random Photo Return Application
This repository contains the source code for the Immich Random Photo Return application. The application fetches a random image from the Immich API and serves it over a Flask web server. It is designed to be deployed using Docker.

## Getting Started
Follow the instructions below to set up and run the application.

### Setup
Docker: Make sure you have Docker installed on your system. For installation instructions, visit Docker documentation.
Building the Docker Image

***
**Note**: Setting the environment variable `IMMICH_ALBUM` will only get images from the specified album. However, since Immich has no api request for such a feat, it gets data of all items in the album at startup. It chooses a random image at each request. This means that it should load faster than getting all images, but while having a higher memory footprint. There is also the side effect of a longer startup time.
***
**Important**: The Immich album variable should be a uuid, not the title of the album. 
- :x: family
- :heavy_check_mark: d3ef890e-e227-433e-9493-47af3e5dd598
***

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
```
docker run -d --restart=unless-stopped \
-p 9996:5000 \
-e IMMICH_API_URL=<API_URL> \
-e IMMICH_API_KEY=<API_KEY> \
-e TIMEZONE=UTC \
-e IMMICH_ALBUM=all \
glcr.iefi.xyz/bhghdhfh/immich-random-photo-return:latest
```
