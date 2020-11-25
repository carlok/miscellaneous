import boto3

"""
Essential Policy (counting out EC2 creation):
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": "iam:PassRole",
            "Resource": "*"
        },
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": "sts:DecodeAuthorizationMessage",
            "Resource": "*"
        }
    ]
}
"""

ec2 = boto3.resource(
    'ec2',
    aws_access_key_id='x',
    aws_secret_access_key='x',
    region_name='x'
)

instances = ec2.create_instances(
    ImageId='ami-x',
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro',
    KeyName='x',
    IamInstanceProfile={'Arn': 'arn:aws:iam::x:instance-profile/x'},
    TagSpecifications=[
      {
        'ResourceType': 'instance',
        'Tags': [
          {
            'Key': 'Name',
            'Value': 'foobar'
          }
        ]
      },
    ]
)
