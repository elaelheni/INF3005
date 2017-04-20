import uuid
from datetime import datetime, timedelta

def dffds():
    test = "sdfsdfs"
    email_token = uuid.uuid4()
    print email_token

dffds()
dffds()
dffds()
dffds()
dffds()
dffds()

ee = datetime.now() + timedelta(hours=9)
eee = str(ee)

print datetime.now() > ee
print ee
print "fdf"+ "dsf4"
datetime_object = datetime.strptime(eee, "%Y-%m-%d %H:%M:%S.%f")
print datetime_object < datetime.now()