from .associations import role_worker, role_permission
from .. import db


# Role Table 
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    
    workers = db.relationship("Worker", secondary=role_worker, back_populates="roles")
    permissions = db.relationship("Permission", secondary=role_permission, back_populates="roles")
 
    def __init__(self, name=None , workers=None, permissions=None):
        self.name = name
        self.workers = workers
        self.permissions = permissions
        
    def __rep__(self):
        return'<{} {}>'.format(self.id, self.name)
