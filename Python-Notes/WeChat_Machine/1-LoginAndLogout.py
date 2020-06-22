# author = Wyh
# coding: UTF-8

import itchat

#1登录微信
#自动登录
itchat.login(enableCmdQR=False)


#让微信机器人可以自动运行
#这其实是一个网页版微信，旧版的微信应该支持，很多微信不支持

itchat.run()

#弹出png二维码，扫码，应该是使用QR Code生成的，因为提示语中有，如果登陆成功手机会有显示，运行也会有显示