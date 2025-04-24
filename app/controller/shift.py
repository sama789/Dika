from flask import render_template, request, redirect, url_for
from app.utils.authentication import get_authenticated_user
from .. import app
from ..repositories.shift import get_shifts, get_shift, create_shift, update_shift, delete_shift
from ..repositories.worker import get_workers


# get the List of all the Shifts in our DB 
@app.route('/shift/list', methods=['GET'])
def shift_list():
    if request.method == 'GET':
        shifts = get_shifts()
        workers = get_workers()
        user = get_authenticated_user()
       
        for worker in workers:
            if user.uid == worker.name:
                return render_template('shift/calendar.html', shifts=shifts)
        return render_template('shift/calendar_user.html', shifts=shifts)


# delete Shift by ID    
@app.route('/shift/delete/<int:sid>', methods=['POST'])
def shift_delete(sid):
    if request.method == 'POST':
        delete_shift(sid)
        return redirect(url_for(('shift_list')))

  
@app.route('/shift/read/<int:sid>', methods=['GET'])
def shift_read(sid):
    if request.method == 'GET':
        shift = get_shift(sid)
        return render_template('shift/read.html', shift=shift)
    
    
# get the Shift by Id with his features and Edit it   
@app.route('/shift/edit/<int:sid>', methods=['POST', 'GET'])
def shift_edit(sid):
    if request.method == 'GET':
        shift = get_shift(sid)
        workers = get_workers()
        for worker in workers:
            if worker in shift.workers:
                worker.selected = True
            else:
                worker.selected = False
        return render_template('shift/edit.html', shift=shift, workers=workers,)

    if request.method == 'POST':
        sid = sid
        stype = request.form['stype'] 
        print(sid)
        status = request.form['status']
        start = request.form['start']
        end = request.form['end']
        workerIds = request.form.getlist('workers')
        update_shift(sid, stype, status, start, end, workerIds)
        return redirect(url_for('shift_list'))

        
# create a new Shift,and choice his features then save it in our DB 
@app.route('/shift/add', methods=['POST', 'GET'])
def shift_create():
    if request.method == 'GET':
        workers = get_workers()
        return render_template('shift/add.html', workers=workers)

    if request.method == 'POST':
        stype = request.form['stype']
        status = request.form['status']
        start = request.form['start']
        end = request.form['end']
        workerIds = request.form.getlist('workers')
        create_shift(stype, status, start, end, workerIds)
        return redirect(url_for(('shift_list')))
