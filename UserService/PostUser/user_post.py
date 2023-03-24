import boto3
import json
from boto3.dynamodb.conditions import Key
from os import getenv
from uuid import uuid4

region_name = getenv('APP_REGION')

user_table = boto3.resource(
    'dynamodb',
    region_name=region_name
    ).Table('TodoAuthUsers')
    
def lambda_handler(event, context):
    username = event['username']
    password = event['password']
    id= str(uuid4())
    
    user_table.put_item(Item={
        'username': username,
        'Id': id,
        'password': password
        
    })

    return response(200,{
        'username': username,
        'Id': id,
        'password': password
    })
def response(code, body):
    return {
        "statusCode": code,
        "headers": {
            "Content-Type": "application/json"
            },
        "body": json.dumps(body)
    }