import logging
import boto3
from botocore.exceptions import ClientError
import os
import io
from PIL import Image

BUCKET = {
    "service": "s3",
    "name": "yns-profile",
    "region": "us-east-2",
    "domain": "amazonaws.com",
    "sizes": [[100, 100], [400, 400], [720, 720]]
}

def upload_file(img, username):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """
    file_name = '{}-profile'.format(username)
    format = 'webp'
    # Upload the file
    s3_client = boto3.client(
        service_name = BUCKET["service"],
        endpoint_url = 'https://{}.{}.{}.{}/'.format(BUCKET["name"], BUCKET["service"], BUCKET["region"], BUCKET["domain"]), 
    )
    try:
        img = Image.open(img)
        for size in BUCKET['sizes']:
            buffer = io.BytesIO()
            img.thumbnail((size[0],size[1]))
            img.save('/Users/libardovega/{}{}.{}'.format(file_name,size[0],format), format, quality=60)
            buffer.seek(0) # rewind pointer back to start
            """ s3_client.put_object(
                ACL = 'public-read',
                Body = buffer,
                Bucket = '{}x{}'.format(size[0], size[1]),
                Key = '{}.{}'.format(file_name, format),
                ContentType = 'media-type',
            ) """
            buffer.close()
            del buffer
        img.close()
    except ClientError as e:
        logging.error(e)
        return False
    return True