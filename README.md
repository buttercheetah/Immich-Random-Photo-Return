# Random-Photo-Return
A simple Python flask script to return a random photo in a directory everytime the webpage loads

This application was made over the span of 1 hour. It is not made to be used for anything other than messing around. Be warned that this code is not bug tested nor is it to be relied upon. However, it does work most of the time

## Deployment
| Docker run `docker run -d --restart=unless-stopped -p 9996:5000 -v /dir/to/photos:/images glcr.iefi.xyz/bhghdhfh/random-photo-return:latest`

| download the docker compose file and run `docker compose up -d`