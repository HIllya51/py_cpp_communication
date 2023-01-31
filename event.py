     
import time
import os 
from traceback import print_exc

import win32pipe, win32file,win32con,win32event,win32security
attr=win32security.SECURITY_DESCRIPTOR(win32con.SECURITY_DESCRIPTOR_REVISION)
attr.SetSecurityDescriptorDacl(True,None,False) 
secu=win32security.SECURITY_ATTRIBUTES() 
secu.SECURITY_DESCRIPTOR=attr
secu.bInheritHandle=False
event=win32event.CreateEvent(secu,False, False,  "testtest")
win32event.SetEvent(event)
 