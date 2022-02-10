import aws_cdk as core
import aws_cdk.assertions as assertions

from pipe_line_test.pipe_line_test_stack import PipeLineTestStack

# example tests. To run these tests, uncomment this file along with the example
# resource in pipe_line_test/pipe_line_test_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = PipeLineTestStack(app, "pipe-line-test")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
