
import os
import psycopg2
import json
from flask import Flask, request, jsonify

app = Flask(__name__)


def _get_db_config():
    with open('config.json') as f:
        config = json.load(f)
        host = config.get('host', '127.0.0.1'),
        database = config.get('database', 'dsp_analytics'),
        user = config.get('user', 'dsp_analytics'),
        password = config.get('password', 'analyticstest'),
        port = config.get('port', 5432)
    return {
        'host': host,
        'database': database,
        'user': user,
        'password': password,
        'port': port
    }


@app.route('/authenticate', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    conn = psycopg2.connect(
        host=db_configuration.get('DB_HOST'),
        database=db_configuration.get('DB_NAME'),
        user=db_configuration.get('DB_USER'),
        password=db_configuration.get('DB_PASSWORD')
    )
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
    result = cur.fetchone()
    conn.close()
    if result is None:
        return jsonify({'message': 'Invalid username or password'}), 401
    else:
        return jsonify({'message': 'Success'}), 200


@app.route('/users', methods=['GET'])
def get_users():
    conn = psycopg2.connect(
        host=db_configuration.get('DB_HOST'),
        database=db_configuration.get('DB_NAME'),
        user=db_configuration.get('DB_USER'),
        password=db_configuration.get('DB_PASSWORD')
    )
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
    result = cur.fetchall()
    conn.close()
    return jsonify(result), 200


@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    conn = psycopg2.connect(
        host=db_configuration.get('DB_HOST'),
        database=db_configuration.get('DB_NAME'),
        user=db_configuration.get('DB_USER'),
        password=db_configuration.get('DB_PASSWORD')
    )
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE id = %s", (user_id,))
    result = cur.fetchone()
    conn.close()
    return jsonify(result), 200


@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    username = request.form['username']
    password = request.form['password']
    conn = psycopg2.connect(
        host=db_configuration.get('DB_HOST'),
        database=db_configuration.get('DB_NAME'),
        user=db_configuration.get('DB_USER'),
        password=db_configuration.get('DB_PASSWORD')
    )
    cur = conn.cursor()
    cur.execute("UPDATE users SET username = %s, password = %s WHERE id = %s",
                (username, password, user_id))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Success'}), 200


@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    conn = psycopg2.connect(
        host=db_configuration.get('DB_HOST'),
        database=db_configuration.get('DB_NAME'),
        user=db_configuration.get('DB_USER'),
        password=db_configuration.get('DB_PASSWORD')
    )
    cur = conn.cursor()
    cur.execute("DELETE FROM users WHERE id = %s", (user_id,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Success'}), 200


@app.route('/users', methods=['POST'])
def create_user():
    username = request.form['username']
    password = request.form['password']
    conn = psycopg2.connect(
        host=db_configuration.get('DB_HOST'),
        database=db_configuration.get('DB_NAME'),
        user=db_configuration.get('DB_USER'),
        password=db_configuration.get('DB_PASSWORD')
    )
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Success'}), 200


if __name__ == '__main__':
    db_configuration = _get_db_config()
    app.run(debug=True)
