# -*- coding: UTF-8 -*-
from wordcloud import WordCloud
wc = WordCloud()  # 创建词云对象
wc.generate('hello world! Python is Beautiful! I like it')  # 生成词云
wc.to_file(r'Python10行内的高端操作\view\wordcloud.png')  # 保存词云
