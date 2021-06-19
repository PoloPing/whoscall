from whoscall import db


class Task(db.Model):
    __tablename__ = 'task'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.VARCHAR(30), nullable=False)
    status = db.Column(db.Integer, default=0)

    @staticmethod
    def to_dict(task):
        return {'id': task.id, 'name': task.name, 'status':task.status}

    def get_all_tasks(self):
        data = []
        for task in self.query.all():
            data.append(Task.to_dict(task))
        return data

    def get_task(self, _id):
        data = []
        for task in self.query.filter_by(id=_id):
            data.append(Task.to_dict(task))
        return data

    def add_task(self, name, status=0):
        new_task = Task(name=name, status=status)
        db.session.add(new_task)
        db.session.commit()
        return self.to_dict(new_task)

    def update_task(self, _id, *args, **kwargs):
        task = self.query.filter_by(id=_id).first()
        if not task:
            return "Task not exits."
        for key, value in kwargs.items():
            if hasattr(task, key):
                setattr(task, key, value)
        db.session.add(task)
        db.session.commit()
        return self.to_dict(task)

    def delete_task(self, _id):
        Task.query.filter_by(id=_id).delete()
        db.session.commit()




