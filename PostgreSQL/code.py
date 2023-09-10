import psycopg2, time

print("Waiting for the Postgres container to be ready...")
time.sleep(10)

print("Connecting to the Postgres container...")
conn = psycopg2.connect(host="postgres", dbname="db", user="user", password="password")
cur = conn.cursor()

print("Creating table and inserting data...")
cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")
cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)", (100, "abc'def"))
conn.commit()

print("Retrieving data...")
cur.execute("SELECT * FROM test;")
row = cur.fetchone()
assert row == (1, 100, "abc'def")
print(row)

print("Dropping table...")
cur.execute("DROP TABLE test;")
conn.commit()

print("Closing connection...")
cur.close()
conn.close()