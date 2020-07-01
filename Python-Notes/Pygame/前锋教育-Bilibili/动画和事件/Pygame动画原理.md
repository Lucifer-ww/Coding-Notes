# Pygame动画原理

这是动画原理的第一节，首先需要游戏的最小系统，在此之后我就不再提游戏最小系统了，那是最基本的，可以看我的第一篇

所有代码、配套资源、讲解都在[Github Coding-Notes](https://github.com/Github-Programer/Coding-Notes/tree/master/Python-Notes/Pygame/%E5%89%8D%E9%94%8B%E6%95%99%E8%82%B2-Bilibili)帮助更多的人，还有Python其他资源，以及C++。

--课程--

# 移动

Pygame移动就是帧动画，每一帧将移动对象向一个方向移动，移动速度足够快就可以形成动画，下面是PPT模拟。

![](E:\ProgramThomas\Coding-Notes\Python-Notes\Pygame\前锋教育-Bilibili\动画和事件\2020年6月26日15-20-48.gif)

这就是移动的原理，对象也可以向任何方向移动，这就是动画原理

刚才PPT的球对应的每一个页面就是一帧，将图片连接起来称为视频，一般视频再12帧以上才能说是流畅的，一般的视频都是24帧动画，否则太低无法流畅，看到的就是卡的，今天这一讲没什么难的，就是原理，顺便玩玩Scratch，体验一下帧动画

![](E:\ProgramThomas\Coding-Notes\Python-Notes\Pygame\前锋教育-Bilibili\动画和事件\逐帧动画-Scratch高帧率.gif)

这是较快的帧率，看这速度，那么每一次切换等待一秒，就是1秒的帧动画，太慢了

![](E:\ProgramThomas\Coding-Notes\Python-Notes\Pygame\前锋教育-Bilibili\动画和事件\逐帧动画-Scratch低帧率.gif)

最后说一个软件叫做：ScreenToGIF，很好用，可以录制一个Gif，还可以打开一个现有的GIF，并拆分出每一帧，这不是最重量的GIF工具，但是很强大而且轻便，还能添加字幕