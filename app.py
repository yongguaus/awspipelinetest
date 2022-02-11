import aws_cdk as cdk

from pipe_line_test.pipe_line_test_stack import PipeLineTestStack

app = cdk.App()

PipeLineTestStack(app, "PipeLineTestStack", 
    env=cdk.Environment(account="889043514394", region="ap-southeast-2")
    )


app.synth()
