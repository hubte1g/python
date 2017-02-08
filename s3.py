# your_project/users.py
import Pillow

def thumbnailer(event, context):
    """ Upon PUT, thumbnail! """

    # Get the bytes from S3
    in_bucket = event['Records']['s3']['bucket']['name']
    key = event['Records']['s3']['object']['key']
    image_bytes = s3_client.download_file(in_bucket, key, '/tmp/' + key).read()

    # Thumbnail it
    size = (250, 250)
    thumb = ImageOps.fit(image_bytes, size, Image.ANTIALIAS)

    # Put it back on S3
    s3_client.put_object(
        ACL='public-read',
        Body=thumb,
        Key=key + 'thumbnail.jpg',
        Bucket='avatar-bucket')
