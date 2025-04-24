from app.model.role import Role
from app.model.worker import Worker
from app import db


# create a new Worker 
def create_worker(name, email, role_ids):
    worker = get_worker_by_username(name)
    if worker is None:
        name = name
        email = email
        roles = []

        for i in role_ids:
            role = Role.query.filter_by(id=int(i)).first()
            roles.append(role)

        worker = Worker(name=name, email=email, roles=roles)
        db.session.add(worker)
        db.session.commit()


# delete Worker by id 
def delete_worker(worker_id):
    worker = Worker.query.filter_by(id=worker_id).first()
    db.session.delete(worker)
    db.session.commit()


# get Worker by Email
def get_worker_by_username(username):
    return Worker.query.filter_by(name=username).first()


# get all the workers 
def get_workers():
    return Worker.query.all()


# get worker by id
def get_worker(worker_id):
    return Worker.query.filter_by(id=worker_id).first()


# Edit worker 
def update_worker(worker_id, name, email, role_ids):
    worker = Worker.query.filter_by(id=worker_id).first()

    # remove all old assigned roles
    worker.roles = []
    db.session.commit()

    for i in role_ids:
        role = Role.query.filter_by(id=int(i)).first()
        worker.roles.append(role)

    worker.name = name.lower()
    worker.email = email.lower()

    db.session.commit()
