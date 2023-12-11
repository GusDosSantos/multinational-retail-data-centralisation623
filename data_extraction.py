import pandas as pd
from sqlalchemy import text
import json
import tabula
import requests
import boto3
import fsspec
import yaml
from database_utils import DatabaseConnector

class DataExtractor:
    def __init__(self):
        self.pdf ='https://data-handling-public.s3.eu-west-1.amazonaws.com/card_details.pdf'
        self.key_dict = {"x-api-key":"yFBQbwXe9J3sd6zWVAMrK6lcxxr0q1lr2PT6DDMX"}
        self.store_count = self.list_number_of_stores('https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/number_stores')
        with open('db_creds.yaml', 'r') as yaml_file:
            self.aws_keys = yaml.safe_load(yaml_file)
        

    
    def read_rds_table(self, databaseconnector, table_name):
        engine = databaseconnector.init_db_engine()
        with engine.connect() as connection:
           table = pd.DataFrame(connection.execute(text(f'select * from {table_name}')))
           print(table)
        return table
    
    def retrieve_pdf_data(self):
        tabula.convert_into(self.pdf, "new_output.csv", output_format="csv", pages='all')
        self.card_df = pd.read_csv('new_output.csv') 
        print(self.card_df)
        return self.card_df
    
    def list_number_of_stores(self, num_stores_endpoint):
        number_of_stores = requests.get(num_stores_endpoint, headers = self.key_dict)
        self.num_of_stores = number_of_stores
        print(number_of_stores.json()['number_stores'],"Stores Retrieved")
        return number_of_stores.json()['number_stores']
    
    def retrieve_stores_data(self):
        stores = []
        for store_number in range(self.store_count):
            store = requests.get(f'https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/store_details/{store_number}', headers = self.key_dict)
            store = store.json()
            stores.append(store)
        df = pd.DataFrame(stores, index = range(0, (len(stores))))
        #print(df)
        return df
    
    #def extract_from_s3(self): #PRODUCTS DATA #AWS account is not working currently, currently awaiting support email 
        client = boto3.client('s3',aws_access_key_id= self.aws_keys['Access key ID'], aws_secret_access_key=self.aws_keys['Secret access key'])
        csv_object = client.get_object(Bucket = 'data-handling-public', Key = 'products.csv' )['Body']
        csv_object = csv_object.read().decode('utf-8')
        from io import StringIO
        df_product_details = pd.read_csv(StringIO(csv_object))
        return df_product_details
    
    #def extract_from_json(self): #DATE EVENTS DATA #AWS account is not working currently, currently awaiting support email 





    


#dc = DatabaseConnector()   #Extract table test
#extractor = DataExtractor()
#table_data = extractor.read_rds_table(dc, 'orders_table')

#extractor = DataExtractor()    #PDF extraction Test
# extractor.retrieve_pdf_data()


#extractor = DataExtractor()    #API Extraction test
#extractor.list_number_of_stores('https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/number_stores')
#extractor.retrieve_stores_data()

