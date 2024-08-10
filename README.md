# serverless

# test s3
testing s3 access

(used GPT4 assistance)
test successful

- created a bucket => BUCKET_NAME
- created an access point on the Bucket => ACCESS_POINT_ARN
- created IAM user with permission "AmazonS3FullAccess" => aws_access_key_id, aws_secret_access_key

# test ecs

```bash
aws ecr get-login-password --region eu-central-1 | docker login --username AWS --password-stdin 031028648877.dkr.ecr.eu-central-1.amazonaws.com

docker compose build server

docker tag aws-sandbox-server:latest 031028648877.dkr.ecr.eu-central-1.amazonaws.com/microweb-containers:latest

docker push 031028648877.dkr.ecr.eu-central-1.amazonaws.com/microweb-containers:latest

```
