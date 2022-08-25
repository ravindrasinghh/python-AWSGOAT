
import boto3

AWS_REGION = "us-east-1"
ec2 = boto3.client('ec2', region_name=AWS_REGION)
describe_address = ec2.describe_addresses()


""" Cleanup elastic IP's that are not being used in our AWS Account"""
def delete_unused_elastic_ip(ec2):
    for eip in describe_address['Addresses']:
        if "NetworkInterfaceId" not in eip:
            print (eip['PublicIp'] + "is not asscoaited with any Network Interface ID") 
            ec2.release_address(AllocationId=eip['AllocationId'])
            print (eip['PublicIp'] + "got deleted") 

delete_unused_elastic_ip(ec2) 
