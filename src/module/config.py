import boto3

# the following could be anything, it will not be actually run at prefect deploy time
region_name = "us-east-1"
aws_access_key_id = "***"
aws_secret_access_key = "***"

aws_session = boto3.session.Session(
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=region_name,
)
