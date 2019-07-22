# Initiates the database
client = pymongo.MongoClient("mongodb+srv://dn54321:<password>@cluster0-kixdi.mongodb.net/test?retryWrites=true&w=majority")
db = client.test
