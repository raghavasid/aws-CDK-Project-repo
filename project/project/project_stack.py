from aws_cdk import ( # type: ignore
    # Duration,
    Stack,
    # aws_sqs as sqs,
)
from constructs import Construct

class ProjectStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "ProjectQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
