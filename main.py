from flask import Flask, jsonify




users = [
  {
    "id": 1,
    "username": "JohnDoe",
    "age": 32,
    "weight": 75.5,
    "height": 180
  },
  {
    "id": 2,
    "username": "JaneSmith",
    "age": 28,
    "weight": 62.1,
    "height": 165
  },
  {
    "id": 3,
    "username": "MikeJohnson",
    "age": 41,
    "weight": 85.2,
    "height": 190
  },
  {
    "id": 4,
    "username": "EmilyBrown",
    "age": 24,
    "weight": 58.7,
    "height": 155
  },
  {
    "id": 5,
    "username": "DavidWilson",
    "age": 37,
    "weight": 79.9,
    "height": 175
  }
]



def get_user(users, id):
    for user in users:
        if user['id'] == id:
            return user
    
    return None




app = Flask(__name__)


# http://localhost:5000/users
@app.route("/users", methods=['GET'])
def get_users():

    return jsonify(users)


# http://localhost:5000/users/:id
@app.route("/users/<int:id>", methods=['GET'])
def get_user_by_id(id):

    user = get_user(users, id)

    if user != None:
        return jsonify(user)
    else:
        rsp = {'status': 'faild', 'msg': 'user not found'}
        return (jsonify(rsp), 404)







app.run('127.0.0.1', 5000, debug=True)