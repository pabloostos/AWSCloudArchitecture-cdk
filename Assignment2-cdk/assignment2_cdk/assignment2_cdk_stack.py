from aws_cdk import (
    # Duration,
    Stack,
    aws_lambda as lambda_,
    aws_dynamodb as dynamodb,
    aws_apigateway as apigateway
    # aws_sqs as sqs,
)
from constructs import Construct

class Assignment2CdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Creating DynamoDB table
        table = dynamodb.Table(self, id = "KnowledgeCatalogTable", table_name = "KnowledgeCatTable",
            partition_key=dynamodb.Attribute(name="Title", type=dynamodb.AttributeType.STRING),
            sort_key=dynamodb.Attribute(name="Course", type=dynamodb.AttributeType.STRING)
            )

        # =============================================================================================
        # Lambda Functions and granting permissions
        # =============================================================================================

        # Lambda: Retrieve all the knowledge items in the database.
        retrieveAll_lambda = lambda_.Function(self, "RetrieveAll",
            runtime=lambda_.Runtime.PYTHON_3_10,
            handler="retrieveall.lambda_handler",
            code=lambda_.Code.from_asset("lambdas")
        )
        # Permission for RetrieveAll
        table.grant(retrieveAll_lambda, 'dynamodb:Scan')

        # =============================================================================================
        # Lambda: Retrieve all the knowledge items of a particular course.
        retrieveAllCourse_lambda = lambda_.Function(self, "RetrieveAllCourse",
            runtime=lambda_.Runtime.PYTHON_3_10,
            handler="retrieveallcourse.lambda_handler",
            code=lambda_.Code.from_asset("lambdas")
        )
        # Permission for RetrieveAllCourse
        table.grant(retrieveAllCourse_lambda, 'dynamodb:Scan')

        # =============================================================================================
        # Lambda: Insert a new knowledge item.
        deleteItem_lambda = lambda_.Function(self, "DeleteItem",
            runtime=lambda_.Runtime.PYTHON_3_10,
            handler="deleteitem.lambda_handler",
            code=lambda_.Code.from_asset("lambdas")
        )
        # Permission for RetrieveAllCourse
        table.grant(deleteItem_lambda, 'dynamodb:DeleteItem')

        # =============================================================================================
        # Lambda: Delete a knowledge item.
        insertItem_lambda = lambda_.Function(self, "InsertItem",
            runtime=lambda_.Runtime.PYTHON_3_10,
            handler="insertitem.lambda_handler",
            code=lambda_.Code.from_asset("lambdas")
        )
        # Permission for RetrieveAllCourse
        table.grant(insertItem_lambda, 'dynamodb:PutItem')
    
        # =============================================================================================
        # API Gateway
        # =============================================================================================
        api = apigateway.RestApi(self, id = "Assignment2", rest_api_name = "Assignment2", endpoint_types= [apigateway.EndpointType.REGIONAL])
        
        # API Reusorce and Method for retrieveAllCourse
        retrieve_All = api.root.add_resource("retrieveall")
        retrieve_All.add_method("GET", apigateway.LambdaIntegration(retrieveAll_lambda))

        # API Reusorce and Method for retrieveAllCourse
        retrieve_AllCourse = api.root.add_resource("retrievecourse")
        retrieve_AllCourse.add_method("GET", apigateway.LambdaIntegration(retrieveAllCourse_lambda))

        # API Reusorce and Method for InsertItem
        delete_item = api.root.add_resource("deleteitem")
        delete_item.add_method("DELETE", apigateway.LambdaIntegration(deleteItem_lambda))

        # API Reusorce and Method for InsertItem
        insert_item = api.root.add_resource("insertitem")
        insert_item.add_method("POST", apigateway.LambdaIntegration(insertItem_lambda))






        
