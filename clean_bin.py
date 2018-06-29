# !/usr/bin/env python
# -*- coding: utf-8 -*-

#
#
# Copyright (c) 2018 Pedro Gabaldon
#
#
# Licensed under MIT License. See LICENSE
#
#

from DriveUtil.main import *

cred = Auth()

response = cred.files().emptyTrash().execute()

print 'Cleaned'
print 'Byeee!'