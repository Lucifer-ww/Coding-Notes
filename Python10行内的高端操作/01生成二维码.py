#coding: UTF-8
from MyQR import myqr
myqr.run(
    words='https://blog.csdn.net/cool99781',	# 包含信息
    picture='Python10行内的高端操作/IMG/git.png',			# 背景图片
    colorized=True,			# 是否有颜色，如果为False则为黑白
    save_name='Python10行内的高端操作/view/blogc1.png'  # 输出文件名
)
