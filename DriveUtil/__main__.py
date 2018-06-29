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

if __name__ == '__main__':
	try:
		import argparse
		import platform
		import banner
		from drive import *
	except ImportError:
		raise ImportError('Error importing')

	if platform.system() == "Windows":
		codec = 'windows-1252'	
	else:
		codec = 'utf-8'

	parse = argparse.ArgumentParser(description='Google Drive Utility')	
	parse.add_argument('-u, --upload', dest='upload', type=str, nargs='+', help='Path of folder or file to upload.', metavar='Path(s)')
	parse.add_argument('-s, --specificf', dest='specificf', type=str, nargs='+', help='Path of folder or file to upload to a specific folder.', metavar='Path(s)')
	parse.add_argument('-c, --createf', dest='createf', help='Creates a folder.', action='store_true')
	parse.add_argument('-r, --remove', dest='remove', help='Remove access to Drive.', action='store_true')
	parse.add_argument('-l, --list', dest='list', help='List Drive files and folders.', action='store_true')
	parse.add_argument('-d, --delete', dest='delete', help='Delete selected file or folder.', action='store_true')
	parse.add_argument('-g, --get', dest='get', help='Download file or folder. Optionally, you can specify a path to downlaod there.', type=str, nargs='?', const='', metavar='Path')
	parse.add_argument('-m, --move', dest='move', help='Move file or folder.', action='store_true')


	args = parse.parse_args()

	print banner.banner

	if args.remove:
		DeleteCred()
	else:
		cred = Auth()
		if cred:
			drive = Drive(cred)
			if args.specificf:
				for path in args.specificf:
					drive.UploadSpecificFolder(path.decode(codec))
			elif args.createf:
				drive.CreateFolder()
			elif args.upload:
				for path in args.upload:
					drive.Upload(path.decode(codec))
			elif args.list:
				drive.List()
			elif args.delete:
				drive.Delete()
			elif args.get == '':
				drive.Download(path=None)
			elif args.get:
				drive.Download(path=args.get.decode(codec))
			elif args.move:
				drive.Move()				
			else:
				print 'Use -h or --help to see the valid arguments'

		else:
			print 'Please make sure you have allowed the app to acces your Drive'