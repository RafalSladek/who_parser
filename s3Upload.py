import boto3

from callWHODataAPI import WHODataAPI


class S3Uploader:
    def __init__(self, api_client: WHODataAPI):
        self.s3Client = boto3.resource('s3')
        self.s3TargetBucketName = 'who-parsed-articles'
        self.apiClient = api_client

    def get_all_buckets(self):
        return self.s3Client.buckets.all()

    def get_bucket(self, bucket_name):
        return self.s3Client.Bucket(bucket_name)

    def get_target_bucket(self):
        return self.get_bucket(self.s3TargetBucketName)

    def get_all_objects_from_bucket(self, bucket):
        return bucket.objects.all()
