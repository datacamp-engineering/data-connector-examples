# DataCamp Data Connector example scripts

This is a small collection of scripts that show several approaches how you can 
connect to the Data Connector using Python and run any analysis on the data.

## Authentication

For convenience all authentication credentials are stored in the CREDENTIALS.py
file. The file itself contains instructions where to fetch your private 
credentials.

## Libraries

The example scripts cover using the dcdcpy and pyathena libraries.

### [dcdcpy](https://github.com/datacamp/dcdcpy)
This is a python library created by DataCamp specifically for use with the 
Data Connector and can be used to easily access all the tables using an
SDK style approach. 

⚠️ Make sure you have installed dcdcpy as documented on our official
github repository https://github.com/datacamp/dcdcpy 

See the following example scripts
- course_activity_for_user.py
- list_all_users.py

### [pyathena](https://pypi.org/project/pyathena/)
This is a open source python library used to connect to the Athena REST API
and execute queries against it's database. This is very useful if you prefer
to execute raw SQL queries instead of using a Python SDK like dcdcpy.

⚠️ Make sure you have installed pyathena using `pip install PyAthena` before
running the scripts that use pyathena!

See the following example scripts
- athena.py