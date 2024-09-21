from pymongo import MongoClient
from dotenv import load_dotenv
import os
load_dotenv()
client = MongoClient(
    os.environ.get("MONGO_URL")
)

db = client["test"]
collection = db["entries"]

text = "Vaa"
airesp = "airesp"
ipt = 12
opt = 13
tt = 14

collection.insert_one(
    {
        "user_id": "Vaasa",
        "Duser_text": text,
        "AI_response": airesp,
        "input_tokens": ipt,
        "output_tokens": opt,
        "total_tokens": tt,
    }
)

client.close()
