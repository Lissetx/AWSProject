import boto3
import json
from boto3.dynamodb.conditions import Attr, Key
from os import getenv

region_name = getenv('APP_REGION')
director_table = boto3.resource('dynamodb', region_name=region_name).Table('Director')

def lambda_handler(event, context):
    path = event["pathParameters"]
    
    if path is not None and "id" in path:
        output = director_table.delete_item(Key={"Id":path["id"]})
    
        return response(200, output)
    return response(400, "Bad Request")

def response(code, body):
    return{
        "statusCode": code,
        "headers": {
            "Content-Type": "application/json"
    },
        "body": json.dumps(body)
    }