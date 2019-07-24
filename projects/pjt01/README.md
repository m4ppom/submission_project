# Project 01 데이터 수집.

### 1) 목적

영화진흥위원회 오픈 API를 이용해 프로잭트 요구사항을 충족시킨다.

### 요구1

주간(월~일)까지 기간의 데이터를 조회합니다.

조회 기간은 총 50주이며, 기준일(마지막 일자)은 2019년 7월 13일입니다.

다양성 영화/상업 영화를 모두 포함하여야 합니다.

한국/외국 영화를 모두 포함하여야 합니다.

모든 상영지역을 포함하여야 합니다.

```python
import requests
import datetime
import csv
from decouple import config
from datetime import timedelta, datetime
```

requests를 사용하여 데이터를 받아오기 위해 requests를 import시킨다.

datetime은 날짜 정보를 가져오고 원하는 데이터를 조회하기 위해 사용.

csv는 얻은 데이터를 csv파일로 출력하여 내보내기 위해 사용

config함수를 사용하여 .env파일에서 API정보를 불러오기 위해 decouple을 import시킨다.

```python
key = config('API_KEY')
URL = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={key}&weekGb=0&targetDt='

for i in range(0, 50, 1):
        date1 = datetime(2019, 7, 12) - timedelta(weeks=i)
        date2 = date1.strftime("%Y%m%d")
        data = requests.get(URL+f'{date2}').json()
```

URL에 API키와 날짜 정보를 넣어 원하는 데이터 정보에 접속한다.



```python
with open('boxoffice.csv', 'w', encoding='utf-8', newline='') as f:
    fieldnames = ['Movie_code', 'Movie_Name', '관객수']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
```

데이터를 저장할 csv파일을 생성하고 데이터가 저장될 필드명을 설정해준다.

```python
result = movie.get('movieCd')

writer.writerow({'Movie_code': movie.get('movieCd'), 'Movie_Name': movie.get('movieNm'), '관객수': movie.get('audiCnt')})
```

데이터를 받아 저장하고 writer.writerow를 사용하여 한 행씩 csv파일에 작성한다. 

실행시, 다음과 같이 파일이 생성된다.

![1563959882034](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1563959882034.png)



### 요구2

영화별로 다음과 같은 내용을 저장합니다.
영화 대표코드 , 영화명(국문) , 영화명(영문) , 영화명(원문) , 관람등급 , 개봉연도 , 상영시간 , 장
르 , 감독명
해당 결과를 movie.csv에 저장합니다.

```python
for movie_code in mov_list:
            information = requests.get(URL2+movie_code).json().get('movieInfoResult').get('movieInfo')   
            movie_info['movieNm'] = information.get('movieNm')
            movie_info['movieNmEn'] = information.get('movieNmEn')
            movie_info['movieNmOg'] = information.get('movieNmOg')
            if information['audits']:
                movie_info['watchGradeNm'] = information.get('audits')[0].get('watchGradeNm')
            movie_info['openDt'] = information.get('openDt')
            movie_info['showTm'] = information.get('showTm')
            movie_info['genreNm'] = information.get('genres')[0].get('genreNm')
            if information['directors']:
                movie_info['peopleNm'] = information.get('directors')[0].get('peopleNm')
                movie_director_list.append(copy.copy(movie_info['peopleNm']))
            movie_info_list.append(copy.copy(movie_info))
```

데이터를 받아오는 방법은 위의 1번과 같다.

2번에서 원하는 데이터를 저장하는데 항목 중 데이터가 없고 중복인 부분이 있어서 중복을 제거하기 위해 if문을 사용해 처리를 했다.

copy를 사용하기 위해 import copy를 했다.

![1563960158939](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1563960158939.png)



### 요구3

요청 조건
영화인명 으로 조회합니다.
결과
영화인별로 다음과 같은 내용을 저장합니다.
영화인 코드 , 영화인명 , 분야 , 필모리스트
해당 결과를 director.csv에 저장합니다.  

```python
dir_info = {}
dir_info_list = []
URL3 = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/people/searchPeopleList.json?key={key}&peopleNm='
actor_list = []
with open('director.csv', 'w', encoding='utf-8', newline='') as f:
    fieldnames = ['영화인코드', '영화인명', '분야', '필모리스트']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for direc in movie_director_list:
        data = requests.get(URL3+direc).json()
        result = {}
        for actor in data['peopleListResult']['peopleList']:
            direc = actor.get('peopleNm')

            writer.writerow({
                '영화인코드': actor.get('peopleCd'),
                '영화인명': actor.get('peopleNm'),
                '분야': actor.get('repRoleNm'),
                '필모리스트': actor.get('filmoNames')
            })
       
```

1, 2번에서 데이터를 받아오는 방식과 동일하게 작성하고 출력하면된다.



![1563960250426](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1563960250426.png)





# 느낀점

프로잭트를 수행하면서 리스트와 딕셔너리를 처리하는 방법에 대해 더욱 생각해볼 수 있었다.

API를 통해 데이터를 얻어보면서 이를 활용해 다양한 작업이 가능하다는 것을 알게 되었다.

다른 방법으로 프로잭트를 완성한 것을 보면서 정답이 없음을 느낄 수 있었따.



