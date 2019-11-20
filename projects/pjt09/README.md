# Project 09

## Vue.js 개발 프로세스를 통한 영화 목록 페이지 구현



### 1. 컴포넌트 구조

![1574234952052](C:\Users\student\submission\projects\pjt09\img\1574234952052.png)

```
App.vue -> MovieList.vue -> MovieListItem.vue -> MovieListModal.vue
위의 순서로 정보를 보내고 받는다.
App.vue에서 활용할 데이터를 정의하고 components에 Movielist에 등록하여 사용한다.
```

### App.vue

```vue
<script>
    const axios = require('axios');
    import MovieList from './components/movies/MovieList';
    const HOST = "http://localhost:3000/"
    export default {
      name: 'app',
      components: {
        MovieList,
      },
      data() {
        return {
          movies: [],
          genres: [],
        }
      },
      mounted() {
        axios.get(HOST + 'movies')
          .then(res => this.movies = res.data)
        axios.get(HOST + 'genres')
          .then(res => this.genres = res.data)
      },
    }
</script>
```



```
MovieList.vue에서 장르 선택 옵션을 만들어주고 전체 영화를 보여주는 옵션을 만들어 출력되게 변경해준다.
```

### MovieList.vue

```vue
<select class="form-control" v-model="selectedGenreId">
     <option value="all">All</option>
     <option v-for="genre in genres" :key="genre.id" :value="genre.id">
       {{genre.name}}
     </option>
</select>
```

```
옵션에 선택된 장르만 보여주기 위해 조건을 걸어준다.
```

```vue
<div class="row" >
      <!-- <v-if="{{genre.name}} === 'movie.genre'" > -->
        <MovieListItem
         v-for="movie in movies"
         :key ="movie.id"
         :movie ="movie"
         v-show ="selectedGenreId === movie.genre_id || !selectedGenreId  "
       />
       <MovieListItem
         v-for="movie in movies"
         :key ="movie.id"
         :movie ="movie"
         v-show ="selectedGenreId === 'all'  "
       />
</div>
```



### MovieListModal.vue

```
버튼 클릭시 내용이 나오도록 설정해준다.
```

```vue
<template>
  <div class="col-3 my-3">
    <img class="movie--poster my-3" :src="movie.poster_url" :alt="movie.name">
    <button class="btn btn-primary" data-toggle="modal" :data-target="`#movie-${movie.id}`">{{ movie.name }}</button>
      <MovieListItemModal :movie="movie" />
  </div>
</template>
<script>
import MovieListItemModal from './MovieListItemModal';
export default {
  name: 'MovieListItem',
  components: {
    MovieListItemModal,
  },
  props: {
    movie: Object,
    genre: Object,
  },

  data () {
    return {
    }
  }
}
</script>
```

```
버튼에 영화 이름을 넣어주면서 H3에 쓴 영화제목 부분을 삭제하였다.
```



### 화면

* 코미디를 선택했을 때.

  ![1574235650103](C:\Users\student\submission\projects\pjt09\img\1574235650103.png)

* 전체를 선택했을 때.

![1574235683300](C:\Users\student\submission\projects\pjt09\img\1574235683300.png)



```
조건을 두번돌려서 all이 선택되었을때 나올 수 있도록 했다.
```

