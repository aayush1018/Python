from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Float
import os
from flask_marshmallow import Marshmallow
from flask_marshmallow.sqla import SQLAlchemyAutoSchema
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
from flask_mail import Mail, Message
#for the demo project we are going to use mailtrap, you can set your own server and change the credentails accordingly


app = Flask(__name__)
basedir= os.path.abspath(os.path.dirname(__file__))   #setting path for the application itself
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test_api.db')
app.config['JWT_SECRET_KEY'] = 'super-secret' #change this in real life

app.config['MAIL_SERVER']=os.environ['MAIL_SERVER']
app.config['MAIL_PORT'] = os.environ['MAIL_PORT']
app.config['MAIL_USERNAME'] = os.environ['MAIL_USERNAME']
app.config['MAIL_PASSWORD'] = os.environ['MAIL_PASSWORD']
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False


db = SQLAlchemy(app)
ma = Marshmallow(app)
jwt = JWTManager(app)
mail = Mail(app)


@app.cli.command('db_create')
def db_create():
    db.create_all()
    print("Database creation successful")


@app.cli.command('db_drop')
def db_drop():
    db.drop_all()
    print("Database drop successful")


@app.cli.command('db_seed')
def db_seed():
    mercury = TestAPI(planet_name='Mercury',
                      planet_type='Class D',
                      mass=3.256e23,
                      radius=1516,
                      distance=35.98e6)

    venus = TestAPI(planet_name='Venus',
                      planet_type='Class K',
                      mass=4.867e24,
                      radius=3760,
                      distance=67.24e6)
    earth = TestAPI(planet_name='Earth',
                      planet_type='Class M',
                      mass=5.972e24,
                      radius=3959,
                      distance=92.96e6)

    db.session.add(mercury)
    db.session.add(venus)
    db.session.add(earth)

    test_user= User(first_name='Test',last_name='User',email='test@email.com',password='@bCd')
    db.session.add(test_user)
    db.session.commit()
    print("Database seed successful!!")

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route("/simple_route")
def simple_route():
    return jsonify(message="Welcome to Demo API.")


@app.route("/parameters")
def parameters():
    name = request.args.get("name")
    age = int(request.args.get("age"))
    if age < 18:
        return jsonify(message= "Hi " + name + ", you are not authorized to access this page"), 401
    else:
        return jsonify(message= "Hi " + name + ", welcome to test API")


@app.route("/url_variables/<string:name>/<int:age>")
def url_variables(name: str, age: int):
    if age < 18:
        return jsonify(message= "Hi " + name + ", you are not authorized to access this page"), 401
    else:
        return jsonify(message= "Hi " + name + ", welcome to test API")


@app.route("/error_not_found")
def error_not_found():
    return jsonify(message="No API found"), 404

@app.route("/planets", methods=['GET'])
def planets():
    planets_list = TestAPI.query.all()
    result = planets_schema.dump(planets_list)
    return jsonify(result)

@app.route("/register", methods=["POST"])
def register():
    email = request.form['email']
    test = User.query.filter_by(email=email).first()
    if test:
        return jsonify(message="Email already exists"), 409
    else:
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        password = request.form['password']
        user = User(first_name=first_name, last_name=last_name, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        return jsonify(message="User created successfully"), 201

@app.route('/login', methods=['POST'])
def login():
    if request.is_json:
        email = request.json['email']
        password = request.json['password']
    else:
        email = request.form['email']
        password = request.form['password']
    test = User.query.filter_by(email=email, password= password).first()
    if test:
        access_token = create_access_token(identity=email)
        return jsonify(message="Login Sucessful!!", access_token=access_token)
    else:
        return jsonify(message="Bad email or password"), 401


#if you are unable to receive the response for success test case, make sure you have passed all the configuration details like port, server, tls, ssl details above
@app.route('/retrieve_password/<string:email>', methods =['GET'])
def retrieve_password(email: str):
    user = User.query.filter_by(email=email).first()
    if user:
        msg= Message("Your Test API password is " + user.password,
                     sender = "admin@testAPI.com",
                     recipients=[email])
        mail.send(msg)
        return jsonify(message="Password send to " +email)
    else:
        return jsonify(message ="The email " +email+ " doesn't exist"), 401

@app.route('/planet_details/<int:planet_id>',methods=["GET"])
def planet_details(planet_id: int):
    planet= TestAPI.query.filter_by(planet_id=planet_id).first()
    if planet:
        result = planet_schema.dump(planet)
        return jsonify(result)
    else:
        return jsonify(message="Planet id does not exists"), 404

@app.route('/add_planet', methods=['POST'])
@jwt_required()
def add_planet():
    planet_name = request.form['planet_name']
    test = TestAPI.query.filter_by(planet_name=planet_name).first()
    if test:
        return jsonify(message="Planet name already exists"), 409
    else:
        planet_type = request.form['planet_type']
        mass = float(request.form['mass'])
        radius = float(request.form['radius'])
        distance = float(request.form['distance'])

        new_planet = TestAPI(planet_name=planet_name,
                             planet_type=planet_type,
                             mass=mass,
                             radius=radius,
                             distance=distance)

        db.session.add(new_planet)
        db.session.commit()
        return jsonify(message='Planet added sucessfully'), 201


@app.route('/update_planet/<int:planet_id>', methods=['PUT'])
@jwt_required()
def update_planet(planet_id: int):
    planet_id = int(request.form['planet_id'])
    test_id = TestAPI.query.filter_by(planet_id=planet_id).first()
    if test_id:
        test_id.planet_name = request.form['planet_name']
        test_id.planet_type = request.form['planet_type']
        test_id.mass = float(request.form['mass'])
        test_id.radius = float(request.form['radius'])
        test_id.distance = float(request.form['distance'])
        db.session.commit()
        return jsonify(message='Planet updated sucessfully')
    else:
        return jsonify(message="Planet id does not exists"), 404


@app.route('/delete_planet/<int:planet_id>', methods=['DELETE'])
@jwt_required()
def delete_planet(planet_id: int):
    planet_id = int(request.form['planet_id'])
    test_id = TestAPI.query.filter_by(planet_id=planet_id).first()
    if test_id:
        db.session.delete(test_id)
        db.session.commit()
        return jsonify(message='Planet deleted sucessfully')
    else:
        return jsonify(message="Planet id does not exists"), 404


#database model
class User(db.Model):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)


class TestAPI(db.Model):
    __tablename__ = "planets"
    planet_id = Column(Integer, primary_key=True)
    planet_name = Column(String)
    planet_type = Column(String)
    mass = Column(Float)
    radius = Column(Float)
    distance = Column(Float)

#ma.schema returns an error.. To avoid such errors we can use autoschema which fetches the data automatically for us
class TestuserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True

#ma.schema returns an error.. To avoid such errors we can use autoschema which fetches the data automatically for us
class DemotestApi(SQLAlchemyAutoSchema):
    class Meta:
        model = TestAPI
        load_instance = True

user_schema = TestuserSchema() #returns single object
users_schema = TestuserSchema(many=True) #this returns multiple objects in the result

planet_schema = DemotestApi()
planets_schema = DemotestApi(many=True)


if __name__ == '__main__':
    app.run()
