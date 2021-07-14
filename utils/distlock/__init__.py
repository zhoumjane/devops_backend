#coding:utf-8
import time

from contextlib import contextmanager
from random import random

DEFAULT_EXPIRES = 15
DEFAULT_RETRIES = 5

@contextmanager
def dist_lock(key, client):
    key = 'lock_%s' % key

    try:
        t = _acquire_lock(key, client)
        yield t
    finally:
        _release_lock(key, client)

def ask_lock(key,client):
    key = 'lock_%s' % key
    if client.get(key):
        return True
    else:
        return False
    

def _acquire_lock(key, client):
    while 1:
        get_stored = client.get(key)
        if get_stored:
            time.sleep(0.03)
        else:
            if client.setnx(key, 1):
                client.expire(key,DEFAULT_EXPIRES)
                return True
    return False

def _release_lock(key, client):
    client.delete(key)
