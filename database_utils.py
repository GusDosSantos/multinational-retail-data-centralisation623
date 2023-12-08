import yaml
from sqlalchemy import create_engine
from sqlalchemy import inspect

class DatabaseConnector: 
    def read_db_creds(self):
        with open('db_creds.yaml', 'r') as yaml_file:
            data = yaml.safe_load(yaml_file)
            return data