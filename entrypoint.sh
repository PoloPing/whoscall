flask db init
flask db migrate -m "Initial migration."
flask db upgrade

$ flask db stamp head  # To set the revision in the database to the head, without performing any migrations. You can change head to the required change you want.
$ flask db migrate     # To detect automatically all the changes.
$ flask db upgrade     # To apply all the changes.
flask test
