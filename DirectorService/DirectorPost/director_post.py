import boto3
import json
import uuid
from boto3.dynamodb.conditions import Key
from os import getenv
from uuid import uuid4

region_name = getenv('APP_REGION')

director_table = boto3.resource(
    'dynamodb',
    region_name=region_name
    ).Table('Director')

director_auth_table = boto3.resource(
    'dynamodb',
    region_name=region_name).Table('DirectorAuth')
    
def lambda_handler(event, context):
    name = event['Name']
    email = event['Email']
    phone = event['Phone']
    castingdirector = event['CastingDirector']
    username = event['Username']
    password = event['Password']
    
    id= str(uuid4())
    
    director_auth_table.put_item(Item={
        'id':str(uuid.uuid4()),
        'username': username,
        'password': password,
    })
        
    
    director_table.put_item(Item={
        'Id': id,
        'Name': name,
        'Email': email,
        'Phone': phone,
        'CastingDirector': castingdirector
    })

    return response(200,{
        'Id': id,
        'Name': name,
        'Email': email,
        'Phone': phone,
        'CastingDirector': castingdirector,
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