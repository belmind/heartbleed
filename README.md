# heartbleed

## Setup and run server

- Install docker and run the daemon
- Install the docker container with `docker pull hmlio/vaas-cve-2014-0160`
- Run the container with a port mapping `docker run -d -p 8443:443 hmlio/vaas-cvve-2014-0160`
- Open your browser and visit `https://localhost:8443/`
