import boto3

def ecr_tags_get(credentials, arn):
	ecr = boto3.client('ecr', region_name=credentials['AWS_REGION'])
	return ecr.list_tags_for_resource(resourceArn=arn)

def ecr_tag_update(region, account_id, repo):
    ecr = boto3.client(
        'ecr',
        region_name=region
    )

    arn = 'arn:aws:ecr:{}:{}:repository/{}'.format(region, account_id, repo['name'])
    repository_tags = ecr.list_tags_for_resource(resourceArn=arn)

    response = ecr.tag_resource(
        resourceArn=arn,
        tags=[
            {
                'Key': 'stable_tag',
                'Value': repo['tag']
            },
        ]
    )