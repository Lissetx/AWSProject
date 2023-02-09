import boto3
import json
from boto3.dynamodb.conditions import Key
from os import getenv
from uuid import uuid4

region_name = getenv('APP_REGION')
performance_table = boto3.resource('dynamodb', region_name=region_name).Table('Performance')

def lambda_handler(event, context):
    id = event['Id']
    title = event['Title']
    director = event['Director']
    casting_director = event['CastingDirector']
    venue = event['Venue']
    performance_date = event['PerformanceDate']
    characters = event['Characters']
    auditioners = event['Auditioners']
    status = event['Status'] #open or closed

    if id is not event:
        response(400, "Id is required")
    
    performance = performance_table.get_item(Key={"Id":id})["Item"]
    
    if performance is None:
        response(404, "Performance not found")
    
    if title is not None:
        performance['Title'] = title
    if director is not None:
        performance['Director'] = director
    if casting_director is not None:
        performance['CastingDirector'] = casting_director
    if venue is not None:
        performance['Venue'] = venue
    if performance_date is not None:
        performance['PerformanceDate'] = performance_date
    if characters is not None:
        performance['Characters'] = characters
    if auditioners is not None:
        performance['Auditioners'] = auditioners
    if status is not None:
        performance['Status'] = status
        
    performance_table.put_item(Item=performance)
    return response(200, performance)

def response(code, body):
    return{
        "statusCode": code,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps(body)
    }