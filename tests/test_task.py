import unittest
from flask_testing import TestCase
from app import create_app, db
from task.models import Task


class SettingBase(TestCase):
    def create_app(self):
        app = create_app("testing")

        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:pass1234@db/test"
        app.config['PRESERVE_CONTEXT_ON_EXCEPTION'] = False
        db.init_app(app)
        from task.api import bp as task_bp
        app.register_blueprint(task_bp, url_prefix='/task')
        return app

    def setUp(self):
        engine = db.create_engine('mysql+pymysql://root:pass1234@db', {})
        create_str = "CREATE DATABASE IF NOT EXISTS test ;"
        engine.execute(create_str)
        engine.execute("USE test;")

        db.create_all()
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class CheckTask(SettingBase):
    def test_get_all(self):
        task1 = Task().add_task(name="task1", status=0)
        task2 = Task().add_task(name="task2", status=0)
        resp = self.client.get('/task/')
        assert resp.status_code == 200
        expect = [task1, task2]
        assert resp.get_json() == expect

    def test_get_by_id(self):
        task1 = Task().add_task(name="task1", status=0)
        task2 = Task().add_task(name="task2", status=0)
        task3 = Task().add_task(name="task3", status=0)
        resp = self.client.get('/task/3')
        assert resp.status_code == 200
        expect = [task3]
        assert resp.get_json() == expect

    def test_get_by_id_not_exits(self):
        task1 = Task().add_task(name="task1", status=0)
        task2 = Task().add_task(name="task2", status=0)
        task3 = Task().add_task(name="task3", status=0)
        resp = self.client.get('/task/4')
        assert resp.status_code == 200
        expect = []
        assert resp.get_json() == expect

    def test_create(self):
        task1 = Task().add_task(name="task1", status=0)
        data = {"name": "test2", "status": 0}
        resp = self.client.post('/task/', json=data, follow_redirects=True)
        assert resp.status_code == 201
        data['id'] = 2
        assert resp.get_json() == data

    def test_create_no_name(self):
        task1 = Task().add_task(name="task1")
        data = {"status": 0}
        resp = self.client.post('/task/', json=data, follow_redirects=True)
        assert resp.status_code == 400

    def test_create_no_status(self):
        task1 = Task().add_task(name="task1")
        data = {"name": "test2"}
        resp = self.client.post('/task/', json=data, follow_redirects=True)
        assert resp.status_code == 400

    def test_update(self):
        task1 = Task().add_task(name="task1")
        task1['name'] = 'test3'
        resp = self.client.put('/task/1', json=task1, follow_redirects=True)
        expect = task1
        assert resp.status_code == 200
        assert resp.get_json() == expect

    def test_update_no_name(self):
        task1 = Task().add_task(name="task1")
        task1.pop('name')
        resp = self.client.put('/task/1', json=task1, follow_redirects=True)
        assert resp.status_code == 400

    def test_update_no_status(self):
        task1 = Task().add_task(name="task1")
        task1.pop('status')
        resp = self.client.put('/task/1', json=task1, follow_redirects=True)
        assert resp.status_code == 400

    def test_delete(self):
        task1 = Task().add_task(name="task1")
        task2 = Task().add_task(name="task2")
        resp = self.client.delete('/task/1', json=task1, follow_redirects=True)
        assert resp.status_code == 200
        resp = self.client.get('/task/')
        assert len(resp.get_json()) == 1

if __name__ == '__main__':
    unittest.main()
