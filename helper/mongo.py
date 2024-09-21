from pymongo import MongoClient
from datetime import datetime
from dotenv import load_dotenv
import os
load_dotenv()


# Get the current timestamp
current_timestamp = datetime.now()

# Format the timestamp
formatted_timestamp = current_timestamp.strftime("%Y-%m-%d %H:%M:%S")

# Connect to MongoDB
client = MongoClient(os.environ.get("MONGO_URL"))

db = client["test"]
collection = db["entries"]

Dcollection = db["dentries"]

# current_time = int(time.time())


# Insert documents
def insert(text, airesp, ipt, opt, tt):

    try:
        collection.insert_one(
            {
                "user_id": "Vaasa",
                "user_text": text,
                "AI_response": airesp,
                "input_tokens": ipt,
                "output_tokens": opt,
                "total_tokens": tt,
                "created_at": formatted_timestamp,
                "updated_at": formatted_timestamp,
            }
        )
        # client.close()
    except Exception as e:
        raise RuntimeError(f"Error inserting into MongoDB: {e}")


def dinsert(text, airesp, ipt, opt, tt):
    try:
        Dcollection.insert_one(
            {
                "user_id": "Vaasa",
                "Duser_text": text,
                "AI_response": airesp,
                "input_tokens": ipt,
                "output_tokens": opt,
                "total_tokens": tt,
                "created_at": formatted_timestamp,
                "updated_at": formatted_timestamp,
            }
        )
        # client.close()
    except Exception as e:
        raise RuntimeError(f"Error inserting into MongoDB: {e}")
