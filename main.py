# main_file.py

from data_extraction import DataExtractor
from database_utils import DatabaseConnector
from data_cleaning import DataCleaning

def main():
    data_extractor = DataExtractor()
    db_connector = DatabaseConnector()
    data_cleaner = DataCleaning()


    #===ORDERS===
    #try:
       # print("Attempting to load ORDERS to database")
        #cleaned_orders_data = data_cleaner.clean_orders_data()
        #db_connector.upload_to_db(cleaned_orders_data,'orders_table')
        #print("Data transferred.")
    #except Exception as e:
        #print(f"An error occurred: {e}")



    #====USERS====
    #try:
        #print("Attempting to load USERS to database")
        #cleaned_orders_data = data_cleaner.clean_user_data()
        #db_connector.upload_to_db(cleaned_orders_data,'dim_users')
        #print("Data transferred.")
    #except Exception as e:
        #print(f"An error occurred: {e}")


    #===STORES===
    try:
        print("Attempting to load STORES to database")
        cleaned_orders_data = data_cleaner.clean_store_data()
        db_connector.upload_to_db(cleaned_orders_data,'dim_store_details')
        print("Data transferred.")
    except Exception as e:
        print(f"An error occurred: {e}")





if __name__ == "__main__":
    main()
