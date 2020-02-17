#!/usr/bin/python3
import boto3
#import json

'''{'clusterArns': ['arn:aws:ecs:us-east-2:279578293836:cluster/cluster1'], 'nextToken': 'czM6', 'ResponseMetadata': {'RequestId': 'a38ff7b2-1250-4b3d-b198-33c72c2d37d2', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': 'a38ff7b2-1250-4b3d-b198-33c72c2d37d2', 'content-type': 'application/x-amz-json-1.1', 'content-length': '90', 'date': 'Fri, 14 Feb 2020 09:10:21 GMT'}, 'RetryAttempts': 0}}'''

'''response1 = client.list_clusters(
    nextToken= 'czM6',

opsutil and cob

    172.16.16.9
    maxResults=1
)
print(response1)'''

#no_of_Clusters = (len(clusterInfo))
#for i in range(no_of_Clusters):
#    print(clusterInfo[i])'''


#clusterInfo= ['arn:aws:ecs:us-east-2:279578293836:cluster/cluster1','arn:aws:ecs:us-east-2:279578293836:cluster/cluster2']
#print(clusterInfo)
#print(type(clusterInfo))
#print(no_of_Clusters)
'''
for i in range(no_of_Clusters):
    x=clusterInfo[i]
    actualClusterInfo=x.rsplit('/',1)
    print("This is value of x printed",actualClusterInfo)'''
    #print(x)
    #print(clusterInfo)

# this defines the client to be used
client = boto3.client('ecs')


# to get all the cluster details and stored into a variable
clusterInfo = client.list_clusters(
    maxResults=10
)
print(clusterInfo)
clusterInfo=clusterInfo["clusterArns"]
no_of_Clusters = len(clusterInfo)

for i in range(no_of_Clusters):
    x=clusterInfo[i]
    clusterInfo1=x.partition("/")[2]
    print("This is value of x printed",clusterInfo1)