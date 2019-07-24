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
