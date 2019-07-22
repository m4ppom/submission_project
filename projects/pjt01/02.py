import requests
from decouple import config
import datetime
from datetime import timedelta, datetime
import csv

# http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key=430156241533f1d058c603178cc3ca0e&movieCd=20124079

key = config('API_KEY')
URL = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={key}&weekGb=0&targetDt='

mov_list = []
with open('movie.csv', 'w', encoding='utf-8', newline='') as f:
    fieldnames = ['대표코드', '영화명(국문)', '영화명(영문)', '영화명(원문)', '관람등급', '개봉연도', '상영시간', '장르', '감독명']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for i in range(0, 50, 1):
        date1 = datetime(2019, 7, 12) - timedelta(weeks=i)
        date2 = date1.strftime("%Y%m%d")
        data = requests.get(URL+f'{date2}').json()
        result = {}
        for movie in data['boxOfficeResult']['weeklyBoxOfficeList']:
            result = movie.get('movieNm')
            if result in mov_list:
                continue
            else:
                mov_list.append(result)
                URL2 = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key={key}&movieCd='
                data3 = requests.get(URL2+movie.get('movieCd')).json()
                movie2 = data3['movieInfoResult']['movieInfo']
                for movieNm in mov_list:
                    if movieNm == movie2.get('movieNm'):
                        writer.writerow({
                            '대표코드': movie2.get('movieCd'),
                            '영화명(국문)': movie2.get('movieNm'),
                            '영화명(영문)': movie2.get('movieNmEn'),
                            '영화명(원문)': movie2.get('movieNmOg'),
                            '관람등급': movie2.get('watchGradeNm'),
                            '개봉연도': movie2.get('openDt'),
                            '상영시간': movie2.get('showTm'),
                            '장르': movie2.get('genreNm'),
                            '감독명': movie2.get('directors')
                        })
