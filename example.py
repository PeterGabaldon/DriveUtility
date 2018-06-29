# !/usr/bin/env python
# -*- coding: utf-8 -*-

# Upload all conntents of Test folder.

from DriveUtil.drive import *
import os


#Initialize the Drive class.
drive = Drive(Auth())

#Get a list of all files in folder 'Test' and enter that dir.
files = os.listdir('Test')
os.chdir('Test')

#Finally call the Uplaod method with the path for each file in the 'Test' folder
for x in files:
	drive.Upload(os.path.abspath(x))

print 'Uploaded'	
