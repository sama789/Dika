from app.model.permission import Permission
from app.repositories.worker import get_worker_by_username


# Create a permission object with all these attributes set to False by default.  
class Permissions:
    create_user = False
    read_user = False
    update_user = False
    delete_user = False
    create_shift = False
    read_shift = False
    update_shift = False
    delete_shift = False


def get_user_permissions(username):
    # get the user from Db with LowerCase 
    worker = get_worker_by_username(username.lower())
    permissions = Permissions()
    # check if the user is in our DB to enter the user only once 
    if worker is not None:
        for role in worker.roles:
            for permission in role.permissions:
                if permission.name == "read_user":
                    permissions.read_user = True
                if permission.name == "create_user":
                    permissions.create_user = True
                if permission.name == "delete_user":
                    permissions.delete_user = True
                if permission.name == "update_user":
                    permissions.update_user = True
                if permission.name == "read_shift":
                    permissions.read_shift = True
                if permission.name == "create_shift":
                    permissions.create_shift = True
                if permission.name == "delete_shift":
                    permissions.delete_shift = True
                if permission.name == "update_shift":
                    permissions.update_shift = True
        return permissions
    else:
        return permissions
''' 
check if the user has a role and which permissions he has
 return true or false  (For authorization)

'''


def check_permission(username, permission_name):
    worker = get_worker_by_username(username)
    permissions = set()
    for role in worker.roles:
        for permission in role.permissions:
            permissions.add(permission.name)
    return True if permission_name in list(permissions) else False


# get all the Permissions rfom DB 
def get_permissions():
    return Permission.query.all()


# get the permission by ID
def get_permission(per_id):
    return Permission.query.filter_by(id=per_id).first()

