#!/usr/bin/python3
import boto3

client = boto3.client('ecs')
i = 0

for i in range(0,1):
    response = client.list_clusters()
    print(response )


'''response = client.list_clusters(
    maxResults=50
)
print(response)'''


