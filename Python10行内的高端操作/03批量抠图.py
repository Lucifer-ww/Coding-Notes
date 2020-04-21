# -*- coding: UTF-8 -*-
#!/usr/bin/python3

import os, paddlehub as hub
humanseg = hub.Module(name='deeplabv3p_xception65_humanseg')		# 加载模型
path = "E:\王一涵programThomas\王一涵PythonThomas\Python-Learned\Python10行内的高端操作\IMG\笔.png"	# 文件目录
files = [path + i for i in os.listdir(path)]	# 获取文件列表
results = humanseg.segmentation(data={'image':files})	# 抠图