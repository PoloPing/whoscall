from whoscall import create_app, db
from flask_migrate import Migrate

app = create_app()
db.init_app(app)
migrate = Migrate(app, db)

from task.api import bp as task_bp
app.register_blueprint(task_bp, url_prefix='/task')


@app.cli.command()
def test():
    import unittest
    import sys

    tests = unittest.TestLoader().discover("tests")
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.errors or result.failures:
        sys.exit(1)


if __name__ == '__main__':
    app.run()
