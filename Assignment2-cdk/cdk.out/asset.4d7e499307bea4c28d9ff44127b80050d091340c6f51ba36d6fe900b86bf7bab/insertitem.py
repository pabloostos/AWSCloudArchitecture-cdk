import json
import boto3

def lambda_handler(event, context):
    if len(event["queryStringParameters"]) != 3: 
        return {
            "statusCode": 400,
            'body': "Input not valid!"
        }
    else:
        for key in event["queryStringParameters"]: 
            if key not in ["Title", "Course", "Description"]:
                return {
                "statusCode": 400,
                'body': "Input not valid!"
                }
      
    
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('KnowledgeCatalogTable')

    response = table.put_item(
        Item=event["queryStringParameters"]
    )
    
    return response