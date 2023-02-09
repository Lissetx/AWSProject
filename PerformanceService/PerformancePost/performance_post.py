import boto3
import json
from boto3.dynamodb.conditions import Key
from os import getenv
from uuid import uuid4

region_name = getenv('APP_REGION')

performance_table = boto3.resource(
    'dynamodb',
    region_name=region_name
    ).Table('Performance')
    
def lambda_handler(event, context):
    title = event['Title']
    director = event['Director']
    casting_director = event['CastingDirector']
    venue = event['Venue']
    performance_date = event['PerformanceDate']
    performers = event['Performers']
    characters = event['Characters']
    auditoners = event['Auditioners']
    status = event['Status'] #open or closed
    id= str(uuid4())
    
    performance_table.put_item(Item={
        'Id': id,
        'Title': title,
        'Director': director,
        'CastingDirector': casting_director,
        'Venue': venue,
        'PerformanceDate': performance_date,
        'Performers': performers,
        'Characters': characters,
        'Auditioners': auditoners,
        'Status': status
        
    })

    return response(200,{
        'Id': id,
        'Title': title,
        'Director': director,
        'CastingDirector': casting_director,
        'Venue': venue,
        'PerformanceDate': performance_date,
        'Performers': performers,
        'Characters': characters,
        'Auditioners': auditoners,
        'Status': status
    })
def response(code, body):
    return {
        "statusCode": code,
        "headers": {
            "Content-Type": "application/json"
            },
        "body": json.dumps(body)
    }