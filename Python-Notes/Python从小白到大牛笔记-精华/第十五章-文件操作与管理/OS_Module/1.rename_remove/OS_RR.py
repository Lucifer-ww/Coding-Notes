# -*-coding: UTF-8 -*-
#!/usr/bin/python3
import os

os.rename(r"E:\王一涵programThomas\Coding-Notes\Python-Notes\第十五章-文件操作与管理\OS_Module\1.rename_remove\test.txt",
          r"E:\王一涵programThomas\Coding-Notes\Python-Notes\第十五章-文件操作与管理\OS_Module\1.rename_remove\last.txt")
'''
rename文档：
---
rename(src: _PathType, dst: _PathType, *, src_dir_fd: Optional[int]=..., dst_dir_fd: Optional[int]=...) -> None
param src: _PathType

Rename a file or directory.
If either src_dir_fd or dst_dir_fd is not None, it should be a file
descriptor open to a directory, and the respective path string (src or dst)
should be relative; the path will then be relative to that directory.
src_dir_fd and dst_dir_fd, may not be implemented on your platform.
If they are unavailable, using them will raise a NotImplementedError.
'''

os.remove(r'E:\王一涵programThomas\Coding-Notes\Python-Notes\第十五章-文件操作与管理\OS_Module\1.rename_remove\removeTEST.TXT')
'''
remove文档：
---
remove(path: _PathType, *, dir_fd: Optional[int]=...) -> None
param path: _PathType

Remove a file (same as unlink()).
If dir_fd is not None, it should be a file descriptor open to a directory,
and path should be relative; path will then be relative to that directory.
dir_fd may not be implemented on your platform.
If it is unavailable, using it will raise a NotImplementedError.
'''
