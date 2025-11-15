import os
import certifi
import json
import sys
import pandas as pd
import numpy as np
import pymongo

from dotenv import load_dotenv
from urllib.parse import quote_plus
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging



ca=certifi.where()
load_dotenv()

username = quote_plus(os.getenv("Mongodb_username"))
password = quote_plus(os.getenv("Mongodb_password"))
mongo_host = os.getenv("Mongo_DB_host")

Mongo_DB_url = f"mongodb+srv://{username}:{password}@{mongo_host}/?appName=Cluster0"

print(Mongo_DB_url)



class NetworDataExtract():

    def __init__(self):
        try:
            pass
        except Exception as e:
            logging.info(f"exception has been raised{NetworkSecurityException(e,sys)}")
            raise NetworkSecurityException(e,sys)
        
    def cv_to_json_convertor(self,file_path):
        try:
            
            data=pd.read_csv(file_path)
            data.reset_index(drop=True,inplace=True)
            logging.info("file path is correct and it can load csv file")
            records=list(json.loads(data.T.to_json()).values())
            return records
            logging.info("it returns the records")
        
        except Exception as e:
            raise NetworkSecurityException(e,sys)
            logging.info(f"exception has been raised{NetworkSecurityException(e,sys)}")

    def insert_data_mongodb(self,records,database,collection):
        try:
            self.mongo_client = pymongo.MongoClient(Mongo_DB_url)

            db = self.mongo_client[database]            # database object
            collection_obj = db[collection]             # collection object

            result = collection_obj.insert_many(records)
            return len(result.inserted_ids)
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        




if __name__=="__main__":
    FILE_PATH="Network_Data\phisingData.csv"
    DATABASE="BHASKAR"
    Collection="NetworkData"
    networkobj=NetworDataExtract()
    records=networkobj.cv_to_json_convertor(file_path=FILE_PATH)
    print(records)
    no_of_records=networkobj.insert_data_mongodb(records,DATABASE,Collection)
    print(no_of_records)