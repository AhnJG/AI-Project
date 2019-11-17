from __future__ import print_function

import urllib
import os
import subprocess
import boto3


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
LIB_DIR = os.path.join(SCRIPT_DIR, 'lib')

def downloadFromS3(strBucket,strKey,strFile):
    s3_client = boto3.client('s3')
    s3_client.download_file(strBucket, strKey, strFile)

def write_db(file_name, result):
    dynamo_client = boto3.client(
        'dynamodb',
#        aws_access_key_id=ACCESS_KEY,
#        aws_secret_access_key=SECRET_KEY,
        region_name='ap-northeast-2' # DynamoDB는 리전 이름이 필요합니다.
    )
    
    dynamo_client.put_item(
        TableName='flxr', # DynamoDB의 Table이름
        Item={
            'filename': {
                'S': file_name,
            },
            'predicts': result,
        }
    )

def handler(event, context):
    try:
        img_file_path = '/tmp/atv_rider.jpg'
#        if ('imagelink' in event):
#          urllib.urlretrieve(event['imagelink'], imgfilepath)
#        else:
        bucket_name = 'flxr-yolo'
        key = event['Records'][0]['s3']['object']['key']
        
        downloadFromS3(bucket_name,key,img_file_path)
        print(img_file_path)
        
        weight_key = 'weight/yolov3_4000.weights'
        weight_file_path = '/tmp/yolov3_4000.weights'
        
        downloadFromS3(bucket_name, weight_key, weight_file_path)
        print(weight_file_path)

        command = './darknet detect cfg/yolov3.cfg {} {}'.format(
            weight_file_path,
            img_file_path
        )
        print(command)

        try:
            print('Start')
            output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
            print('Finish')
            print(output)
        except subprocess.CalledProcessError as e:
            print('Error')
            print(e.output)
            
        write_db(key, output)
        
    except Exception as e:
        print('Error e')
        print(e)
        raise e
    return 0 
