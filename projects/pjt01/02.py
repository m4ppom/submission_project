import copy
movie_info = {}
movie_info_list = []
movie_director_list = []

URL2 = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key={key}&movieCd='
with open('movie.csv', 'w', encoding='utf-8', newline='') as f:
        fieldnames = [
            'movieNm',
            'movieNmEn',
            'movieNmOg',
            'watchGradeNm', 
            'openDt',
            'showTm', 
            'genreNm', 
            'peopleNm'
        ]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

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
        for i in movie_info_list:
            writer.writerow(i)
            