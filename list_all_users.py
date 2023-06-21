'''
This script uses the datacamp python library dcdcpy to query all of the 
users available in the reporting data in your private S3 bucket.
Using the dcdcpy library doesn't require you to download and process the 
files individually but you can directly create dataframes from the "tables" 
as you can see in the script below.
'''
from dcdcpy.dcdcpy import DataConnector
from CREDENTIALS import *
import os

# See https://enterprise-docs.datacamp.com/data-connector/getting-started/your-credentials
os.environ["AWS_BUCKET"] = DC_AWS_BUCKET
os.environ["AWS_ACCESS_KEY_ID"] = DC_AWS_ACCESS_KEY_ID
os.environ["AWS_SECRET_ACCESS_KEY"] = DC_AWS_SECRET_ACCESS_KEY
os.environ["AWS_DEFAULT_REGION"] = DC_AWS_DEFAULT_REGION

dc = DataConnector()

dataframe = dc.user_dim()
print(dataframe['email']);