import os
from flask import Flask, request, render_template, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from models import db, Fcuser
from api_v1 import api as api_v1



app = Flask(__name__)
#blueprint를 쓸거다 api_v1에서 제공하고 있는 controller 코드들은 user.py url_prefix 붙힌뒤에 제공하겠다
#200 정상처리, 실패코드 404, 403 
app.register_blueprint(api_v1, url_prefix='/api/v1')

app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this!
jwt = JWTManager(app)

#JWT 가 기본적으로 username 을 활용하고 있음
def authenticate(username, password) : 
    user = Fcuser.query.filter(Fcuser.userid == username).first()
    if user.password == password:
        return user


@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/login')
def login():
    
    return render_template('login.html')


@app.route('/auth', methods=['POST'])
def auth():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    user = authenticate(username, password)
    if user:
        # Generate a JWT token
        access_token = create_access_token(identity=user.userid)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"msg": "Bad username or password"}), 401

@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

@app.route('/')
def hello():
    return 'Hello World'

basedir = os.path.abspath(os.path.dirname(__file__))
dbfile = os.path.join(basedir, 'db.sqlite')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbfile
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True  # Commit on teardown
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Suppress warning messages
app.config['SECRET_KEY'] = 'adfhalskdjfl;asdjriern' #for CSRF

db.init_app(app)

# Ensure the following block runs within an app context
with app.app_context():
    db.create_all()  # Create the database tables


if __name__ == "__main__" :
    app.run(host='127.0.0.1', port=5000, debug=True)