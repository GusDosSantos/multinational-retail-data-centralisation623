# Multinational Retail Data Centralisation Project

This project aimed to develop a program that can collect data from multiple sources for an international retail client. This includes data such as order data, user data, store data and more. The data must be extracted, cleaned, and then added to a database so that it may be used by the client to analyse and garner actionable insights.

## Motivation
- Due to the complexity and variety of data sources, the program’s development would improve one’s practical ability to work with and clean all types of data and develop schemas while also allowing an understanding of the data flow.
- This process also would improve one’s technical knowledge of Python, including a wide range of libraries, SQL and use of several tools such as Git Bash, GitHub, PgAdmin and AWS.

## Data Sources
This client has data spread across multiple sources and in different formats. These include:
- Order data from an AWS RDS Database.
- User data from an AWS RDS Database.
- Credit Card data from a PDF stored in an AWS S3 Bucket.
- Store Data collected from an API service on AWS.
- Product data from a CSV File in an AWS S3 Bucket.
- Event data from CSV File in an AWS S3 Bucket.


## File Structure

### There are four main scripts, each with a respective purpose:

1. ### Data_extraction.py
2. ### Data_cleaning.py
3. ### Database_utils.py
4. ### Main.py

##

### Data_extraction.py
This script is responsible for extracting the data from the variety of data sources. It is composed of a class: DataExtractor. This class contains functions for extracting the data from each of the data sources.

### Data_cleaning.py
This script is responsible for cleaning the data that is extracted from the source. This is so that the data can be input on to the client database in a suitable format while removing any null or wrong values. This script is composed of a main class: DataCleaning. This class contains functions to clean the data from each of the sources once extracted.

### Database_utils.py
This class is responsible for providing a connection to the local client database, uploading cleaned data and other utility functions. It consists of a class called DatabaseConnector and has functions such as init_db_engine which initiates a connection for the creation of tables. 

### Main.py
This script is what instantiates all the other classes and allows for the extracting, cleaning and uploading of the data. There is a try block for each of the data sources, where it will attempt to extract, clean and upload that piece of table. 


## Usage

- A basic understanding of Python would be necessary to run and use this program.
- Install each of the files and folders within this repo and download locally into a folder of your choice.
- Use pip/conda to install any of the libraries & modules specified within the script imports as these are necessary for the program to function.
- Create the following yaml files:
    1. **db_creds.yaml (RDS_HOST, RDS_PASSWORD, RDS_USER, RDS_DATABASE, RDS_PORT)** - This file stores the necessary values for connection to the aws relational database.
    2. **local_creds.yaml (LOCAL_PASSWORD, DATABASE_NAME)** - This file stores the root password and the database name to connect/upload to on your local postgres server.
    3. **s3_keys.yaml (ACCESS, SECRET)** - This file stores the access and secret key for the IAM user to allow for a connection to the AWS S3 Bucket. Make sure that AWS is configured in the command line when attempting to extract data from the bucket. It is also important to note that the user must have S3 permissions on the account.
- With these yaml files filled appropriately, the program can now be ran in order to extract, clean and upload the data from the various sources into your local postgres database.
- The scripts can be modified to extract data from other types of sources, although this would require changes to the cleaning according to both the values within the source data as well as the end specification.



