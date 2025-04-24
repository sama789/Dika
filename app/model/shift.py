from .associations import worker_shift
from .. import db

from sqlalchemy import Enum
import enum


# Shift's Status
class ShiftStatus(enum.Enum):
    online = "Online"
    vor_ort = "Vor Ort"


# Shift's Types
class ShiftType(enum.Enum):
    usc_dienst = 'USC Dienst'
    wlan_beratung = 'Wlan Beratung'
    drucker_dienst = 'Drucker Dienst'
    pools_dienst = 'Pools Dienst'


# Shift Table
class Shift(db.Model):
    __tablename__ = 'shifts'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    stype = db.Column(Enum(ShiftType))
    status = db.Column(Enum(ShiftStatus))
    start = db.Column(db.DATETIME(), nullable=False)
    end = db.Column(db.DATETIME(), nullable=False)

    workers = db.relationship("Worker", secondary=worker_shift, back_populates="shifts")

    def __init__(self, stype=None, status=None, start=None, end=None, workers=None):
        self.stype = stype
        self.status = status
        self.start = start
        self.end = end
        self.workers = workers

    def __rep__(self):
        return '<{} {} {} {} {}>'.format(self.id, self.stype, self.status, self.start, self.end)
