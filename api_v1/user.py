from flask import jsonify
from models import Fcuser, db
from flask import request
from . import api

#controller 코드를 만듬
@api.route('/users', methods=['GET', 'POST'])
def users():
    #회원생성
    if request.method == 'POST' :
        userid = request.form.get('userid')
        username = request.form.get('username')
        password = request.form.get('password')
        re_password = request.form.get('re-password')

        if not (userid and username and password and re_password) :
            return jsonify({'error' : 'No arguments'}), 400

        if password != re_password :
            return jsonify({'error' : 'Check password'}), 400 

        fcuser = Fcuser()
        fcuser.userid = userid
        fcuser.username = username
        fcuser.password = password

        db.session.add(fcuser)
        db.session.commit()

        return jsonify(), 201

    
    users = Fcuser.query.all()
    return jsonify([user.serialize for user in users])

@api.route('/users/<uid>', methods=['GET', 'PUT', 'DELETE'])
def user_detail(uid):
    #method 를 확인해서 원하는 api 를 만들 수 있음
    if request.method == 'GET' :
        user = Fcuser.query.filter(Fcuser.id ==uid).first()
        return jsonify(user.serialize)

    elif request.method == 'DELETE' : 
        Fcuser.query.delete(Fcuser.id == uid)
        return jsonify(), 204

    
    #method 가 세가지 경우 뿐이기 때문에 이 시점에 오는 것은 무조건 PUT method 임 
    #PUT 요청은 수정하는 것임
    #PUT의 경우, 바꿔치기 할때 사용함 (전체를 다 바꿔치기), 일부만 수정하고 싶을 경우 PATCH method 를 활용함
    #BUT 구현하기에 따라 PUT 에서도 일부수정이 가능함 ㅎㅎ 

    data = request.get_json()
    userid = data.get('userid')
    username = data.get('username')
    password = data.get('password')

    updated_data = {} #input data 가 없을 경우 빈 값을 가져가기 위해 빈 dictionary 를 만들어줌 
    if userid : 
        updated_data['userid'] = userid
    if username:
        updated_data['username'] = username
    if password :
        updated_data['password'] = password

    Fcuser.query.filter(Fcuser.id ==uid).update(updated_data)
    user = Fcuser.query.filter(Fcuser.id ==uid).first()
    return jsonify(user.serialize)
