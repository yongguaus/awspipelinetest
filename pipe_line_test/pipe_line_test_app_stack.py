import aws_cdk
from  aws_cdk import (
    aws_lambda
    )

from constructs import Construct

class PipeLineTestAppStack(cdk.Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        aws_lambda(
            self, "LambdaFunction", 
            runtime=Runtime.NODEJS_12_X,
            handler="index.handler",
            code=InlineCode("exports.handler = _ => 'Hello, CDK';")
        )

