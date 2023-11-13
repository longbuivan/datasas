import os
import psycopg2
import logging
# set up logging
logging.basicConfig(filename='app.log', level=logging.INFO,
                    format='%(asctime)s %(message)s')


def _generate_sql_template(table_name, columns, rows):
    column_names = ", ".join(columns)
    placeholder = ', '.join(['(%s, %s)'] * len(rows))
    values = [item for sublist in rows for item in sublist]
    sql_template = f"INSERT INTO {table_name} ({column_names}) VALUES {placeholder}"
    return (sql_template, values)


def _common_execute_sql(conn, sql):
    with conn:
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        cur.close()
    return True


# Get the last transfer timestamp
def _get_last_trans(conn_type, conn_string, table_name, last_transfer_timestamp):
    if conn_type == "GET":
        try:
            connection_string = conn_string
            conn = psycopg2.connect(
                host=os.environ['DB_HOST'],
                port=os.environ['DB_PORT'],
                database=os.environ['DB_NAME'],
                user=os.environ['DB_USER'],
                password=os.environ['DB_PASS'])
            cursor = conn.cursor()
            cursor.execute(
                "SELECT {last_transfer_timestamp} FROM config_table")
            last_transfer_timestamp = cursor.fetchone()[0]
            logging.info("Successfully fetched the last transfer timestamp")
            cursor.execute(
                f"SELECT * FROM {table_name} WHERE timestamp > {last_transfer_timestamp}")
            data = cursor.fetchall()
            logging.info("Successfully fetched updated data from the database")
        except Exception as e:
            logging.error(
                "Error while fetching updated data from the database: %s", e)

        # Close the cursor and database connection
        cursor.close()
        conn.close()
        return data


def _insert_trans(conn_type, conn_string, table_name, columns, insert_data):
    if conn_type == "POST":
        try:
            connection_string = conn_string
            conn = psycopg2.connect(
                host=os.environ['DB_HOST'],
                port=os.environ['DB_PORT'],
                database=os.environ['DB_NAME'],
                user=os.environ['DB_USER'],
                password=os.environ['DB_PASS'])
            cursor = conn.cursor()

            # Get the updated data from the database
            sql_stmt = _generate_sql_template(table_name, columns, insert_data)
            cursor.execute(sql_stmt)
            logging.info(
                "Successfully inserting updated data from the database")
        except Exception as e:
            logging.error(
                "Error while inserting updated data from the database: %s", e)

        # Close the cursor and database connection
        cursor.close()
        conn.close()
        return len(insert_data)
