import boto3
import json
from boto3.dynamodb.conditions import Key
from os import getenv
from uuid import uuid4

region_name = getenv('APP_REGION')
performance_table = boto3.resource('dynamodb', region_name=region_name).Table('Performance')
performer_table = boto3.resource('dynamodb', region_name=region_name).Table('Performer')

def lambda_handler(event, context):
    performerid = event['PerformerId']

    id = str(uuid4())
    if "pathParameters" not in event or "queryStringParameters" not in event:
        return response(400, {"message":"missing request data"})
    
    path = event["pathParameters"]

    if path is not None and "id" in path:
        #check which fields are being updated
        if performerid is not None:
            performance_table.insert_item(Key={"id":path["id"]}, UpdateExpression="set #p = :p", ExpressionAttributeNames={"#p": "performers"}, ExpressionAttributeValues={":p": performerid})
            #add performance id to performer current performances list
            performer_table.insert_item(Key={"id":performerid}, UpdateExpression="set #p = :p", ExpressionAttributeNames={"#p": "currentperformances"}, ExpressionAttributeValues={":p": path["id"]})
        return response(200, performance_table.get_item(Key={"id":path["id"]})["Item"])
    

    
    return response(200, {
        'Message': "Performer added to performance"
        
    })
    
def response(code, body):
    return{
        "statusCode": code,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps(body)
    }