import boto3
from moto import mock_s3


@mock_s3
def test():
    S3_BUCKET = "bucket_name"
    S3_PREFIX = "signal/.hoodie"

    s3 = boto3.client("s3", region_name="us-east-1")
    s3.create_bucket(Bucket=S3_BUCKET)
    s3_mock_body_value = "1".encode()
    s3.put_object(Bucket=S3_BUCKET, Key=f"{S3_PREFIX}/1.commit", Body=s3_mock_body_value)
    
    lov2 = s3.list_objects_v2(Bucket=S3_BUCKET, Prefix=S3_PREFIX)
    print(lov2)

    if 'Contents' in lov2:
        print(True)
    else:
        print(False)

