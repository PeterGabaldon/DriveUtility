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

from main import *

def clean():
	cred = Auth()

	response = cred.files().emptyTrash().execute()

	print 'Cleaned'
	print 'Byeee!'

if __name__ == '__main__':
	clean()	