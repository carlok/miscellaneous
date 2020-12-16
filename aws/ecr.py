import boto3

def ecr_tags_get(credentials, arn):
	ecr = boto3.client('ecr', region_name=credentials['AWS_REGION'])
	return ecr.list_tags_for_resource(resourceArn=arn)