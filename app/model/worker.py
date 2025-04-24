from .associations import worker_shift, role_worker
from .. import db


# Worker Table
class Worker(db.Model):
    __tablename__ = 'workers'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    
    shifts = db.relationship("Shift", secondary=worker_shift, back_populates="workers",)
    roles = db.relationship("Role", secondary=role_worker, back_populates="workers",)
     
    def __init__(self, name, email, roles=None):
        self.name = name
        self.email = email
        self.roles = roles
    
    def __rep__(self):
        return '<{} {}>'.format(self.id, self.email, self.name)
