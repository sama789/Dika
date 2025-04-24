from app import db 
from app.model.shift import Shift
from app.model.worker import Worker
from datetime import datetime


# create a new Shift
def create_shift(stype, status, start, end, worker_ids):
    stype = stype 
    status = status
    start = datetime.strptime(start, '%Y-%m-%dT%H:%M')
    end = datetime.strptime(end, '%Y-%m-%dT%H:%M')
    workers = []
    
    for i in worker_ids:
        worker = Worker.query.filter_by(id=int(i)).first()
        workers.append(worker)
        
    shift = Shift(stype=stype, status=status, start=start, end=end, workers=workers)
    db.session.add(shift)
    db.session.commit()

    
# delete shift by Id 
def delete_shift(shift_id):
    shift = Shift.query.filter_by(id=shift_id).first()
    db.session.delete(shift)
    db.session.commit()

    
# get all the Shifts    
def get_shifts():
    return Shift.query.all()


# get the shift by Id
def get_shift(shift_id):
    shift = Shift.query.filter_by(id=shift_id).first()
    shift.start_iso = shift.start.strftime('%Y-%m-%dT%H:%M')
    shift.end_iso = shift.end.strftime('%Y-%m-%dT%H:%M')
    if shift.status.name == "online":
        shift.status.online.selected = True
        shift.status.vor_ort.selected = False
    if shift.status.name == "vor_ort":
        shift.status.vor_ort.selected = True
        shift.status.online.selected = False
    if shift.stype.name == "usc_dienst":
        shift.stype.usc_dienst.selected = True
        shift.stype.wlan_beratung.selected = False
        shift.stype.drucker_dienst.selected = False
        shift.stype.pools_dienst.selected = False
    if shift.stype.name == "wlan_beratung":
        shift.stype.wlan_beratung.selected = True
        shift.stype.usc_dienst.selected = False
        shift.stype.drucker_dienst.selected = False
        shift.stype.pools_dienst.selected = False
    if shift.stype.name == "drucker_dienst":
        shift.stype.drucker_dienst.selected = True
        shift.stype.usc_dienst.selected = False
        shift.stype.wlan_beratung.selected = False
        shift.stype.pools_dienst.selected = False
    if shift.stype.name == "pools_dienst":
        shift.stype.pools_dienst.selected = True
        shift.stype.usc_dienst.selected = False
        shift.stype.wlan_beratung.selected = False
        shift.stype.drucker_dienst.selected = False
    return shift


# Edit a Shift     
def update_shift(shift_id, stype, status, start, end, worker_ids):
    shift = Shift.query.filter_by(id=shift_id).first() 
    
    # remove all old assigned workers
    shift.workers = []
    db.session.commit()
    
    for i in worker_ids:
        worker = Worker.query.filter_by(id=int(i)).first()
        shift.workers.append(worker)
     
    shift.stype = stype
    shift.status = status
    shift.start = datetime.strptime(start, '%Y-%m-%dT%H:%M')
    shift.end = datetime.strptime(end, '%Y-%m-%dT%H:%M')
    db.session.commit()
