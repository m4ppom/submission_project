import csv
import requests
import time
from decouple import config
import copy
from IPython import embed


def send_naver_movie(movie_name):
    naver_client_id = config('NAVER_CLIENT_ID')
    naver_client_secret = config('NAVER_CLIENT_SECRET')
    BASE_URL = 'https://openapi.naver.com/v1/search/movie.json'
    headers = {
        'X-Naver-Client-Id': naver_client_id,
        'X-Naver-Client-Secret': naver_client_secret
    }
    URL = BASE_URL + '?query=' + movie_name
    response = requests.get(URL, headers=headers)
    return response.json()

f = open('boxoffice.csv', 'r', encoding='utf-8')
movie_pri = {}
movie_info = []
movie_names = {}
movie_naver = {}
movie_pri_list = []
reader = csv.reader(f)
next(reader, None)
for line in reader:
    movie_names['movieCd'] = line[0]
    movie_names['movieNm'] = line[1]
    movie_info.append(copy.copy(movie_names))

with open('movie_naver.csv', 'w', encoding='utf-8', newline='') as f:
    fieldnames = ['code', 'link', 'sum_URL', 'rate']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for movie_name in movie_info:
        time.sleep(0.5)
        movie_naver = send_naver_movie(movie_name['movieNm'])
        print(movie_naver)
        movie_pri['code'] = movie_name['movieCd']
        try:
            movie_pri['link'] = movie_naver.get('items')[0].get('link')
            movie_pri['sum_URL'] = movie_naver.get('items')[0].get('image')
            movie_pri['rate'] = movie_naver.get('items')[0].get('userRating')
            movie_pri_list.append(copy.copy(movie_pri))
        except IndexError:
            embed()
    for i in movie_pri_list:
        writer.writerow(i)

# with open('movie_naver.csv', 'w', encoding='utf-8', newline='') as f:
#     fieldnames = ['대표코드', '링크', '썸네일URL', '유저평점']
#     writer = csv.DictWriter(f, fieldnames=fieldnames)
#     writer.writeheader()
#     for movie_name in movie_names.keys:
#         time.sleep(0.8)
#         send_naver_movie(movie_name)
#         print(movie_name)

# with open('movie_naver.csv', 'w', encoding='utf-8', newline='') as f:
#     fieldnames = ['Movie_code', 'Movie_Name', '관객수']
#     writer = csv.DictWriter(f, fieldnames=fieldnames)
#     writer.writeheader()
#     data = requests.get(URL3+direc).json()



# for i in range(100):
#     time.sleep(0.8)
#     requests.get('naver')

# naver_client_id = config('NAVER_CLIENT_ID')
# naver_client_secret = config('NAVER_CLIENT_SECRET')


# def send_naver_movie(movie_name):
#     naver_client_id = config('NAVER_CLIENT_ID')
#     naver_client_secret = config('NAVER_CLIENT_SECRET')
#     BASE_URL = 'https://openapi.naver.com/v1/search/movie.json'

#     headers = {
#         'X-Naver-Client-Id': naver_client_id,
#         'X-Naver-Client-Secret': naver_client_secret
#     }

#     URL = BASE_URL + '?query=' + movie_name

#     response = requests.get(URL, headers=headers)
#     return response.json()['items']['image']
    
# send_naver_movie('알라딘')['items'][0]['image']
# print(send_naver_movie('알라딘'))

# image_urls = []
# for movie_name in movie_names:
#     image_urls.append(send_naver_movie_img(movie_name))


# dogurl = 'https://d4ougc3s3r7jj.cloudfront.net/images/design-assets/testimonials-dog-taller.png'
# with open(f'./images/{moptest.png', 'wb') as f:
#     image = requests.get(dogurl, stram=True).content  # 사진담음
#     f.write(image)


