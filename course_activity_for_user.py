'''
This script uses the datacamp python library dcdcpy to query the
datacamp dataconnector and return all course activity for a single user
including the course title, time spent in seconds and date of activity.
'''
from dcdcpy.dcdcpy import DataConnector
from CREDENTIALS import *
import os

# See https://enterprise-docs.datacamp.com/data-connector/getting-started/your-credentials
os.environ["AWS_BUCKET"] = DC_AWS_BUCKET
os.environ["AWS_ACCESS_KEY_ID"] = DC_AWS_ACCESS_KEY_ID
os.environ["AWS_SECRET_ACCESS_KEY"] = DC_AWS_SECRET_ACCESS_KEY
os.environ["AWS_DEFAULT_REGION"] = DC_AWS_DEFAULT_REGION

# Replace this with the email of the user you want to query
USER_EMAIL = 'john.doe@acme.com'

# Instantiate library
dc = DataConnector()

# Query and merge data
course_facts = dc.course_fact()
course_facts = course_facts \
    .merge(dc.course_dim(), left_on="course_id", right_on="course_id") \
    .merge(dc.user_dim(), left_on="user_id", right_on="user_id") \

# Filter out single user
course_facts = course_facts[course_facts['email'] == USER_EMAIL]

# Output data
print(course_facts[['course_id', 'title', 'time_spent', 'date_id']])