# -*- coding: UTF-8 -*-
#!/usr/bin/python3
import os

os.mkdir(
    r"E:\王一涵programThomas\Coding-Notes\Python-Notes\第十五章-文件操作与管理\OS_Module\2.mkdir_rmdir\MKDIR"
)
'''
mkdir:
---
mkdir(path: _PathType, mode: int=..., *, dir_fd: Optional[int]=...) -> None
param path: _PathType
Create a directory.
If dir_fd is not None, it should be a file descriptor open to a directory,
and path should be relative; path will then be relative to that directory.
dir_fd may not be implemented on your platform.
If it is unavailable, using it will raise a NotImplementedError.
The mode argument is ignored on Windows.
'''

os.rmdir(
    r"E:\王一涵programThomas\Coding-Notes\Python-Notes\第十五章-文件操作与管理\OS_Module\2.mkdir_rmdir\MKDIR"
)
'''
rmdir:
---
rmdir(path: _PathType, *, dir_fd: Optional[int]=...) -> None
param path: _PathType
Remove a directory.
If dir_fd is not None, it should be a file descriptor open to a directory,
and path should be relative; path will then be relative to that directory.
dir_fd may not be implemented on your platform.
If it is unavailable, using it will raise a NotImplementedError.
'''
