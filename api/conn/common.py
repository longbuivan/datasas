import os
import hvac
import boto3
import sys
import logging
logging.basicConfig(filename='app.log', level=logging.INFO,
                    format='%(asctime)s %(message)s')


def read_connection_string_from_vault(vault_url, vault_token, path):
    """
    Read the connection string from Vault
    :param vault_url: URL of the Vault server
    :param vault_token: authentication token for Vault
    :param path: path of the secret in Vault
    :return: connection string
    """
    try:
        client = hvac.Client(url=vault_url, token=vault_token)
        secret = client.read(path)
        return secret["data"]["connection_string"]
    except Exception as e:
        print(f"Error reading connection string from Vault: {e}")
        return None


def write_to_s3(data, conn_type, bucket_name, file_name):
    """
    Write data to S3
    :param data: data to write
    :param conn_type: connection type
    :param bucket_name: name of the bucket
    :param file_name: name of the file
    """

    s3_client = boto3.client("s3")

    now = datetime.now()
    datetime = datetime = now.strftime("%Y/%m/%d")

    key = f"{conn_type}/{datetime}/{file_name}"
    
    s3_client.put_object(Bucket=bucket_name, Key=key, Body=data)
    return True

