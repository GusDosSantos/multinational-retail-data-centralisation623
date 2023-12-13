import pandas as pd
import numpy as np
import yaml
import data_extraction, database_utils


class DataCleaning:
    def __init__(self):
        self.extractor = data_extraction.DataExtractor()   
        self.connector = database_utils.DatabaseConnector()


    def get_from_aws(self, table_name):
        df = self.extractor.read_rds_table(self.connector, table_name)
        return df

    def get_pdf_data(self):
        df = self.extractor.retrieve_pdf_data()
        return df
    
    def get_api_data(self):
        df = self.extractor.retrieve_stores_data()
        return df
    
    def get_s3_data(self):
        df = self.extractor.extract_from_s3()
        return df
    
    def get_json_data(self):
        df = self.extractor.extract_json_data()
        return df


    def clean_user_data(self):
        df = self.get_from_aws('legacy_users')
        user_id_duplicates = df[df['user_uuid'].duplicated(keep='first')==True]
        df = df.drop(user_id_duplicates.index)
        df_dob_filter = df[df['date_of_birth'].str.contains('.*-+|/+.*') == False]['date_of_birth']
        df_dob_filter = df_dob_filter[df_dob_filter.str.isupper()==True]
        df = df.drop(df_dob_filter.index)
        df['phone_number'] = df['phone_number'].str.replace('[()\-x\s.,]','',regex=True)
        df['phone_number'] = df['phone_number'].str.replace('+','',regex=False)
        df['country_code'] = df['country_code'].str.replace('GGB','GB')
        df[['country_code','country']] = df[['country_code','country']].astype('category')
        df['address'] = df['address'].str.replace(r'\n',' ',regex=True)
        to_string_cols = df.iloc[:, np.r_[1:3,4:10,11]]
        df[to_string_cols.columns] = to_string_cols.astype('string')
        df = df.drop('index', axis=1)
        df = df.reset_index(drop=True)
        #print(df)
        return df
    
    
    def clean_card_data(self):   
        df = self.get_pdf_data()
        df['date_payment_confirmed'] = pd.to_datetime(df['date_payment_confirmed'], infer_datetime_format=True, errors='coerce')
        df=df.dropna()
        df['card_number'] = df['card_number'].astype('string')
        df['card_number'] = df['card_number'].str.replace('?', '')
        df['card_provider'] = df['card_provider'].astype('category')

        #print(df)
        return df


    def clean_store_data(self):

        df = self.get_api_data()
        df = df[df['index'] != 447]
        df['latitude'].fillna(0, inplace=True)
        df['longitude'].fillna(0, inplace=True)
        df['locality'].fillna('Unknown', inplace=True)
        df['country_code'].fillna('Unknown', inplace=True)
        df['continent'] = df['continent'].str.replace('ee', '')
        df['opening_date'] = pd.to_datetime(df['opening_date'], format="%Y-%m-%d", errors='coerce')
        df['staff_numbers'] = pd.to_numeric(df['staff_numbers'], errors='coerce')
        df['staff_numbers'].fillna(0, inplace=True)
        df['staff_numbers'] = df['staff_numbers'].astype('int')
        return df


    def clean_orders_data(self):
        df = self.get_from_aws('orders_table')
        df = df.drop(['first_name', 'last_name', '1', 'index'], axis=1)
        df['product_quantity'] = df['product_quantity'].astype('category')
        to_string_cols = ['date_uuid', 'user_uuid', 'store_code', 'product_code', 'card_number']
        df[to_string_cols] = df[to_string_cols].astype('string')
        # Reset index
        df = df.reset_index(drop=True)

        return df
    


    def convert_product_weights(self):
        df = self.get_s3_data().dropna(subset=['weight'])

        df['weight'] = df['weight'].str.replace(' x ', '*').str.replace('kg', ' k').str.replace('g', ' g').str.replace('ml', ' ml').str.replace('oz', ' oz')
        df[['Weight(kg)', 'Units']] = df['weight'].str.split(" ", n=1, expand=True)
        df['date_added'] = pd.to_datetime(df['date_added'], infer_datetime_format=True, errors='coerce')
        df['Weight(kg)'] = pd.to_numeric(df['Weight(kg)'], errors='coerce').round(3)
        df['Units'] = df['Units'].str.replace('.', '').str.replace(' ', '')
        df[['m1', 'm2']] = df['weight'].str.split("*", n=1, expand=True)
        df['m2'] = df['m2'].str.replace('g', '')
        for weight_in_kg in df.index:
            if pd.notna(df.at[weight_in_kg, 'weight']) and '*' in df.at[weight_in_kg, 'weight']:
                df.at[weight_in_kg, 'Weight(kg)'] = pd.to_numeric(df.at[weight_in_kg, 'm1'], errors='coerce') * pd.to_numeric(df.at[weight_in_kg, 'm2'], errors='coerce')
        for weight_in_kg in df.index:
            if pd.notna(df.at[weight_in_kg, 'Units']) and df.at[weight_in_kg, 'Units'] == 'g':
                df.at[weight_in_kg, 'Weight(kg)'] /= 1000
        for weight_in_kg in df.index:
            if pd.notna(df.at[weight_in_kg, 'Units']) and df.at[weight_in_kg, 'Units'] == 'ml':
                df.at[weight_in_kg, 'Weight(kg)'] /= 1000
        for weight_in_kg in df.index:
            if pd.notna(df.at[weight_in_kg, 'Units']) and df.at[weight_in_kg, 'Units'] == 'oz':
                df.at[weight_in_kg, 'Weight(kg)'] /= 35.274


        return df
    

    def clean_date_data(self):
        df = self.get_json_data()
        for row in df.index:
            if df.loc[row, 'day'] == 'NULL':
                df.drop(row, inplace=True)
        df['month'] = pd.to_numeric(df['month'], errors='coerce')
        df = df.dropna()
        df['month'] = df['month'].astype(np.int64)
        print("AFTER")
        #print(df)
        return df



#data_clean = DataCleaning()           User Cleaning Test
#df = data_clean.get_from_aws('legacy_users')
#data_clean.clean_user_data(df)


#data_clean = DataCleaning()          #Card detail clean test
# df = data_clean.clean_card_data()

#data_clean = DataCleaning()    #Store data clean test
#data_clean.clean_date_data()


#data_clean = DataCleaning()
#data_clean.clean_orders_data()
