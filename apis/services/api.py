
from flask import Flask
import json
import psycopg2
import logging
from flask import request
from common import read_connection_string_from_vault
from jdbc_conn import _get_last_trans, _insert_trans
from rest_api_conn import _get_data
from kafka_conn import _get_kafka_consumer
app = Flask(__name__)
# api = Api(app)
logging.basicConfig(filename='app.log', level=logging.INFO,
                    format='%(asctime)s %(message)s')


@app.route('/jdbc', methods=['GET', 'POST'])
def jdbc_conn():
    """
    JDBC connection function

    This function is used to establish a JDBC connection. It retrieves the required parameters
    from the incoming request and passes them to the `read_connection_string_from_vault`
    function to get the connection string.

    If the request method is GET, it fetches the last transfer data by calling the 
    `_get_last_trans` function and returns the data in JSON format.

    If the request method is POST, it inserts the ingested data into the database by calling
    the `_insert_trans` function and returns the affected data in JSON format.
    """
    req = request.get_json()
    logging.debug(req)
    vault_url = req['vault_url']
    vault_token = req['vault_token']
    secret_path = req['secret_path']
    table_name = req['table_name']

    #  Read the connection string from Vault
    secret = read_connection_string_from_vault(
        vault_url=vault_url, vault_token=vault_token, path=secret_path)

    if request.method == 'GET':
        last_timestamp = req['last_timestamp']
        secret = secret['connection_string']
        ingested_data = _get_last_trans(
            request.method, conn_string=secret, table_name=table_name, last_transfer_timestamp=last_timestamp)
        return ingested_data
    elif request.method == 'POST':
        ingested_data = req['body']['ingested_data']
        columns = req['body']['columns']
        affected_rows = _insert_trans(request.method, conn_string=secret,
                                      table_name=table_name, columns=columns, insert_data=ingested_data)
        return affected_rows

# Rest API connection


@app.route('/rest', methods=['GET', 'POST'])
def rest_conn():
    """
    REST API Connection

    This function is used to establish a REST API connection. It retrieves the required parameters
    from the incoming request and passes them to the `read_connection_string_from_vault`
    function to get the connection string.

    If the request method is GET, it fetches the last transfer data by calling the 
    `_get_data` function and returns the data in JSON format.

    If the request method is POST, send data in JSON format to API endpoint.
    """
    req = request.get_json()
    logging.debug(req)
    vault_url = req['vault_url']
    vault_token = req['vault_token']
    secret_path = req['secret_path']

    secret = read_connection_string_from_vault(
        vault_url=vault_url, vault_token=vault_token, path=secret_path)

    if request.method == 'GET':
        api_url = req['api_url']
        last_timestamp = req['last_timestamp']
        access_token = secret['access_token']
        ingested_data = _get_data(
            api_url=api_url, access_token=access_token, last_timestamp=last_timestamp)
        return ingested_data
    if request.method == 'POST':
        return json.dumps({'success': True, 'message': "Not implemented"})


# SFTP Connection
@app.route('/sftp', methods=['GET', 'POST'])
def sftp_conn():
    """
    SFTP Connection

    This function is used to establish a SFTP connection. It retrieves the required parameters
    from the incoming request and passes them to the `read_connection_string_from_vault`
    function to get the connection string.

    If the request method is GET, it fetches the last transfer data by calling the 
    `_get_data` function and returns the data in JSON format.

    If the request method is POST, send data in JSON format to API endpoint.
    """
    req = request.get_json()
    logging.debug(req)
    vault_url = req['vault_url']
    vault_token = req['vault_token']
    secret_path = req['secret_path']

    secret = read_connection_string_from_vault(
        vault_url=vault_url, vault_token=vault_token, path=secret_path)

    if request.method == 'GET':
        api_url = req['api_url']
        last_timestamp = req['last_timestamp']
        credentials = req['credentials']
        ingested_data = _get_data(credentials)
        return ingested_data
    if request.method == 'POST':
        return json.dumps({'success': True, 'message': "Not implemented"})

# Kafka connection


@app.route('/kafka', methods=['GET', 'POST'])
def kafka_conn():
    """
    Kafka connection

    This function is used to establish a Kafka connection. It retrieves the required parameters
    from the incoming request and passes them to the `read_connection_string_from_vault`
    function to get the connection string.

    If the request method is GET, it fetches the last transfer data by calling the 
    `_get_kafka_consumer` function and returns the data in JSON format.

    If the request method is POST, send data in JSON format to API endpoint.
    """
    req = request.get_json()
    logging.debug(req)
    vault_url = req['vault_url']
    vault_token = req['vault_token']
    secret_path = req['secret_path']

    secret = read_connection_string_from_vault(
        vault_url=vault_url, vault_token=vault_token, path=secret_path)

    if request.method == 'GET':
        consumer_conf = req['consumer_conf']
        topic = req['topic']
        credentials = req['credentials']
        ingested_data = _get_kafka_consumer(consumer_conf, credentials, topic)
        return ingested_data
    if request.method == 'POST':
        return json.dumps({'success': True, 'message': "Not implemented"})


if __name__ == '__main__':
    app.run(debug=True)
#     # app.run(host='0.0.0.0', port=5000)
#     # app.run(host='0.0.0.0', port=5000, threaded=True)
#     # app.run(host='0.0.0.0', port=5000, threaded=True, use_reloader=True)
#     # app.run(host='0.0.0.0', port=5000, threaded=True, use_reloader=True, use_debugger=True)

#     # app.run(host='0.0.0.0', port=5000, threaded=True, use_reloader=True, use_debugger=True, use_evalex=True)
