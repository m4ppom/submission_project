import requests
from decouple import config
import datetime
from datetime import timedelta, datetime
import csv

key = config('API_KEY')
# movieCd  movieNm  audiCnt
URL = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={key}&weekGb=0&targetDt='
# mov_list = []
mov_list = []
with open('boxoffice.csv', 'w', encoding='utf-8', newline='') as f:
    fieldnames = ['Movie_code', 'Movie_Name', '관객수']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for i in range(0, 51, 1):
        date1 = datetime(2019, 7, 12) - timedelta(weeks=i)
        date2 = date1.strftime("%Y%m%d")
        data = requests.get(URL+f'{date2}').json()
        result = {}
        for movie in data['boxOfficeResult']['weeklyBoxOfficeList']:
            result = movie.get('movieNm')
            if result in mov_list:
                continue
            else:
                writer.writerow({'Movie_code': movie.get('movieCd'), 'Movie_Name': movie.get('movieNm'), '관객수': movie.get('audiCnt')})
                mov_list.append(result)
