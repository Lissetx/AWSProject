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

performer_table = boto3.resource(
    'dynamodb',
    region_name=region_name
    ).Table('Performer')

def lambda_handler(event, context):
    #take performer id and find performance by id and add performer id to auditioners
    performer_id = event['PerformerId']
    id = str(uuid4())
    path = event["pathParameters"]
    
    if path is not None and "id" in path:
        performance_table.insert_item(Key={"id":path["id"]}, UpdateExpression="set #p = :p", ExpressionAttributeNames={"#p": "auditioners"}, ExpressionAttributeValues={":p": performer_id})
        return response(200, performance_table.get_item(Key={"id":path["id"]})["Item"])
    
    return response(200, {
        'Auditioners': performer_id
    })
    
def response(code, body):
    return{
        "statusCode": code,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps(body)
    }