# setting up
#powershell 에서 권한 설정 하기 위해 아래 command 실행

Set-ExecutionPolicy -Scope CurrentUser

#이후 매개 변수에 대한 값을 제공 요청할 경우 
Unrestricted

# 이후 venve 환경 설정 하기 위해 
# 아래 폴더에서
PS C:\Users\songb\api\

#venv 설정
# python -m venv 

# 아래 스크립트 실행
./api_v1/Scripts/activate

(api_v1) PS C:\Users\songb\api

#사용하는 library
pip install Flask-SQLAlchemy flask 

#아래 실행
flask --app app run
#or
python app.py

#sqlite 들어가서 db 확인
sqlite3 db.sqlite

select * from fcuser; 