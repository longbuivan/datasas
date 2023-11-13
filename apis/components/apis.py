import psycopg2
import json
from flask import Flask, request
import mappings

import logging
logging.basicConfig(filename='app.log', level=logging.INFO,
                    format='%(asctime)s %(message)s')
app = Flask(__name__)

def check_sql(sql, type):
    if sql is None:
        return "SQL query is missing from the request body", 400

    if not sql.endswith(";"):
        return "SQL query must end with a semicolon", 400

    if not sql.count(";") == 1:
        return "SQL query must contain exactly one semicolon", 400

    if not sql.count(";") == 1:
        return "SQL query must contain exactly one semicolon", 400

    if type == 'editor':
        if sql.upper().startswith("ALTER"):
            return "SQL query must start with [SELECT, INSERT, UPDATE]", 400

    if type == 'viewer':
        if sql.upper().startswith("SELECT") and sql.upper().startswith("INSERT") and sql.upper().startswith("UPDATE"):
            return "SQL query must start with [SELECT]", 400


def connect_to_jdbc():
    with open('config.json') as f:
        config = json.load(f)

    try:
        connection = psycopg2.connect(
            host=config.get('host', '127.0.0.1'),
            database=config.get('database', 'dsp_analytics'),
            user=config.get('user', 'dsp_analytics'),
            password=config.get('password', 'analyticstest')
        )
        app.logger.info("Connected to JDBC database")
        return connection
    except Exception as e:
        app.logger.info(e)
        return None


@app.route('/api/jdbc/query', methods=['POST'])
def query_jdbc():
    sql = request.get_json().get('sql')
    
    check_sql(sql=sql,type="viewer")
    
    connection = connect_to_jdbc()
    if not connection:
        raise Exception("Unable to connect to the database")
    cursor = connection.cursor()
    app.logger.info("Executing SQL query")
    cursor.execute(sql)

    result = cursor.fetchall()

    result_json = json.dumps(result, default=str)

    cursor.close()
    connection.close()
    app.logger.info("Closed connection")

    return result_json, 200

@app.route('/api/jdbc/push', methods=['POST'])
def push_jdbc():
    sql = request.get_json().get('sql')

    check_sql(sql=sql, type="editor")
    connection = connect_to_jdbc()
    if not connection:
        raise Exception("Unable to connect to the database")
    cursor = connection.cursor()
    app.logger.info("Executing SQL query")
    cursor.execute(sql)

    cursor.close()
    connection.close()
    app.logger.info("Closed connection")

    return 200



if __name__ == '__main__':
    app.run(debug=True)

