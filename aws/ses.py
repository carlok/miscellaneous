import boto3
import json

from botocore.exceptions import ClientError
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

def email_send(region, subject, sender, recipient, mtext, results, file_name):
    CHARSET = "utf-8"
    mhtml = '<pre>\n{}</pre>'.format(mtext)

    client = boto3.client(
        'ses',
        region_name=region
    )

    msg = MIMEMultipart('mixed')
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient

    msg_body = MIMEMultipart('alternative')

    textpart = MIMEText(mtext.encode(CHARSET), 'plain', CHARSET)
    htmlpart = MIMEText(mhtml.encode(CHARSET), 'html', CHARSET)

    msg_body.attach(textpart)
    msg_body.attach(htmlpart)

    att = MIMEApplication(json.dumps(results))

    att.add_header('Content-Disposition', 'attachment',
                filename='{}.json'.format(file_name))

    msg.attach(msg_body)

    msg.attach(att)
    try:
        response = client.send_raw_email(
            Source=sender,
            Destinations=[
                recipient
            ],
            RawMessage={
                'Data': msg.as_string(),
            }
        )
    except ClientError as e:
        print(e.response['Error']['Message'])