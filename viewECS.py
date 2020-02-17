#!/usr/bin/python3
import boto3

# this defines the client to be used
client = boto3.client('ecs')


# to get all the cluster details and stored into a variable
clusterInfo = client.list_clusters(
    maxResults=10
)
clusterInfo=clusterInfo["clusterArns"]
no_of_Clusters = len(clusterInfo)
print("The below are list of clusters available in the mentioned region")

for i in range(no_of_Clusters):
    x=clusterInfo[i]
    clusterInfo1=x.partition("/")[2]
    print(clusterInfo1)