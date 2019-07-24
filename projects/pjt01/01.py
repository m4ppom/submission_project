import requests
import datetime
import csv
from decouple import config
from datetime import timedelta, datetime


key = config('API_KEY')
URL = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={key}&weekGb=0&targetDt='
mov_list = []

with open('boxoffice.csv', 'w', encoding='utf-8', newline='') as f:
    fieldnames = ['Movie_code', 'Movie_Name', '관객수']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for i in range(0, 50, 1):
        date1 = datetime(2019, 7, 12) - timedelta(weeks=i)
        date2 = date1.strftime("%Y%m%d")
        data = requests.get(URL+f'{date2}').json()
        result = {}
        for movie in data['boxOfficeResult']['weeklyBoxOfficeList']:
            result = movie.get('movieCd')
            result2 = movie.get('directors')
            if result in mov_list:
                continue
            else:
                writer.writerow({'Movie_code': movie.get('movieCd'), 'Movie_Name': movie.get('movieNm'), '관객수': movie.get('audiCnt')})
                mov_list.append(result)
