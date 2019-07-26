import csv
import requests


f = open('movie_naver.csv', 'r', encoding='utf-8')
reader = csv.reader(f)
next(reader, None)
for line in reader:
    with open(f'./images/{line[0]}.jpg', 'wb') as f: 
        image = requests.get(line[2], stream=True).content  # 사진담음
        f.write(image)
