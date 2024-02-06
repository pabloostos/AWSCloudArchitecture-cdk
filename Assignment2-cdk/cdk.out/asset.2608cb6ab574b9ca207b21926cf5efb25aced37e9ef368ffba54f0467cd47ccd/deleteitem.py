import json as JSON
import boto3

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('KnowledgeCatalogTable')
    
    response = table.delete_item(
        Key = {
            "Title": event["queryStringParameters"]["Title"]
        }
    )
    
    respuesta = {
        "isBase64Encoded": True,
        "statusCode": response["ResponseMetadata"]["HTTPStatusCode"],
        "headers": response["ResponseMetadata"]["HTTPHeaders"],
        "body": JSON.dumps(response)
    }

    return respuesta