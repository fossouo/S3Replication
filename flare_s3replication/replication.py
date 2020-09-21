#!/usr/bin/python3
import boto3

class Replication:

    client = boto3.client('s3')

    def __init__(self, resource, owner):
        self.resource=resource
        self.owner=owner
        return

    def status(self): 
        
        print("Calling S3 replication service with the following parameters: ")
        print("Bucket Name = ", self.resource) 
        print("ExpectedBucketOwner = ", self.owner)

        return self.client.get_bucket_replication(
		    Bucket=self.resource,
		    ExpectedBucketOwner=self.owner
	)
