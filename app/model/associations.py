from .. import db

# worker_shift junction table
worker_shift = db.Table('worker_shift',
                        db.Column('shift_id', db.Integer,
                                  db.ForeignKey('shifts.id', ondelete="CASCADE", onupdate="CASCADE")),
                        db.Column('worker_id', db.Integer,
                                  db.ForeignKey('workers.id', ondelete="CASCADE", onupdate="CASCADE"))
                        )

# role_worker junction table
role_worker = db.Table('role_worker',
                       db.Column('role_id', db.Integer,
                                 db.ForeignKey('roles.id', ondelete="CASCADE", onupdate="CASCADE")),
                       db.Column('worker_id', db.Integer,
                                 db.ForeignKey('workers.id', ondelete="CASCADE", onupdate="CASCADE"))
                       )

# role_permission junction table
role_permission = db.Table('role_permission',
                           db.Column('role_id', db.Integer,
                                     db.ForeignKey('roles.id', ondelete="CASCADE", onupdate="CASCADE")),
                           db.Column('permission_id', db.Integer,
                                     db.ForeignKey('permissions.id', ondelete="CASCADE", onupdate="CASCADE"))
                           )
