import json
import boto3

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('KnowledgeCatalogTable')

    data = table.scan()
    
    # respuesta = {
    #     "isBase64Encoded": True,
    #     "statusCode": response["ResponseMetadata"]["HTTPStatusCode"],
    #     "headers": response["ResponseMetadata"]["HTTPHeaders"],
    #     "body": response
    # }
    
    # return respuesta
    
    return data