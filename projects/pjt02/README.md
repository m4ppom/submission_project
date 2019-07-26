# Project 2

## 1. 네이버 영화 검색 API 

![1564117947234](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1564117947234.png)

import csv = 파일을 읽고 저장하기 위해 사용.

import requests = 정보를 받아오기 위해 사용.

import time = 데이터를 받아오는데 지연시간을 두어 사고를 방지한다.

import config = decouple을 사용하여 개인정보를 보호하기 위해 사용한다.

import copy = 복사를 수행하기 위해 사용

import embed = 디버깅을 하기위해 사용.

![1564118151955](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1564118151955.png)

영화명을 넣으면 해당 정보를 리턴하는 함수를 만든다.

![1564118294695](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1564118294695.png)

boxoffice에서 영화코드와 영화이름을 받아서 리스트로 저장한다.

movie_naver.csv 데이터를 저장하기 위해 탭을 설정한다.

빈movie_pri 딕셔너리에 원하는 내용을 넣고 movie_pri_list에 저장한다.

movie_pri_list 한 행씩 저장한다.







## 2.영화 포스터 이미지 저장

![1564118669493](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1564118669493.png)

movie_naver.csv에서 내용을 reader을 사용해서 읽는다.

읽은  내용을 image파일에 저장한다.



## 3. 느낀점

디버깅의 중요성과 다른 사람과 코드를 공유하여 문제를 발견하는 것의 장점을 알 수 있었다.

project1과 같이 리스트와 딕셔너리를 처리하는 방법에 대해 생각해볼 수 있었다.