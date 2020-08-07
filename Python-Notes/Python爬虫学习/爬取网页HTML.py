# coding: utf-8
from requests import get

# res = get("https://c.runoob.com/front-end/55")
# res.encoding="UTF-8"
# fh = open("Runoob_55-rgbhex.html", 'r+', encoding="UTF-8")
# fh.writelines(res.text)

res = get("https://live.youdao.com/live/index.html?courseId=61251&lesson=3107990&type=1")

fh = open("状语从句[LJYY].html", 'r+', encoding="utf-8")
fh.writelines(res.text)