from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
    aws_codepipeline,
    pipelines,
)
from constructs import Construct

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
         
       