import boto3
import json
from boto3.dynamodb.conditions import Key
from os import getenv
from uuid import uuid4

region_name = getenv('APP_REGION')

character_table = boto3.resource(
    'dynamodb',
    region_name=region_name
    ).Table('Character')
    
def lambda_handler(event, context):
    name = event['Name']
    available = event['Available']
    performer = event['Performer']
    id= str(uuid4())
    
    character_table.put_item(Item={
        'Id': id,
        'Name': name,
        'Available': available,
        'Performer': performer
    })

    return response(200,{
        'Id': id,
        'Name': name,
        'Available': available,
        'Performer': performer
    })
def response(code, body):
    return {
        "statusCode": code,
        "headers": {
            "Content-Type": "application/json"
            },
        "body": json.dumps(body)
    }