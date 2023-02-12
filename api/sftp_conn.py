# import lib for sftp
import paramiko
import sys
import logging
import logging.handlers
from io import BytesIO
# import lib for AWS Cloud
import boto3

# create s3 client
s3_client = boto3.client('s3')

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


# initialize variables
sftp_host = 'localhost'
sftp_port = 22
username = 'root'
password = 'root'
sftp_path = '/home/ubuntu/data'
s3_bucket = 'ubuntu-data'


class SFTPClient(object):
    def __init__(self, host, username, password, port=22):
        self.host = host
        self.username = username
        self.password = password
        self.port = port
        self.sftp = None
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        self.logger.addHandler(logging.StreamHandler(sys.stdout))
        self.logger.addHandler(
            logging.handlers.SysLogHandler(address='/dev/log'))
        self.logger.info('SFTP Client Initialized')
        self.connect()
        self.logger.info('SFTP Client Connected')

    def connect(self):
        try:
            self.sftp = paramiko.SSHClient()
            self.sftp.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.sftp.connect(self.host, username=self.username,
                              password=self.password, port=self.port)
            self.logger.info('SFTP Client Connected')
        except Exception as e:
            self.logger.error('SFTP Client Connect Error: {}'.format(e))
            sys.exit(1)

    def close(self):
        self.sftp.close()
        self.logger.info('SFTP Client Closed')
        self.sftp = None

    def put(self, local_path, remote_path):
        try:
            self.sftp.put(local_path, remote_path)
        except Exception as e:
            self.logger.error('SFTP Client Put Error: {}'.format(e))
            sys.exit(1)

    def get(self, remote_path, local_path):
        try:
            self.sftp.get(remote_path, local_path)
        except Exception as e:
            self.logger.error('SFTP Client Get Error: {}'.format(e))
            sys.exit(1)

    def list(self, remote_path):
        try:
            self.sftp.listdir(remote_path)
        except Exception as e:
            self.logger.error('SFTP Client List Error: {}'.format(e))
            sys.exit(1)

    def remove(self, remote_path):
        try:
            self.sftp.remove(remote_path)
        except Exception as e:
            self.logger.error('SFTP Client Remove Error: {}'.format(e))
            sys.exit(1)

def main():
    sftp_client = SFTPClient(sftp_host, username, password, port=sftp_port)
    logging.info("Connecting to SFTP host: %s", sftp_host)
    sftp_client.connect()
    logging.info("Listing directories: /, /home, /home/user")
    sftp_client.list('/')
    sftp_client.list('/home')
    sftp_client.list('/home/user')
    # List the files on the SFTP server
    file_list = sftp_client.listdir(sftp_path)
    logging.info("Files to be uploaded: %s", file_list)
    # Loop through the files and upload to S3
    for file_name in file_list:
        file_path = sftp_path + '/' + file_name
        data = sftp_client.open(file_path).read()
        logging.info("Uploading file: %s", file_name)
        s3_client.upload_fileobj(BytesIO(data), s3_bucket, file_name)
    logging.info("Uploading process completed")
    # Close the SFTP connection
    logging.info("Closing SFTP connection")
    sftp_client.close()
