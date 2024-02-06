import aws_cdk as core
import aws_cdk.assertions as assertions

from assignment2_cdk.assignment2_cdk_stack import Assignment2CdkStack

# example tests. To run these tests, uncomment this file along with the example
# resource in assignment2_cdk/assignment2_cdk_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = Assignment2CdkStack(app, "assignment2-cdk")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
