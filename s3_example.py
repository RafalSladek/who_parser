import boto3

s3 = boto3.resource('s3')
# parser is collecting and return article content#
s3.Bucket('who-parsed-articles').put_object(Key='article-001.json', Body=article_content)

#  multithreading processing can be used to optimized speed



for bucket in s3.buckets.all():
    print(bucket.name)