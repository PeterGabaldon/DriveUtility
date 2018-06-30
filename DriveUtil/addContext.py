# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Pedro Gabaldon

from _winreg import *
import os

dirBackPath = "Directory\\Background\\shell\\"
dirPath = "Directory\\shell\\"
anyExtPath = "*\\shell\\"

removeAuthK = SetValue(CreateKey(HKEY_CLASSES_ROOT, dirBackPath + "Remove Drive access"), "command", REG_SZ, os.path.dirname(__file__) + "\\cmd\\removeOauth.bat")

newFolderK = SetValue(CreateKey(HKEY_CLASSES_ROOT, dirBackPath + "New Drive folder"), "command", REG_SZ, os.path.dirname(__file__) + "\\cmd\\createFolder.bat")

deleteK = SetValue(CreateKey(HKEY_CLASSES_ROOT, dirBackPath + "Delete Drive file/folder"), "command", REG_SZ, os.path.dirname(__file__) + "\\cmd\\delete.bat")

updirK = SetValue(CreateKey(HKEY_CLASSES_ROOT, dirPath + "Upload Drive"), "command", REG_SZ, "\"" + os.path.dirname(__file__) + "\\cmd\\upload.bat" + "\"" + " \"%1\"")
upAnyExtK = SetValue(CreateKey(HKEY_CLASSES_ROOT, anyExtPath + "Upload Drive"), "command", REG_SZ, "\"" + os.path.dirname(__file__) + "\\cmd\\upload.bat" + "\"" + " \"%1\"")

updirSK = SetValue(CreateKey(HKEY_CLASSES_ROOT, dirPath + "Upload Drive(Specific)"), "command", REG_SZ, "\"" + os.path.dirname(__file__) + "\\cmd\\upload (specific).bat" + "\"" + " \"%1\"")
upAnyExtSK = SetValue(CreateKey(HKEY_CLASSES_ROOT, anyExtPath + "Upload Drive(Specific)"), "command", REG_SZ, "\"" + os.path.dirname(__file__) + "\\cmd\\upload (specific).bat" + "\"" + " \"%1\"")

print 'Added'
