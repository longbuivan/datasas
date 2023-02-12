import psycopg2
import boto3
import hvac
import logging
import datetime

# set up logging
logging.basicConfig(filename='app.log', level=logging.INFO,
                    format='%(asctime)s %(message)s')

conn = psycopg2.connect(
    host="hostname",
    database="database_name",
    user="username",
    password="password"
)
# create s3 client
s3_client = boto3.client('s3')


# generate template for execution sql statements
def generate_sql_template(table_name, columns, rows):
    column_names = ", ".join(columns)
    placeholder = ', '.join(['(%s, %s)'] * len(rows))
    values = [item for sublist in rows for item in sublist]
    sql_template = f"INSERT INTO {table_name} ({column_names}) VALUES {placeholder}"
    return (sql_template, values)

# function to execute sql statements
def execute_sql(sql):
    with conn:
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        cur.close()
    # close connection
    conn.close()
    # return result
    return True


# Connect to Hashicorp Vault to retrieve the database credentials
client = hvac.Client(url="http://vault.example.com:8200")
try:
    client.auth_approle("my-approle-id", "my-secret-id")
    logging.info("Successfully authenticated to Vault")
except Exception as e:
    logging.error("Error while authenticating to Vault: %s", e)

secret = client.read("secret/database")

# Connect to the local PostgreSQL database using the credentials from Vault
try:
    conn = psycopg2.connect(
        host="localhost",
        database=secret["data"]["database"],
        user=secret["data"]["username"],
        password=secret["data"]["password"]
    )
    logging.info("Successfully connected to PostgreSQL database")
except Exception as e:
    logging.error("Error while connecting to PostgreSQL database: %s", e)

# Create a cursor object to execute SQL commands
cur = conn.cursor()

# Get the last transfer timestamp
try:
    cursor = conn.cursor()
    cursor.execute("SELECT last_transfer_timestamp FROM config_table")
    last_transfer_timestamp = cursor.fetchone()[0]
    logging.info("Successfully fetched the last transfer timestamp")
except Exception as e:
    logging.error("Error while fetching the last transfer timestamp: %s", e)

# Get the updated data from the database
try:
    cursor.execute(
        f"SELECT * FROM table_name WHERE timestamp > {last_transfer_timestamp}")
    data = cursor.fetchall()
    logging.info("Successfully fetched updated data from the database")
except Exception as e:
    logging.error("Error while fetching updated data from the database: %s", e)

# Close the cursor and database connection
cur.close()
conn.close()

# function to put data into s3 bucket using current timestamp as key


def put_data_to_s3(bucket_name, file_name, data):
    # Get the current timestamp
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Use the current timestamp as the partition key in S3
    s3_client.put_object(Bucket=bucket_name,
                         Key=f"{now}/{file_name}", Body=data)
    print(
        f"Data successfully uploaded to S3, bucket: {bucket_name}, key: {now}/{file_name}")
