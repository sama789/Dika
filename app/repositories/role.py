from app import db
from app.model.permission import Permission
from app.model.role import Role
from app.model.worker import Worker


# create a new Role 
def create_role(name, worker_ids, permission_ids):
    name = name
    workers = []
    permissions = []
    for i in worker_ids:
        worker = Worker.query.filter_by(id=int(i)).first()
        workers.append(worker)
        
    for i in permission_ids:
        permission = Permission.query.filter_by(id=int(i)).first()
        permissions.append(permission)
        
    role = Role(name=name, workers=workers, permissions=permissions)
    db.session.add(role)
    db.session.commit()


# delete a Role by Id 
def delete_role(role_id):
    role = Role.query.filter_by(id=role_id).first()
    db.session.delete(role)
    db.session.commit()


# get all the Roles   
def get_roles():
    return Role.query.all()


# get a Role by ID 
def get_role(role_id):
    return Role.query.filter_by(id=role_id).first()


# Edite  Role
def update_role(role_id, name, worker_ids, permission_ids):
    role = Role.query.filter_by(id=role_id).first()
    
    role.workers = []
    role.permissions = []
    
    for i in worker_ids:
        worker = Worker.query.filter_by(id=int(i)).first()
        role.workers.append(worker)
        
    for i in permission_ids:
        permission = Permission.query.filter_by(id=int(id)).first()
        role.permissions.append(permission)
        
    role.name = name 
    db.session.commit()
        
