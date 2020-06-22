import requests
import json
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import numpy as np
from PIL import Image

words_dict = {}

#1. 请求数据
url = 'https://api.yimian.xyz/coro'
response = requests.get(url)


#2. 提取数据
json_data = json.loads(response.text)
for p in json_data:
	if 'cities' in p:
		for c in p['cities']:
			words_dict[c['cityName']] = c['confirmedCount']
	else:
		words_dict[p['provinceName']] = p['confirmedCount']



#3. 显示数据
alice_mask = np.array(Image.open('heart.jpg'))

wordcloud = WordCloud(font_path='/Users/zjueman/Library/fonts/HYQuHeiW.ttf', background_color='white', mask=alice_mask)
wordcloud = WordCloud(font_path='/Users/zjueman/Library/fonts/HYQuHeiW.ttf', width=2400, height=1200, background_color='white').generate_from_frequencies(frequencies=words_dict)



plt.figure(dpi=1200)
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")

plt.savefig('coro_love_1200.svg')
#plt.show()