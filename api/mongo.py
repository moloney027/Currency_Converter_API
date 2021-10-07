import pymongo

db_client = pymongo.MongoClient("mongodb://localhost:27017/")

current_db = db_client["testdb"]

collection = current_db["exchange_rates"]

docs = [
    {'currency': 'USD', 'description': 'Доллар США', 'rate': 72.5682},
    {'currency': 'EUR', 'description': 'Евро', 'rate': 83.9251},
    {'currency': 'BYN', 'description': 'Белорусский рубль', 'rate': 29.0622},
    {'currency': 'UAH', 'description': 'Украинская гривна', 'rate': 2.75566},
    {'currency': 'CNY', 'description': 'Китайский юань', 'rate': 11.2566},
    {'currency': 'RON', 'description': 'Румынский лей', 'rate': 16.9540}
]

ins_result = collection.insert_many(docs)
print("id объекта: ", ins_result.inserted_ids)

print(collection.find_one({'rate': 2.75566}))

