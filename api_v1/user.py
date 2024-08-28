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


    return jsonify()