import json
import boto3

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('KnowledgeCatalog')
    
    response = table.delete_item(
        Key = {
            "Title": event["queryStringParameters"]["Title"]
        }
    )
    
    return response