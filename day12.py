import psycopg2

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    database="postgres",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432"
)

conn.autocommit = True

# Create a cursor object
cur = conn.cursor()

# Execute SQL queries here
# cur.execute('CREATE DATABASE database1;')
# cur.execute('CREATE DATABASE database2;')
# cur.execute('CREATE DATABASE database3;')

#Execute SQL to view all datases
# cur.execute('SELECT datname FROM pg_database;')
# databases = cur.fetchall()
# print(databases)

# Execute SQL TO CREATE A TABLE
cur.execute('''
            CREATE TABLE table1 (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            age INT
            );
        ''')

# Execute SQL to insert data into the table
cur.execute("INSERT INTO table1 (name, age) VALUES (%s, %s);", ('Pavan', 25))

cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public';")
tables = cur.fetchall()
print(tables)


# Execute SQL to view data from a table
cur.execute("SELECT * FROM table1;")
data = cur.fetchall()
for row in data:
    print(row)



# Close the cursor and connection
cur.close()
conn.close()