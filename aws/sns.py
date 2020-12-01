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

