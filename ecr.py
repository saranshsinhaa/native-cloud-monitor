import boto3

ecr_client = boto3.client('ecr')

repository_name = "native-cloud-monitor"
response = ecr_client.create_repository(repositoryName=repository_name)

repository_uri = response ['repository']['repositoryUri']
print(repository_uri)