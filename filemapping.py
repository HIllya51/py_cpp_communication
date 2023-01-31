     
# import time
# import os 
# from traceback import print_exc
# from ctypes import windll,c_char_p,cast
# FILE_MAP_EXECUTE=0x0020
# FILE_MAP_ALL_ACCESS=0xF001F
# import win32pipe, win32file,win32con,win32event,win32security,win32file,win32api
# fm=windll.kernel32.OpenFileMappingW(FILE_MAP_ALL_ACCESS|FILE_MAP_EXECUTE, False,"testfmap")#c_char_p("testfmap".encode('utf16')))
# pBuf = windll.kernel32.MapViewOfFile(fm, FILE_MAP_ALL_ACCESS, 0, 0, 1024)
# print(pBuf)
# pBuf=cast(pBuf,c_char_p)
# print(pBuf.value )


import mmap
hmem = mmap.mmap(0, 1024, "testfmap", mmap.ACCESS_READ)
for i in range(5):
    x=hmem.read()
    print(x)
    print(x.decode())