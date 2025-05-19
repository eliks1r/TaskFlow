from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from functools import wraps

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'  # Используй свой секретный ключ
jwt = JWTManager(app)

# Моковые данные о пользователях
users = [
    {"id": 1, "email": "user@example.com", "password": "userpass", "role": "user"},
    {"id": 2, "email": "admin@example.com", "password": "adminpass", "role": "admin"}
]

# Функция для поиска пользователя по email
def get_user_by_email(email):
    for user in users:
        if user['email'] == email:
            return user
    return None

# Декоратор для проверки роли
def role_required(role):
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            current_user = get_jwt_identity()
            user = get_user_by_email(current_user['email'])
            if user['role'] != role:
                return jsonify({"msg": "Permission denied"}), 403
            return fn(*args, **kwargs)
        return decorator
    return wrapper

# Маршрут для логина и получения токена
@app.route('/login', methods=['POST'])
def login():
    email = request.json.get('email')
    password = request.json.get('password')

    user = get_user_by_email(email)
    if user and user['password'] == password:
        access_token = create_access_token(identity={"email": email})
        return jsonify(access_token=access_token)
    
    return jsonify({"msg": "Invalid credentials"}), 401

# Защищённый маршрут для получения данных админа
@app.route('/admin', methods=['GET'])
@jwt_required()
@role_required('admin')
def admin_data():
    return jsonify({"msg": "This is admin data"})

# Защищённый маршрут для обычного пользователя
@app.route('/user', methods=['GET'])
@jwt_required()
@role_required('user')
def user_data():
    return jsonify({"msg": "This is user data"})

if __name__ == '__main__':
    app.run(debug=True)
    

