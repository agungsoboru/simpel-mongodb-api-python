from pymongo import MongoClient
from fastapi import FastAPI

app = FastAPI()



@app.get("/items/{harga_min}")
async def read_item(harga_min,harga_max):
#    harga_max = 43.000
    client = MongoClient('mongodb://localhost:33611/')
    db = client["agungsurya"]
    collection = db["items"]
    cursor = collection.find( {"item price": {"$gte": f"Rp{harga_min}", "$lte": f"Rp{harga_max}"}})
    for document in cursor:
        print(document)
        other_variable = document
        other_variable["_id"] = str(other_variable["_id"])
        return other_variable
