import os, sys
import pymongo
import pandas as pd
import certifi
from dotenv import load_dotenv
from networksecurity.exception.exception import NetworkSecurityException

load_dotenv()

MONGO_DB_URL = os.getenv("MONGODB_URL")
ca = certifi.where()

class NetworkDataExtract:
    def csv_to_json_converter(self, file_path):
        try:
            df = pd.read_csv(file_path)
            df.reset_index(drop=True, inplace=True)
            return df.to_dict(orient="records")
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def insert_data_mongodb(self, records, database, collection):
        try:
            client = pymongo.MongoClient(MONGO_DB_URL, tlsCAFile=ca)
            db = client[database]
            col = db[collection]
            result = col.insert_many(records)
            return len(result.inserted_ids)
        except Exception as e:
            raise NetworkSecurityException(e, sys)

if __name__ == "__main__":
    file_path = "/Users/yasjudanulislam/Documents/MLOps/networksecurity/Network_Data/phisingData.csv"
    database = "TESTDB"
    collection = "NetworkData"

    networkobj = NetworkDataExtract()
    records = networkobj.csv_to_json_converter(file_path)
    count = networkobj.insert_data_mongodb(records, database, collection)
    print(count)
