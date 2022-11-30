```
AWS_IMAGE_BASE_URL=xxxxxxxxxxxx.dkr.ecr.eu-central-1.amazonaws.com
AWS_IMAGE_REPOSITORY=xxx_xxx_xxx
AWS_IMAGE_VERSION=x.x
AWS_PROFILE=XXX
AWS_REGION=eu-central-1
HOST_AWS_CREDENTIALS_FOLDER=$HOME/.aws
LOCAL_REPOSITORY=xxx/xxx

docker run --rm -t -v $HOST_AWS_CREDENTIALS_FOLDER:/root/.aws amazon/aws-cli:2.9.2 ecr get-login-password --region $AWS_REGION --profile $AWS_PROFILE | docker login --username AWS --password-stdin $AWS_IMAGE_BASE_URL

docker tag $LOCAL_REPOSITORY:$AWS_IMAGE_VERSION $IMAGE_BASE_URL/$AWS_IMAGE_REPOSITORY:$AWS_IMAGE_VERSION
docker push $AWS_IMAGE_BASE_URL/$AWS_IMAGE_REPOSITORY:$AWS_IMAGE_VERSION
```
