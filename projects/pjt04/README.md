# Proroject 04 반응형 웹 사이트 구성

## Navigation Bar

bootstrap에서  받은 navigation을 넣고 Item 리스트를 우측정렬한다.

```html
<nav class="navbar sticky-top navbar-expand-lg navbar-light bg-light">
        <a class="navbar-brand" href="#">영화추천사이트</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav"
            aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav ml-auto">
                <li class="nav-item active">
                    <a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#" aria-disabled="true">친구평점보러가기</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#" aria-disabled="true">Login</a>
                </li>
            </ul>
        </div>
    </nav>
```

폭이 좁아지면 Item list가 사라지도록 변경한다.



## Header

헤더를 navigatrion아래 위치하고  중앙에 글을 이 위치하도록 세부 사항을 설정한다.

```html
header {
    height: 350px;
    text-align: center;
    background: url(images/banner2.JPG);
    -webkit-background-size: cover;
    -moz-background-size: cover;
    -o-background-size: cover;
    background-size: 100% 100%;
}
header>h2 {
    text-align: center;
    width: 100%;
    position: absolute;
    float: center;
    top: 25%;
    color: rgb(62, 19, 214);
}
```

## Footer

html문서에 선언되어있는 footer의 설정을 조정하기 위해 css에 다음과 같이 내용을 넣었다.

```css
footer {
    position: fixed;
    bottom: 0;
    float left;
    line-height: 50px;
    padding: 3rem;
    background-color: #123456;
    color: blue;
    width: 100%;
}
```

