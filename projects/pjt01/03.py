import requests
from decouple import config
import datetime
from datetime import timedelta, datetime
import csv
# movie2.get('directors')
# http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key=430156241533f1d058c603178cc3ca0e&movieCd=20124079

direc = '미야자키 하야오'
key = config('API_KEY')
URL = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/people/searchPeopleList.json?key={key}&peopleNm={direc}'

actor_list = []
with open('director.csv', 'w', encoding='utf-8', newline='') as f:
    fieldnames = ['영화인코드', '영화인명', '분야', '필모리스트']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    data = requests.get(URL).json()
    result = {}
    for actor in data['peopleListResult']['peopleList']:
        direc = actor.get('peopleNm')
        writer.writerow({
            '영화인코드': actor.get('peopleCd'),
            '영화인명': actor.get('peopleNm'),
            '분야': actor.get('repRoleNm'),
            '필모리스트': actor.get('filmoNames')
        })
