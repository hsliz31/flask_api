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