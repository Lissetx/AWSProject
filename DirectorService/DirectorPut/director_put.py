import boto3
import json
from boto3.dynamodb.conditions import Key
from os import getenv
from uuid import uuid4

region_name = getenv('APP_REGION')
director_table = boto3.resource('dynamodb', region_name=region_name).Table('Director')

def lambda_handler(event, context):
    
    id = event['Id']
    name = event['Name']
    email = event['Email']
    phone = event['Phone']
    castingdirector = event['CastingDirector']
    
    
    if id is not event:
        response(400, "Id is required")

    director = director_table.get_item(Key={"Id":id})["Item"]
    
    if director is None:
        response(404, "Director not found")
    
    if name is not None:
        director['Name'] = name
    if email is not None:
        director['Email'] = email
    if phone is not None:
        director['Phone'] = phone
    if castingdirector is not None:
        director['CastingDirector'] = castingdirector
        

    #if id not event  response needs id
    #get_item 
    #if get in object empty 404 not found 
    #object['name'] = event['name']
    #table.put_item(Item=object)
    
    director_table.put_item(Item=director)
    return response(200, director)
    
def response(code, body):
    return{
        "statusCode": code,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps(body)
    }