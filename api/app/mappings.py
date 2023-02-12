# import lib
import psycopg2

# Function to get table schema from postgres database,  input is table name and database name
def get_table_schema(table_name, database_name):
    conn = psycopg2.connect(database=database_name)
    cur = conn.cursor()
    cur.execute("SELECT column_name, data_type FROM information_schema.columns WHERE table_name='{}'".format(table_name))
    schema = cur.fetchall()
    conn.close()
    return schema


# Function to compare input list with database schema in postgresql
def compare_input_with_schema(input_list, schema_list):
    if len(input_list)!= len(schema_list):
        return False
    for i in range(len(input_list)):
        if input_list[i]!= schema_list[i]:
            return False
    return True

# Send api request method post if the def compare_input_with_schema is returned False



