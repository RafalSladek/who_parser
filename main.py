from datetime import datetime

from callWHODataAPI import WHODataAPI
from s3Upload import S3Uploader


def print_list(collection):
    for item in collection:
        print(item)


s3_uploader = S3Uploader(WHODataAPI())

all_buckets = s3_uploader.get_all_buckets()

print_list(all_buckets)

response = s3_uploader.apiClient.get_who_dimensions()

myBucket = s3_uploader.get_target_bucket()
timestamp = int(datetime.now().timestamp())
print(timestamp)

myBucket.put_object(Key=('dimensions_' + str(timestamp) + '.json'), Body=response)

all_object = s3_uploader.get_all_objects_from_bucket(myBucket)
print_list(all_object)
