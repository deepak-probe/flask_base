# Docker Flask App Demo CICD Gitlab Readme

### How to run this app locally on Docker
* Make sure Docker is installed 
* Run command: `docker-compose up`
* Note that if you make changes to `Dockerfile` or `requirements.txt`, you will need to run command: `docker-compose build` to rebuild the image.
* After running the app, it should be located at `http://localhost/` (port 80). Note this is an override of the default port 5000 for Flask apps, but on M1 macs, port 5000 is sometimes used by a process. 
* To stop the running web server from terminal, press Control + C on the keyboard.

### Unit and Integration Tests 
Pytest is used to run unit and integ tests for this app. To run pytest from a locally, run cmd: `python3 -m pytest`

### CI/CD Pipeline 
The .gitlab-ci.yml file is where we define the stages and jobs for each stage to due test + build + deploy processes. 
