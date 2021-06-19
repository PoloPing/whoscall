## Whoscall Test

#### Notice: It might take some times for db init, please check db first.

### Install Docker
https://docs.docker.com/docker-for-mac/install/


### Run Repository
docker-compose -f dev_backend.yaml up -d

### init db
docker exec -it whoscall_web_1 bash

flask db stamp head

flask db migrate

flask db upgrade


### Test Command
docker exec -it whoscall_web_1 bash

flask test
