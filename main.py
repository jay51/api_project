from flask import Flask, jsonify, request




users = [
  {
    "id": 10,
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



id = 11
app = Flask(__name__)


# GET http://localhost:5000/users
@app.route("/users", methods=['GET'])
def get_users():

    return jsonify(users)


# GET http://localhost:5000/users/:id
@app.route("/users/<int:id>", methods=['GET'])
def get_user_by_id(id):

    user = get_user(users, id)

    if user != None:
        return jsonify(user)
    else:
        rsp = {'status': 'faild', 'msg': 'user not found'}
        return (jsonify(rsp), 404)


# DELETE http://localhost:5000/users/:id
@app.route("/users/<int:id>", methods=['DELETE'])
def delete_user_by_id(id):
  global users

  found = False
  for x in range(len(users)-1):
    if users[x]['id'] == id:
      users.pop(x)
      found = True


  if found == True:
      return jsonify(users)
  else:
    rsp = {'status': 'faild', 'msg': 'user not found'}
    return (jsonify(rsp), 404)



# POST http://localhost:5000/users
@app.route("/users", methods=['POST'])
def create_user():
  global id
  global users
  user_data = request.get_json()
  # {'keys': 'val'}

  if 'username' not in user_data or 'age' not in user_data or 'weight' not in user_data or 'height' not in user_data:
    rsp = {'status': 'faild', 'msg': 'invalid user data'}
    return (jsonify(rsp), 400)
  
  user_data['id'] = id
  id += 1
  users.append(user_data)

  return jsonify(users)

  # username = 0
  # age = 0
  # weight = 0
  # height = 0




app.run('127.0.0.1', 5000, debug=True)