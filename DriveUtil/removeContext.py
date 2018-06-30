#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Pedro Gabaldon

from _winreg import *
import os

delete = DeleteKey(HKEY_CLASSES_ROOT, "Directory\\Background\\shell\\Remove Drive access\\command")
delete = DeleteKey(HKEY_CLASSES_ROOT, "Directory\\Background\\shell\\Remove Drive access")

delete = DeleteKey(HKEY_CLASSES_ROOT, "Directory\\Background\\shell\\List drive files\\command")
delete = DeleteKey(HKEY_CLASSES_ROOT, "Directory\\Background\\shell\\List drive files")

delete = DeleteKey(HKEY_CLASSES_ROOT, "Directory\\Background\\shell\\Drive download here\\command")
delete = DeleteKey(HKEY_CLASSES_ROOT, "Directory\\Background\\shell\\Drive download here")

delete = DeleteKey(HKEY_CLASSES_ROOT, "Directory\\Background\\shell\\Move Drive files/folders\\command")
delete = DeleteKey(HKEY_CLASSES_ROOT, "Directory\\Background\\shell\\Move Drive files/folders")

delete = DeleteKey(HKEY_CLASSES_ROOT, "Directory\\Background\\shell\\New Drive folder\\command")
delete = DeleteKey(HKEY_CLASSES_ROOT, "Directory\\Background\\shell\\New Drive folder")

delete = DeleteKey(HKEY_CLASSES_ROOT, "Directory\\Background\\shell\\Delete Drive file/folder\\command")
delete = DeleteKey(HKEY_CLASSES_ROOT, "Directory\\Background\\shell\\Delete Drive file/folder")

delete = DeleteKey(HKEY_CLASSES_ROOT, "Directory\\shell\\Upload Drive\\command")
delete = DeleteKey(HKEY_CLASSES_ROOT, "Directory\\shell\\Upload Drive")
delete = DeleteKey(HKEY_CLASSES_ROOT, "*\\shell\\Upload Drive\\command")
delete = DeleteKey(HKEY_CLASSES_ROOT, "*\\shell\\Upload Drive")

delete = DeleteKey(HKEY_CLASSES_ROOT, "Directory\\shell\\Upload Drive(Specific)\\command")
delete = DeleteKey(HKEY_CLASSES_ROOT, "Directory\\shell\\Upload Drive(Specific)")
delete = DeleteKey(HKEY_CLASSES_ROOT, "*\\shell\\Upload Drive(Specific)\\command")
delete = DeleteKey(HKEY_CLASSES_ROOT, "*\\shell\\Upload Drive(Specific)")

print 'Removed'
