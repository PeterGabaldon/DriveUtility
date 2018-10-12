#! /usr/bin/env python
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
drive.py - Contain other Google Drive operations

Example:
    
    import drive
    
    cred = drive.Auth()
    drive = drive.Drive(cred)

    drive.Move()
    drive.AddStar("example.txt")

"""

from main import *


class Drive(mainDrive):
    """
    This class inherits from Drive class and hold other Google Drive operations.
    Constructor parameters:
        -drive: Drive api object
    """
    def __init__(self, drive):
        super(Drive, self).__init__(drive)
            
    def Move(self, moveId=None, moveToId=None):
        """
        Move a file/folder.
        Return:
            -True if successful
            -False if it fails
        """
        self.moveId = moveId
        self.moveToId = moveToId

        print 'Select wich file/folder move: '

        if not self.moveId:
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

            if not self.moveToId:
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

    def AddStar(self, Id=None):
        """
        This method will add a star to the selected folder/file.
        Return:
            -True if successful
            -False if it fails
        """
        self.Id = Id

        metadata = {'starred' : 'true'}
        print 'Selec file/folder to add star: '

        if not self.Id:
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
            
    def RemoveStar(self):
        """
        This method will remove the star of the selected folder/file.
        Return:
            -True if successful
            -False if it fails
        """
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
                
    def GetShareLink(self, Id=None):
        """
        This method will get the share link, enabling link sharing of the selected folder/file.
        Parameters:
            -Id: Id of folder/file to enable sharing with anyone
        Return:
            -Link
            -False if it fails
        """
        self.Id = Id
        permission = {'role' : 'reader', 'type' : 'anyone', 'allowFileDiscovery' : 'false'}

        if not self.Id:
            self.Id = super(Drive, self).List(SelectId=True)

        try:    
            response = self.drive.permissions().create(fileId=self.Id, body=permission).execute()
            link = self.drive.files().get(fileId=self.Id, fields='webViewLink').execute().get('webViewLink')
            print 'Link: ' + link
            return link
        except HttpError as err:
            if err.resp.status == 403:
                print 'You are not allowed to share it'
                return False
            else:
                raise

    def DisableSharing(self, Id=None):
        '''
        This method will disable link sharing in the select link-shared item.
        Parameters:
            -Id: Id of folder/file to delete sharing
        Return:
            -True if successful
            -False if it fails
        '''
        self.Id = Id

        print 'Link sharing enabled items:'
        try:
            response = self.drive.files().list(q='', fields='files(id, shared, trashed, name, ownedByMe)').execute()
            files = response.get('files')
            for x in range(len(files)):
                if files[x].get('trashed'):
                    continue

                if (files[x].get('shared')) and (files[x].get('ownedByMe')):
                    if not Id:
                        self.Id = files[x].get('id')
                    permissionIds = self.drive.files().get(fileId=self.Id, fields='permissionIds').execute().get('permissionIds')
                    name = files[x].get('name')

                    for permission in permissionIds:
                        if permission == 'anyoneWithLink':
                            found = True
                            try:
                                print str(x) + '. ' + name + ' (' + files[x].get('id') + ')'
                            except UnicodeEncodeError:
                                print str(x) + '. ' + '[Unknown name]' + ' (' + files[x].get('id') + ')'
                else:
                    continue                
            if 'found' in locals():
                select  = raw_input('Select: ')
            else:
                print 'No link-shared files/folders found'
                return True
            try:
                select = int(select)
                if select < len(files) and select >= 0:
                    sharedId = files[select].get('id')
            except ValueError:
                print 'Error. Enter valid number'
                self.DisableSharing(Id=self.Id)    

            try:
                response = self.drive.permissions().delete(fileId=sharedId, permissionId='anyoneWithLink').execute()
                print 'Link sharing deleted'
                return True
            except HttpError as err:
                if err.resp.status == 403:
                    print 'You do not have permissions'
                    return False
                else:
                    print 'Error deleting sharing permissions'
                    raise
        except HttpError as err:
            if err.resp.status == 404:
                print 'No files/folders found'
                return True
            else:
                print 'Error getting shared files'
                raise
            
    def Rename(self, Id=None, newName=None):
        '''
        This method will rename the selected item or the one of the Id provided.
        Parameters:
            -Id: Id of folder/file to rename
            -newName: New name of the item
        Return:
            -True if successful
            -False if it fails
        '''
        self.Id = Id
        self.name = newName

        if not self.Id:
            print 'Select item to rename: '
            self.Id = super(Drive, self).List(SelectId=True)
        if not self.name:
            self.name = raw_input('New name: ')

        oldName = self.drive.files().get(fileId=self.Id, fields='name').execute().get('name')
        oldName, ext = os.path.splitext(oldName)
        print oldName + ext + ' --> ' + self.name + ext    
        metadata = {'name' : self.name + ext}
        try:
            response =     self.drive.files().update(fileId=self.Id, body=metadata).execute()
            print 'Renamed'
            return True
        except HttpError as err:
            if err.resp.status == 403:
                print 'You do not have permissions'
                return False
            else:
                print 'Error renaming'
                raise




