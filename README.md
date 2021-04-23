# heartbleed

## Execute the heartbleed exploit

`python heartbleed.py 127.0.0.1 -p 8443`

## Setup and run server

- Install docker and run the daemon
- Install the docker container with `docker pull hmlio/vaas-cve-2014-0160`
- Run the container with a port mapping `docker run -d -p 8443:443 hmlio/vaas-cvve-2014-0160`
- Open your browser and visit `https://localhost:8443/`

## Edit frontend

### One file

- `docker cp container_name:/var/www/index.html .`
- Edit the file locally
- `docker cp index.html container_name:/var/www/index.html`

### Entire directory

- `docker cp container_name:/var/www .`
- Edit the file locally
- `docker cp www container_name:/var/`
