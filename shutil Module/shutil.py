import shutil

shutil.copy("Lists.py","SampleofShutil.py")

shutil.copytree("VE","Copied")

shutil.move("break.py","IO Files")

shutil.rmtree("Copied")

# File Cannot be deleted so use os module for deletion of file


import os
os.remove("SampleofShutil.py") 

