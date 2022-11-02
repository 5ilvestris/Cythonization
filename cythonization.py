import os
import glob
from pyperclip import copy
from setuptools import setup
from Cython.Build import cythonize
folder=os.getcwd()
os.chdir(str(folder) + "/PyxScripts")
files=(glob.glob("*.pyx"))
num=len(files)
x=0
while x<num:
    print(files[x])
    setup(
        name="Silvestris",
        ext_modules=cythonize(files[x]),
        zip_safe=False
    )
    x=x+1
