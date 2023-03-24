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


performer_auth_table = boto3.resource(
    'dynamodb',
    region_name=region_name).Table('TodoAuthUsers')
        
def lambda_handler(event, context):
    name = event['Name']
    email = event['Email']
    phone = event['Phone']
    past_performances = event['PastPerformances']
    current_performances = event['CurrentPerformances']
    username = event['Username']
    password = event['Password']
    
    id= str(uuid4())
    
    performer_table.put_item(Item={
        'Id': id,
        'Name': name,
        'Email': email,
        'Phone': phone,
        'PastPerformances': past_performances,
        'CurrentPerformances': current_performances
        
    })
    
    performer_auth_table.put_item(Item={
        'id':str(uuid.uuid4()),
        'username': username,
        'password': password,
    })

    return response(200,{
        'Id': id,
        'Name': name,
        'Email': email,
        'Phone': phone,
        'PastPerformances': past_performances,
        'CurrentPerformances': current_performances,
        'Username': username,
        'Password': password
    })
def response(code, body):
    return {
        "statusCode": code,
        "headers": {
            "Content-Type": "application/json"
            },
        "body": json.dumps(body)
    }