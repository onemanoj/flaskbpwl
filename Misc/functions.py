import hashlib, binascii
import datetime, timeago 
import inspect
import types
from typing import cast

salt=b'13#0x/v\.Ki8'
def hash(mstr):
    dk = hashlib.pbkdf2_hmac('sha256', bytes(mstr,'utf-8'), salt, 100000)
    return binascii.hexlify(dk).decode("utf-8")

def b_hash(mstr):
    dk = hashlib.pbkdf2_hmac('sha256', bytes(mstr,'utf-8'), salt, 100000)
    return binascii.hexlify(dk)
    
def ago(mdt):
    # Calculate a '1 hours ago' type string from a python datetime.
    now = datetime.datetime.now() + datetime.timedelta(seconds = 60 )
    return (timeago.format(mdt, now)) 

def getFName(p1):
    mfn = datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S] ")
    mfn += cast(types.FrameType, inspect.currentframe().f_back).f_code.co_qualname 
    mfn += " " + str(p1)
    return mfn
