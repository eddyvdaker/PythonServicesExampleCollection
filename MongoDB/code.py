import pymongo, time

print("Waiting for the MongoDB container to be ready...")
time.sleep(10)

print("Connecting to the MongoDB container...")
client = pymongo.MongoClient("mongodb://user:password@mongodb:27017/")
db = client["db"]
coll = db["example_collection"]

print("Inserting data...")
result = coll.insert_one({"num": 100, "data": "abc'def"})

print("Retrieving single record...")
row = coll.find_one({"num": 100})
assert row["_id"] == result.inserted_id
assert row["num"] == 100
assert row["data"] == "abc'def"
print(row)

print("retrieving all records...")
rows = coll.all
print(rows)

print("Dropping collection...")
coll.drop()

print("Closing connection...")
client.close()
