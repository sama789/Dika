from .associations import role_permission
from .. import db


# Permission Table 
class Permission(db.Model):
    __tablename__ = 'permissions'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)

    roles = db.relationship("Role", secondary=role_permission, back_populates="permissions")

    def __init__(self, name, roles=None):
        self.name = name
        self.roles = roles

    def __rep__(self):
        return '<{} {}>'.format(self.id, self.name)
