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