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

    elif request.method
