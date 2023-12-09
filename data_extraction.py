import pandas as pd
import psycopg2
from sqlalchemy import text


class DataExtractor: 
    
    def read_rds_table(self, databaseconnector, table_name):
        engine = databaseconnector.init_db_engine()
        with engine.connect() as connection:
           users_table = pd.DataFrame(connection.execute(text(f'select * from {table_name}')))
        return users_table