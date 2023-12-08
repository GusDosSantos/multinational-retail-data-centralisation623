import yaml
from sqlalchemy import create_engine
from sqlalchemy import inspect

class DatabaseConnector: 
    def credentials(self):
        with open('db_creds.yaml', 'r') as yaml_file:
            yaml_data = yaml.safe_load(yaml_file)
            print("YAML FILE LOADED IN DICTIONARY:" + yaml_data)
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
        engine = create_engine(f"{database_type}+{database_API}://{database_user}:{database_password}@{database_host}:{database_port}/{database_database}")



    def list_db_tables(self):
        engine = self.init_db_engine()
        inspector = inspect(engine)
        print(inspector.get_table_names())
        
        
        




