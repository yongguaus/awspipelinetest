from aws_cdk import (
    Stack,
    pipelines,
)
from constructs import Construct
from pipe_line_test.pipe_line_test_stage_stack import TestPipelineAppStage

class PipeLineTestStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        pipeline = pipelines.CodePipeline(
           scope=self,
           id="TestPipeline",
           synth=pipelines.ShellStep("Synth", 
                            input=pipelines.CodePipelineSource.git_hub("yongguaus/awspipelinetest", "main"),
                            commands=[
                                "npm install -g aws-cdk", 
                                "python -m pip install -r requirements.txt", 
                                "cdk synth"]
                        )
           )

        pipeline.add_stage(TestPipelineAppStage(self, "test",
            env=cdk.Environment(account="889043514394", region="ap-southeast-2")))
         
       