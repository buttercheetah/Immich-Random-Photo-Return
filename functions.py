import os
import random
import time
import platform
import glob

def getimages(imgdir,types):
    if type(types) != list:
        types = [types]
    os.chdir(imgdir)
    ls = []
    for x in types:
        ls.extend(glob.glob(f"*.{x}")) 
    return ls
def getoneimages(imgdir,types):
    ls = getimages(imgdir,types)
    rphoto = ls[random.randrange(0,len(ls))]
    return rphoto
