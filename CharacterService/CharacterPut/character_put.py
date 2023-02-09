import boto3
import json
from boto3.dynamodb.conditions import Key
from os import getenv
from uuid import uuid4

region_name = getenv('APP_REGION')
character_table = boto3.resource('dynamodb', region_name=region_name).Table('Character')

def lambda_handler(event, context):
    id = event['Id']
    name = event['Name'] 
    available = event['Available']
    performer = event['Performer']

    if id is not event:
        response(400, "Id is required")
        
        
    character = character_table.get_item(Key={"Id":id})["Item"]

    if character is None:
        response(404, "Character not found")
    
    if name is not None:
        character['Name'] = name
    if available is not None:
        character['Available'] = available
    if performer is not None:
        character['Performer'] = performer
    
    character_table.put_item(Item=character)
    return response(200, character)
    
def response(code, body):
    return{
        "statusCode": code,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps(body)
    }