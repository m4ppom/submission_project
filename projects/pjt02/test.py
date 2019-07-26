from decouple import config
import requests
import time
import csv



# for i in range(100):
#     time.sleep(0.8)
#     requests.get('naver')

naver_client_id = config('NAVER_CLIENT_ID')
naver_client_secret = config('NAVER_CLIENT_SECRET')


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
    return response.json()  # ['items']['image']
    
send_naver_movie('알라딘')['items'][0]  # ['image']
print(send_naver_movie('알라딘'))

# image_urls = []
# for movie_name in movie_names:
#     image_urls.append(send_naver_movie_img(movie_name))


# dogurl = 'https://d4ougc3s3r7jj.cloudfront.net/images/design-assets/testimonials-dog-taller.png'
# with open(f'test.png', 'wb') as f:
#     image = requests.get(dogurl, stram=True).content  # 사진담음
#     f.write(image)

