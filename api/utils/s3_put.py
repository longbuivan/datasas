# import needed libraries
import boto3

# create s3 put object in utils directory
def create_s3_put_object_in_utils_directory(bucket_name, object_name, file_path):
    s3_client = boto3.client('s3')
    s3_client.put_object(
        Bucket=bucket_name,
        Key=object_name,
        Body=open(file_path, 'rb')
    )
    return True

