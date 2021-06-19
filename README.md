## Whoscall Test

#### Notice: It might take some times for db init, please check db first.

#### Install Docker
https://docs.docker.com/docker-for-mac/install/


#### Run Repository
docker-compose -f dev_backend.yaml up -d

#### init db
$ flask db stamp head  # To set the revision in the database to the head, without performing any migrations. You can change head to the required change you want.
$ flask db migrate     # To detect automatically all the changes.
$ flask db upgrade     # To apply all the changes.


#### Test Command
docker exec -it whoscall_web_1 bash
flask test
