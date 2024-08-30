2024-08-30
- access token 을 cookie 에 저장후 요청할 때마다 전달할 수 있게 설정
- cookie 를 사용하기 위해 - jquery cookie cdn 구글에 검색해서 활용하면 됨 
```https://cdnjs.cloudflare.com/ajax/libs/jquery-cookie/1.4.1/jquery.cookie.min.js```
- 해당 내용을 ```login.html``` 파일에 추가
    - script 로 위 주소 추가
    - 그 이후 ajax 쪽에다가도 추가 하는데 
        결과로 받은 값 중에서 ```$.cookie('access_token', res.access_token);``` access_token 이라는 키로 저장
    - test 하는 방법 : 
        - 개발자 도구 --> application 에서 cookie 를 열어보면 'access_token'값이 잘 들어왔는 지 확인

강의 영상이 아무래도 몇년 전 것이다 보니, flask 버전 등 잘 맞지 않는 부분들이 존재함. 
이것을 어떻게 해결할 것인가...
열심히 GPT와 함께 디버깅을 완료했음
- 코드 순서도 중요함


- 로그인 기능을 설정할 예정
    - TOKEN 을 배울것임 (인증방식) 
    - 토큰기반의 인증방식 / JWT 토큰 방식!
        - JWT = JSON Web Token
            - payload 로 데이터를 넘겨줌 
            - output : three Base64-URL strings separated by dots

    - 기존에는 세션을 활용해서 진행
- 세션 vs. 토큰
    - 토큰 기반 == 클라이언트와 서버 간 연결고리가 아예 없다는 뜻
        - 서버 입장 : 유효한 토큰이 
            - 있으면 로그인 가능
            - 없으면 로그인 불가
        - 클라이언트 입장 : 토큰을 잘 가지고 있고 어떤 요청을 할때마다 전달 (로그인했다는 것을 전달)

- library 가 있음
    - library 설치
     ``` pip install Flask-JWT```
- library가 해주는 일 :
    - 자동으로 인증하기 위한 URL 생성
    - 토큰 생성도 자동으로 생성
    - 토큰에 대한 유효성 검사도 자동으로 진행

- 개발하는 일 :
    - 언제 토큰을 발행할 것인가
        - 사용자가 아이디/비번 을 입력했을 때, 아이디/비번이 DB에 있는 내용과 일치하면 성공 -> 토큰 생성

2024-08-29
- 회원가입은 아래 파트에서 잘 완료했고 
- 로그인 페이지를 작성할건데
    1. login.html 생성
    2. app.py 에 루트 잡아주기
    3. user.py 에 

---------
- jQuery CND 에 들어가서 jQuery 복사! + ```register.html``` 파일에 script 추가
    - <head> 부분에 <script> 를 추가해서 작성하는 것임 
    - 문법 : ```$.ajax ```
    - 언제할 것인가? 
        - 회원가입할 때 버튼을 누를 것임
        - 이때 ajax 요청을 하여 성공이 되었을 때 alert 띄우고 홈으로 보내는 작업
        ㄴ 버튼을 눌렀을 때 ajax 실행 == 함수로 작성
    - 완료되었을 때 콜백을 받을 수 있음 
    
    - 작성이 완료된 후에는 버튼과 연결해야함
    기존 코드
    ```<button type="submit" class="btn btn-primary">등록</button>```
    수정할 내용
    type을 'submit' 일 클릭 할경우, 액션이 넘어감
    type 을 버튼으로 변경, onclick 을 만들고 만든 function 과 연결
    ```<button type="button" class="btn btn-primary" onclick="regist()">등록</button>```
    - 이제 비로소 버튼과 함수가 연결됨

    ----
    - ajax로 이제 데이터도 같이 전송하고 'POST'를 해볼 것임 
    - api 는 폼을 사용하지 않고 json 을 활용함
    - json 형태로 변경해줘야함. 
        - 그래서 form 을 사용하고 있는 부분을 변경해줘야함.

    - API를 만들었음. JSON 으로만 데이터를 주고 받음 
    - 문법하나 - 빨간줄 쳐있을 땐 ```,``` 를 빠뜨렸다거나 등 문제가 있을 수 있음. 
    꼼꼼히 체크 필요 

2024-08-28

b79104c57903d9464c349478955a56a9588b5a19
- 이제 회원 정보 관련 CRUD 전체를 다룰 것임
    - /api/v1/users 까지 등록이 되었더라면 이제는
    - /api/v1/users/<uid> 형태로 하나씩 꺼내서 확인, 수정, 삭제 등 하는 것을 해볼 것임 
- user는 object (class 변수임) => serialize 해줘야함 
- method 가 delete 일 경우, 성공했다는 200 메시지를 주는데, 간혹 204 메시지를 주는 경우도 있음
    - 204 : no contents 라는 의미
    - 정상적으로 삭제가 되었으니 앞으로 요청한 이 콘텐츠는 이용할 수 없다는 상태코드임 
- CRUD 관련해서 작업 완료했고 bash terminal 에서 아래 코드로 테스트 해 볼 수 있었음
```curl -X PUT -H "Content-Type: application/json; charset=utf-8" -d '{"userid":"lee"}' "http://127.0.0.1:5000/api/v1/users/4" ```


44494abda6147926ce4e34d689f3f296889fbdef
- user.py 에서 methods 중 POST 에 대한 부분은 어느정도 작성이 되었는데 이제 GET 에 대한 부분을 작업
- 이때 query.all() 을 활용할것임
    - 근데 이것은 JSON 형식이 아니어서 오류가 남
- 가독성이 좋고 더 편리하게 모델을 serialize 직렬화 해야함 
    > models.py 에 가서 class Fcuser 에 속성 (property) 값을 추가함

a3feef2beee189e686e1763c13652c3f53038714
인덴트 처리가 잘못되어있었던 부분 잡음
원하는 대로 정상적으로 작동하는 것을 확인하고 다음 스테이지로 넘어감

2024-08-27
API 는 리소스 중심

DB 관련 코드 설정
Blueprint (app.py에 추가)
- 내가 작성하는 controller 코드들이 app.py 안에 모여있지 않고 분리해서 작성할 수 있게 도와주는 기능
- api_v1 폴더 안에 만들어져있음 
- 우리가 개발한 controller 코드는 user.py 안에 만들어져있음

api 는 공통으로 사용하는 __init__ 안에 
api 루트에 생성하겠죠

API = 템플릿 코드를 반환한것이 아니라 
jsonify 함수를 통해서 resource 만 전달함

어떤 요청에 대한 응답
성공여부, 데이터만 전달, 에러코드 전달 

CRUD 라는 사용자 관련된 모든 API를 만들고 나서 Jquery (템플릿)쪽으로 가서 다 연결할 예정