from aws_cdk import (
    Stack,
    aws_lambda,
    aws_sqs,
    )

from constructs import Construct

class PipeLineTestApp(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        aws_lambda.Function(
            self, "LambdaFunction", 
            runtime=aws_lambda.Runtime.NODEJS_12_X,
            handler="index.handler",
            code=aws_lambda.InlineCode("exports.handler = _ => 'Hello, CDK';")
        )

