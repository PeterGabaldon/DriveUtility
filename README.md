# Google Drive Utility
## What is Google Drive Utility?
Google Drive Utility provides an easy way to use Google Drive from command line, tasks such as uploading files/folders, downloading them, moving folders/files. Additionally, using the provided .reg files it can be added to the Windows Context Menu, giving the opportunity of using it anywhere in an very easy and friendly way. It is written in Python 2.7. It is licensed under the MIT license, see LICENSE.

# Installation
## Download and installation
You can download it with Pip:
```
pip install DriveUtility
```

# Usage
## Command line utility
Usage:
```
DriveUtil [Args]
```
or:
```
python -m DriveUtil [Args]
```
Available options are:
```
  -h, --help            show this help message and exit
  -u, --upload Path(s) [Path(s) ...]
                        Path of folder or file to upload.
  -s, --specificf Path(s) [Path(s) ...]
                        Path of folder or file to upload to a specific folder.
  -cr, --createf        Creates a folder.
  -re, --remove         Remove access to Drive.
  -l, --list            List Drive files and folders.
  -d, --delete          Delete selected file or folder.
  -g, --get [Path]      Download file or folder. Optionally, you can specify a
                        path to downlaod there.
  -m, --move            Move file or folder.
  -cb, --clean          Clean bin.
  -co, --copy           Copy a file.
  -se, --search         Search by name.
  -aS, --addS           Star a file.
  -rS, --removeS        Remove star from an starred file.
  -sL, --shareLink      Enable share linking and get the share link.
```
## Implementing it
Module `main.py` holds two functions, `Auth()` and `DeleteCred()` and the `main`class. The first one return the Drive API object after a successfully Oauth autentication, and the second remove the Oauth stored token. The `drive.py` module import `main.py` and imlements the `Drive` class wich inherits from `main` class. Botch classes instantiation need the Drive API object parameter.

Methods:

Method |Param 1|Param 2|Param 3|Param 4|Return              
-------|-------|-------|-------|-------|------
Upload |path|FolderId=None|||True if successful. False if not
UploadSpecificFolder|path|Id=None|||True if successful. False if not
CreateFolder|||||Id of the newly created folder
Download|path=None|Id=None|||True if successful. False if it fails
Copy|Id=None||||True if successful. False if it fails
SearchByName|||||           
Delete|Id=None||||True if successful. False if it fails
List |FolderId=None|OnlyFolder=False|SelectId=False|query=None |Folder/file Id if SelectId=True. None otherwise
Move|moveId|moveToId|||True if successful. False if it fails
AddStar|Id||||True if successful. False if it fails
RemoveStar|||||True if successful. False if it fails
getShareLink|||||Share link. False if it fails

# Windows Context Menu
## Adding it
The provided python scripts, `addContext.py` and `removeContext.py` add new options to the Context Menu, making DriveUtil more flexible to use. These two scripts must be run with admin rights. You can use:
```
python -m DriveUtil.addContext
```
and
```
python -m DriveUtil.removeContext
```
from an elevetad Windows command prompt.

![Context Menu](https://media.giphy.com/media/4K1N65N9Wmx6WrdQ4f/giphy.gif)

## Examples
`example.py` is a sample script. It will upload the contents of Test folder.

# Contributing
All pull requests and issues are welcome. I'm very thankful for any type of help, improvement or tests.



