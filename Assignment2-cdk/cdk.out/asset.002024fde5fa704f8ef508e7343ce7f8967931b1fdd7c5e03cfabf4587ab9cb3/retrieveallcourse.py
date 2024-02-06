import json
import boto3

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('KnowledgeCatalog')

    data = table.scan(FilterExpression = boto3.dynamodb.conditions.Key('Course').eq(event["Course"]))
    
    return data["Items"]