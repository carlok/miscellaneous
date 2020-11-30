import boto3
import json

sns = boto3.client('sns')

numbers = ['+39...']

# response = sns.set_sms_attributes(attributes={'DefaultSenderID': 'FixMe'})

for number in numbers:
    response = sns.publish(
        PhoneNumber=number,
        Message="Hello"
    )
    print(response)

