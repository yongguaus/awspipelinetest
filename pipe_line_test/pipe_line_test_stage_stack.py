import aws_cdk as cdk
from constructs import Construct
from pipe_line_test.pipe_line_test_app_stage import PipeLineTestAppStack

class TestPipelineAppStage(cdk.Stage):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        lambdaStack = PipeLineTestAppStack(self, "LambdaStack")