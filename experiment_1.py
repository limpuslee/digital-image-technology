import string
import  numpy as np
import struct
import matplotlib.pyplot as plt
f = open("33655.bmp","rb")
outfile = open("digit.txt","w")
while 1:
    c = f.read(1)
    if not c:
        break
    else:
        if ord(c) <= 15:
            outfile.write(("0"+hex(ord(c))[2:]))
        else:
            outfile.write(hex(ord(c))[2:])
outfile.close()
f.close()