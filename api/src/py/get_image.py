import boto3, re, json

def parse_s3_url(url):
    # returns bucket_name, region, key

    bucket_name = None
    region = None
    key = None

    # http://bucket.s3.amazonaws.com/key1/key2
    match = re.search('^https?://([^.]+).s3.amazonaws.com(.*?)$', url)
    if match:
        bucket_name, key = match.group(1), match.group(2)

    # http://bucket.s3-aws-region.amazonaws.com/key1/key2
    match = re.search('^https?://([^.]+).s3-([^\.]+).amazonaws.com(.*?)$', url)
    if match:
        bucket_name, region, key = match.group(1), match.group(2), match.group(3)

    # http://s3.amazonaws.com/bucket/key1/key2
    match = re.search('^https?://s3.amazonaws.com/([^\/]+)(.*?)$', url)
    if match:
        bucket_name, key = match.group(1), match.group(2)

    # http://s3-aws-region.amazonaws.com/bucket/key1/key2
    match = re.search('^https?://s3-([^.]+).amazonaws.com/([^\/]+)(.*?)$', url)
    if match:
        bucket_name, region, key = match.group(2), match.group(1), match.group(3)

    return list( map(lambda x: x.strip('/') if x else None, [bucket_name, region, key] ) )

def get_image(url):
    s3 = boto3.client('s3')

    bucket = parse_s3_url(url_doc)[0]
    key = parse_s3_url(url_doc)[2]

    img = s3.get_object(Bucket=bucket,Key=key)['Body'].read()

    return img