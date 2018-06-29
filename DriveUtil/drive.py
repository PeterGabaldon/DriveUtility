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

"""
tools.py - Contain other Google Drive operations

Example:
	
	import tools
	
	cred = tools.Auth()
	drive = tools.Drive(cred)

	drive.Move()
	drive.AddStar("example.txt")

"""

from main import *

"""
	This class inherits from Drive class and hold other Google Drive operations
	Constructor parameters:
		-drive: Drive api object
"""
class Drive(mainDrive):
	def __init__(self, drive):
		super(Drive, self).__init__(drive)
		self.drive = drive

	"""
		Move a file/folder
		Return:
			-True if successful
			-False if it fails
	"""	
	def Move(self):
		print 'Select wich file/folder move: '
		moveId = super(Drive, self).List(SelectId=True)
		response = self.drive.files().get(fileId=moveId, fields='parents').execute()
		parents = ",".join(response.get('parents'))
		moveRoot = raw_input('Do you want to move it to My Drive? (Y/N): ')

		if moveRoot in ['Y', 'y']:
			try:
				response = self.drive.files().update(fileId=moveId, removeParents=parents, addParents='root').execute()
				print 'Moved!'
				return True
			except HttpError as err:
				if err.resp.status == 403:
					print 'You are not allowed to move it'
					return False
				else:
					raise
		else:
			print 'Select where to move: '
			moveTo = super(Drive, self).List(SelectId=True, OnlyFolder=True)
			try:
				response = self.drive.files().update(fileId=moveId, removeParents=parents, addParents=moveTo).execute()
				'Moved!'
				return True
			except HttpError as err:
				if err.resp.status == 403:
					print 'You are not allowed to move it'
					return False
				else:
					raise

	"""
		This method will add a star to the selected folder/file
		Return:
			-True if successful
			-False if it fails
	"""
	def AddStar(self):
		metadata = {'starred' : 'true'}
		print 'Selec file/folder to add star: '
		starId = super(Drive, self).List(SelectId=True)
		if starId:
			try:
				response = self.drive.files().update(fileId=starId, body=metadata).execute()
				print 'Starred'
				return True
			except HttpError as err:
				if err.resp.status == 403:
					print 'You are not allowed to move it'
					return False
				else:
					raise
		else:
			return False			

	"""
		This method will remove the star of the selected folder/file
		Return:
			-True if successful
			-False if it fails
	"""			
	def RemoveStar(self):
		query = 'starred = true'
		metadata = {'starred' : 'false'}
		response = self.drive.files().list(q=query, fields='files(id, name, trashed)').execute()
		found = response.get('files')

		if  not response:
			print 'No starred folders/files found'
			return True

		if found:
			for x in range(len(found)):
				if found[x].get('trashed'):
					continue
				try:
					print str(x) + '. ' + found[x].get('name') + ' (' + found[x].get('id') + ')'
				except UnicodeEncodeError:
					print str(x) + '. ' + '[Unknown name]' + ' (' + found[x].get('id') + ')'
			select = raw_input('Select: ')
		else:
			print 'No starred folders/files found'
			return True	

		try:
			select = int(select)
			if select < len(found) and select >= 0:
				starId = found[select].get('id')
				try:
					response = self.drive.files().update(fileId=starId, body=metadata).execute()
					print 'Star removed'
					return True
				except HttpError as err:
					if err.resp.status == 403:
						print 'You are not allowed to move it'
						return False
					else:
						raise

			else:
				print 'Enter a valid number'
				self.RemoveStar()

		except ValueError:
			print 'Error. Enter valid number'
			self.RemoveStar()









