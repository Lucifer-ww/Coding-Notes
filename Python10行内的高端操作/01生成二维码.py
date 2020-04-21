#coding: UTF-8
from MyQR import myqr
myqr.run(
    words='http://www.baidu.com',	# 包含信息
    picture='Python10行内的高端操作/IMG/git.png',			# 背景图片
    colorized=True,			# 是否有颜色，如果为False则为黑白
    save_name='Python10行内的高端操作/view/二维码02.png'  # 输出文件名
)
