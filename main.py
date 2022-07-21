import pymongo
client = pymongo.MongoClient("mongodb+srv://Ashwin123:9819Ash@cluster0.nczx4oy.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d= {
    "name":"Ashwin",
    "email":"ashwin.dhamnaskar22@gmail.com",
    "surname":"Dhamnaskar"
}
db1 = client['mongotest']
coll= db1['test1']
coll.insert_one(d )