from flask import render_template
from app import app
from app.repositories.permission import get_user_permissions
from app.utils.authentication import get_authenticated_user
from app.repositories.worker import get_worker_by_username


# Send data to all tampletes  
@app.context_processor
def inject_user():
    # get logged in user's Info 
    user = get_authenticated_user()
    # getting the user from the DB, if it existed, set the value True, if not set it False
    exists = bool(get_worker_by_username(user.uid))
    # get the User's permission 
    permissions = get_user_permissions(user.uid)
    return dict(user=user, permissions=permissions, exists=exists)


@app.route("/", methods=["POST", "GET"])
def index():
    return render_template('index.html')


# run the Server 
if __name__ == '__main__':
    # db.create_all()
    app.run(port=2009, debug=True)
