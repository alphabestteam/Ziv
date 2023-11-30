from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

#MySQL Connection Configuration
users_db = mysql.connector.connect(
    host="mysql",
    user="root",
    password="",
    database="users",
    port=3306
)

cursor = users_db.cursor()

cursor.execute(f"SHOW TABLES LIKE 'users'")
if not cursor.fetchone():
    cursor.execute(
        #Create table in case one doesn't exist
        f"CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))"
    )

@app.route('/users', methods=['POST', 'GET'])
def handle_requests():
    #When user is posted, add to users database and send matching message
    if request.method == 'POST':
        name = request.json.get('name')
        if name:
            cursor.execute("INSERT INTO users (name) VALUES (%s)", (name,))
            users_db.commit()
            user_id = cursor.lastrowid
            return f'User "{name}" was successfully added to the database with the ID "{user_id}".'
        else:
            return f"Invalid POST request"
    elif request.method == 'GET':
    #Otherwise, when we try to get all users from the user, they are returned
        cursor.execute("SELECT name FROM users")
        users = [user[0] for user in cursor.fetchall()]
        return jsonify(users)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)
