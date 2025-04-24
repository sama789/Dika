from app import app
from flask import render_template, request, redirect, url_for
from app.repositories.role import get_roles
from app.repositories.worker import create_worker, delete_worker, get_workers, get_worker, update_worker


# get the List of all the Workers in our DB
@app.route('/worker/list', methods=['GET'])
def worker_list():
    if request.method == 'GET':
        workers = get_workers()
        return render_template('worker/list.html', workers=workers)


# delete Worker by ID 
@app.route('/worker/delete/<int:wid>', methods=['GET', 'POST'])
def worker_delete(wid):
    if request.method == 'POST':
        delete_worker(wid)
        return redirect(url_for(('worker_list')))


# get the worker by ID with all his features and Edit it 
@app.route('/worker/edit/<int:wid>', methods=['GET', 'POST'])
def worker_edit(wid):
    if request.method == 'GET':
        worker = get_worker(wid)
        roles = get_roles()

        for role in roles:
            if role in worker.roles:
                role.selected = True
            else:
                role.selected = False

        return render_template('worker/edit.html', worker=worker, roles=roles)

    if request.method == 'POST':
        wid = wid
        name = request.form['username']
        email = request.form['email']
        rolesIds = request.form.getlist("roles")
        update_worker(wid, name, email, rolesIds)
        return redirect(url_for(('worker_list')))


# Post Method: create a new Worker and choice the features all,then save it in our DB 
@app.route('/worker/add', methods=['GET', 'POST'])
def worker_create():
    if request.method == 'GET':
        roles = get_roles()
        return render_template('worker/add.html', roles=roles)

    if request.method == 'POST':
        name = request.form['username']
        email = request.form['email']
        rolesIds = request.form.getlist("roles")
        create_worker(name, email, rolesIds)
        return redirect(url_for(('worker_list')))
