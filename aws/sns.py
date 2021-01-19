import boto3
import json

sns = boto3.client('sns')

numbers = ['+39...']

# extension note: https://blog.shikisoft.com/send-sms-with-sns-aws-lambda-python/

for number in numbers:
    response = sns.publish(
        PhoneNumber=number,
        Message="Hello"
    )
    print(response)

# for email
msg_json = {"a": "b"}
sns.publish(
            TargetArn="...",
            Subject=('...'),
            Message=json.dumps({'default': json.dumps(msg_json, indent=4, sort_keys=True)}),
            MessageStructure='json'
        )