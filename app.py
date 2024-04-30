import os

import aws_cdk
from dotenv import load_dotenv

from deployment.lambda_python_example_stack import LambdaPythonExampleStack

load_dotenv()

app = aws_cdk.App()

env = aws_cdk.Environment(
    account=os.environ.get("CDK_DEFAULT_ACCOUNT"),
    region=os.environ.get("CDK_DEFAULT_REGION"),
)

LambdaPythonExampleStack(
    app,
    "LambdaPythonExampleStack",
    env=env,
)

app.synth()
