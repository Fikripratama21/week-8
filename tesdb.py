import pymongo
import uuid
import datetime


client = pymongo.MongoClient("mongodb+srv://fikri:ardigendut1234@cluster0.biklqid.mongodb.net/?retryWrites=true&w=majority")
db = client.MyDatabase
collection = db.MyCollect
def save_to_db(latitude,longitude,kecepatan) -> tuple:
    try:
        data = {
            "request_id" : str(uuid.uuid4()),
            "latitude": latitude,
            "longitude": longitude,
            "kecepatan": kecepatan,
            "timestamp": datetime.datetime.now()
        }

        rec_id1 = collection.insert_one(data)

        print("Data inserted with record ids",rec_id1)
        return True,None
    except Exception as e:
        return False,str(e)
        
save_to_db(-7.811416920979732,112.02551519641301,100)