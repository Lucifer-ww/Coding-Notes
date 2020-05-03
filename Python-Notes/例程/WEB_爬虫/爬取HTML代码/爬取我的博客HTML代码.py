import urllib.request

url = 'https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=osari_pc_1'
req = urllib.request.Request(url)

f = open(r"E:\王一涵programThomas\Coding-Notes\Python-Notes\例程\WEB_爬虫\爬取HTML代码\hcode.html", 'w+', encoding="UTF-8")
with urllib.request.urlopen(req) as response:
	data = response.read()
	htmlstr = data.decode()
	f.write(htmlstr)
