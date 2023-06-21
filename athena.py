'''
This script uses the pyathena library to connect to the athena database
which enables you to execute raw SQL queries against the datacamp dataconnector.
For information on the database schema see https://enterprise-docs.datacamp.com/
'''
from pyathena import connect
from CREDENTIALS import *

ATHENA_SCHEMA = DC_AWS_BUCKET.replace("-production", "").replace("-", "_")

cursor = connect(
    aws_access_key_id = DC_AWS_ACCESS_KEY_ID,
    aws_secret_access_key = DC_AWS_SECRET_ACCESS_KEY,
    s3_staging_dir = f"s3://{DC_AWS_BUCKET}/tmp-tableau/athena/",
    region_name = DC_AWS_DEFAULT_REGION
).cursor()

cursor.execute(f"""
SELECT email, first_name, last_name
FROM {ATHENA_SCHEMA}.user_dim
""")
for row in cursor:
    print(row)

