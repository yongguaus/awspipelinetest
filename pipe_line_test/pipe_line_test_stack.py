from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
    aws_codepipeline,
)
from constructs import Construct

class PipeLineTestStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        pipeline = aws_codepipeline.PipeLine(
           scope=self,
           id="TestPipeline",
           pipelinename="TestPipeline",
           synth=ShellStep("Synth", 
                            input=CodePipelineSource.git_hub("OWNER/REPO", "main"),
                            commands=["npm install -g aws-cdk", 
                                "python -m pip install -r requirements.txt", 
                                "cdk synth"]
                        )
           )
         
        dev_stage = pipeline.add_stage(
            stage_name="Dev",

            
            )

        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "PipeLineTestQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
