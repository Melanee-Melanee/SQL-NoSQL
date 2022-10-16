import pymongo
import dns





client = pymongo.MongoClient("mongodb+srv://SHAGHAYEGH:5BZ0cZpSrm98N78Z@cluster0.fqivsky.mongodb.net/?retryWrites=true&w=majority")




db = client['test']
col= db['test1']
print(client.list_database_names()) 
#print(db.list_collection_names())
#dic = {'name': 'Melanee', 'age':'31' }
#x=col.insert_one(dic)
#print(x)