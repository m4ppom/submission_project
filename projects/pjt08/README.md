# README PROJECT08

### 0. 준비과정

```
installed apps에 
설치한 'rest_frameork','drf_yasg', 'movies'를 입력하여 앱을 등록시킨다.
```

마스터 url에 경로를 등록한다.

```
path('api/v1/', include('movies.urls')),
```

### 1. 모델 생성

```
from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=20)

class Movie(models.Model):
    title = models.CharField(max_length=200)
    audience = models.IntegerField()
    poster_url = models.CharField(max_length=200)
    description = models.TextField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

class Review(models.Model):
    content = models.CharField(max_length=200)
    score = models.IntegerField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
```

### 2. serializer.py

폼과 같은 역할을 한다.

```
from rest_framework import serializers
from .models import Genre, Movie, Review

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    content = serializers.CharField(label="Content of Review")
    score = serializers.IntegerField(min_value=1, max_value=5, label='Score')
    class Meta:
        model = Review
        fields = ('content', 'score',)
```

### 3. Views, urls

이전에 해왔던 부분과 같은 소스에 다음을 추가한다.

views

```

# @api_view(['PUT','DELETE'])
@api_view(['PATCH','DELETE'])
def update_or_delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    if request.method == 'PATCH':
        review_serializer = ReviewSerializer(data=request.data, instance=review)
        if review_serializer.is_valid(raise_exception=True):  # NOT VALID => ERROR
            review_serializer.save()
            return Response({'message': '수정되었습니다.'})
    else:
        review.delete()
        return Response({'message': '삭제되었습니다.'})
```

urls에 urlpatterns뒤에 더한다.

```
+ [
    path('docs/', schema_view.with_ui('redoc'), name='api_docs'),
    path('swagger/', schema_view.with_ui('swagger'), name='api_swagger'),
]

```

