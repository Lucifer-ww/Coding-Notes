import requests
import json

#1. 请求数据
url = 'https://api.yimian.xyz/coro'
data = requests.get(url).text

#2. 解析数据 - 转换成JSON对象
city_dict = {}
json_data = json.loads(data)
for p in json_data:
	if 'cities' in p:
		for c in p['cities']:
			cityName = c['cityName']
			cCount = c['confirmedCount']
			sCount = c['suspectedCount']
			total = int(cCount) + int(sCount)
			city_dict[cityName] = total
	else:
		cityName = p['provinceName']
		cCount = p['confirmedCount']
		sCount = p['suspectedCount']
		total = int(cCount) + int(sCount)
		city_dict[cityName] = total

#3. 写入文件
with open('city_count.txt', 'w') as f:
	for k, v in city_dict.items():
		f.write(f"{k}:{v}\n")

#4. 生成词云
import wordcloud #生成词云的模块
import matplotlib.pyplot as plt 

# ccloud = wordcloud.WordCloud(background_color='white', width=1600, height=800, font_path='/Users/zjueman/Library/fonts/HYQuHeiW.ttf')
# ccloud.generate_from_frequencies(frequencies=city_dict)

# plt.figure()
# plt.imshow(ccloud, interpolation='bilinear')
# plt.axis('off')
# plt.show()

#5. 生成爱心词云，并存图片
import numpy as np
import PIL

heart_mask = np.array(PIL.Image.open('heart.jpg'))
ccloud = wordcloud.WordCloud(background_color='white', mask=heart_mask, font_path='/Users/zjueman/Library/fonts/HYQuHeiW.ttf')
ccloud.generate_from_frequencies(frequencies=city_dict)

plt.figure(dpi=1200) #dpi指定图片清晰度
plt.imshow(ccloud, interpolation='bilinear')
plt.axis('off')
plt.savefig('heart.png') #保存文件
#plt.show()









