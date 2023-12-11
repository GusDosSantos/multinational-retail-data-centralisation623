import yaml
import pandas as pd
import psycopg2
from sqlalchemy import create_engine, inspect
from sqlalchemy.exc import OperationalError

class DatabaseConnector:
    def __init__(self):
        self.engine = self.init_db_engine()
        self.inspector = inspect(self.engine)

    def credentials(self):
        with open('db_creds.yaml', 'r') as yaml_file:
            yaml_data = yaml.safe_load(yaml_file)
            print("YAML file loaded in dictiionary:", yaml_data)
            return yaml_data

    def local_credentials(self):
        with open('local_creds.yaml', 'r') as yaml_file:
            yaml_data = yaml.safe_load(yaml_file)
            return yaml_data


    def init_db_engine(self):
        credentials = self.credentials()
        database_type = 'postgresql'
        database_API = 'psycopg2'
        database_password = credentials['RDS_PASSWORD']
        database_user = credentials['RDS_USER']
        database_host = credentials['RDS_HOST']
        database_database = credentials['RDS_DATABASE']
        database_port = credentials['RDS_PORT']

        connection_string = f"{database_type}+{database_API}://{database_user}:{database_password}@{database_host}:{database_port}/{database_database}"
        try:
            engine = create_engine(connection_string)
            return engine
        except OperationalError as e:
            print(f"Error connecting to the database: {e}")
            return None
        

    def upload_to_db(self, db_clean):
            local_creds = self.local_credentials()
            self.local_type ='postgresql'
            self.local_api ='psycopg2'
            self.local_host = 'localhost'
            self.local_password = local_creds['LOCAL_PASSWORD']
            self.local_user = 'postgres'
            self.local_database = 'sales_data'
            self.local_port = '5432'
            self.tosql = create_engine(f"{self.local_type}+{self.local_api}://{self.local_user}:{self.local_password}@{self.local_host}:{self.local_port}/{self.local_database}")
            db_clean.to_sql('order_table',self.tosql, if_exists = 'replace')

    def list_db_tables(self):
        print(self.inspector.get_table_names())


#data_connector = DatabaseConnector()   #List Tables 
#data_connector.list_db_tables()




