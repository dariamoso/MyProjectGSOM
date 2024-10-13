#Get requests
#Task1

import requests
import re
import os

gsom = 'https://gsom.spbu.ru/en/'
r = requests.get(gsom)

content = r.text
png_num = content.count('.png')
print("Number of .png: ",png_num)

#Task2

png_find = content.find('.png')

first = content.rfind('"', 0, png_find) + 1
last = png_find + 4
png_path = content[first:last]
png_link = f"https://gsom.spbu.ru{png_path}"

image = requests.get(png_link)

f = os.path.basename(png_path)
img = open(f, 'wb')
img.write(image.content)
img.close()
print("Image has been saved!!")