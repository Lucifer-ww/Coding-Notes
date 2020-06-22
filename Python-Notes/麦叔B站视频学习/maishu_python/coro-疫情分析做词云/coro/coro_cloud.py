import requests
import json
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import numpy as np
from PIL import Image

words_dict = {}

url = 'https://api.yimian.xyz/coro'
response = requests.get(url)
json_data = json.loads(response.text)

for p in json_data:
	if 'cities' in p:
		for c in p['cities']:
			words_dict[c['cityName']] = c['confirmedCount']
	else:
		words_dict[p['provinceName']] = p['confirmedCount']

alice_mask = np.array(Image.open('heart.jpg'))

wordcloud = WordCloud(font_path='/Users/zjueman/Library/fonts/HYQuHeiW.ttf', background_color='white', mask=alice_mask)
#wordcloud = WordCloud(font_path='/Users/zjueman/Library/fonts/HYQuHeiW.ttf', background_color='white')
wordcloud.generate_from_frequencies(frequencies=words_dict)


plt.figure(dpi=1200)
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")

plt.savefig('cloud_cloud.png')
#plt.show()