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
        ls = glob.glob(f"*.{x}")
    return ls
def getoneimages(imgdir,types):
    rphoto = getimages(imgdir,types)[random.randrange(0,len(ls))]
    return rphoto
