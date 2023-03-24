import boto3
import json
import uuid
from boto3.dynamodb.conditions import Key
from os import getenv
from uuid import uuid4

region_name = getenv('APP_REGION')

performer_table = boto3.resource(
    'dynamodb',
    region_name=region_name
    ).Table('Performer')
        
def lambda_handler(event, context):
    id = event['Id']
    name = event['Name']
    email = event['Email']
    phone = event['Phone']
    past_performances = event['PastPerformances']
    current_performances = event['CurrentPerformances']
    
    if id is not event:
        response(400, "Id is required")
    
    performer = performer_table.get_item(Key={"Id":id})["Item"]
    
    if performer is None:
        response(404, "Performer not found")
    
    if name is not None:
        performer['Name'] = name
    if email is not None:
        performer['Email'] = email
    if phone is not None:
        performer['Phone'] = phone
    if past_performances is not None:
        performer['PastPerformances'] = past_performances
    if current_performances is not None:
        performer['CurrentPerformances'] = current_performances
        
    performer_table.put_item(Item=performer)
    return response(200, performer)
    
    
def response(code, body):
    return {
        "statusCode": code,
        "headers": {
            "Content-Type": "application/json"
            },
        "body": json.dumps(body)
    }