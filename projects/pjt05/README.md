## PJT05

```
$ pip install django django_extensions
$ django-admin startproject pjt05 .
$ django-admin startapp cinema
$ mkdir -p cinema/templates/cinema
$ touch cinema/urls.py cinema/forms.py
$ cd cinema/templates/cinema/
$ touch movie_list.html movie_detail.html new_movie.html update_movie.html base.html _form.html
```

* django를 사용하기 위한 기본 과정

```python
from django.db import models
from django.urls import reverse

class Movie(models.Model):
    title = models.CharField(max_length=200)
    title_en = models.CharField(max_length=200)
    audience = models.IntegerField()
    open_date = models.DateField()
    genre = models.CharField(max_length=20)
    watch_grade = models.CharField(max_length=20)
    score = models.FloatField()
    poster_url = models.TextField()
    description = models.TextField()
    def get_absolute_url(self):
        return reverse("cinema:movie_detail", kwargs={"movie_id": self.id})
```

```
$ python manage.py makemigrations cinema
$ python manage.py migrate cinema
```

* 모델 생성

- models.py에서 class를 setting한 후 cinema에 migrate한다.

- reverse를 이용해서 url로 만들어 주는 함수를 생성한다.

- url 들을 연결하기 위해 urlpatterns에 입력한다.



![1570786134764](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1570786134764.png)

* 요청이 들어오면 해당 html로 보내준다.

![1570786243560](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1570786243560.png)

![1570786257342](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1570786257342.png)

* @require을 통해 GET이나 POST형식으로 오는 신호만 받을 수 있다.

* MovieModelForm을 사용하여 데이터가 제대로 들어왔는지 검증한다.

* update할 때 이전에 저장되었던 내용을 그대로 가져오기 위해 (instance=movie) 를 사용해 지정한다.



![1570786418279](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1570786418279.png)

* forms.py에서 forms.ModelForm을 사용해 데이터를 한번에 편하게 받을 수 있도록한다.

![1570786522033](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1570786522033.png)

* movie_list.html에서 model에서 선언한 absolute_url을 사용해 링크를 생성한다.

* {{ }}를 사용해 title, score를 받아와서 출력한다.

```html
<h3>{{ movie.title }}, {{ movie.title_en }}</h3>
    <p>관객수 : {{ movie.audience|intcomma }}</p>
    <p>개봉일 : {{ movie.open_date }}</p>
    <p>장르 : {{ movie.genre }}</p>
    <p>관람등급 : {{ movie.watch_grade }}</p>
    <p>평점 : {{ movie.score }}</p>
    <img src="{{ movie.poster_url }}" alt="image" width="200">
    <div>{{ movie.description }}</div>
    <br>
    <div>
        <div class="ui-button">
            <a href="{% url 'cinema:movie_list'%}">
                <button>목록</button>
            </a>
        </div>
        <div class="ui-button">
            <a href="{% url 'cinema:update_movie' movie.id %}">
                <button>수정</button>
            </a>
        </div>
        <div class="ui-button">
            <form action="{% url 'cinema:delete_movie' movie.id %}" method="POST">
                {% csrf_token %}
                <input onclick="return confirm('영화 정보가 삭제.')" type="submit" value="삭제">
            </form>
        </div>
    </div>
```

* movie_detail.html에서 영화 상세 정보를 표현한다 

```
{% include 'cinema/_form.html' %} <- update_movie.html과 new_movie.html에 사용하여 _form.html의 값을 불러온다.

```

* _form.html

  ``` django
  <form method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit">
  </form>
  ```

  위에서 사용하기 위해 _form을  설정한다.

  .as_p를 사용하여 폭을 조절한다.