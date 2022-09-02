"""
-*- coding: utf-8 -*-
========================
Contributor: Ravindra Singh (Source code)
========================
"""
import pprint
import boto3
import paramiko
import os 

AWS_REGION = os.environ["AWS_REGION"]
BUCKET_NAME = os.environ["BUCKET_NAME"]

def lambda_handler(AWS_REGION,BUCKET_NAME):
    # boto3 client
    client = boto3.client("ec2",region_name = AWS_REGION )
    s3_client = boto3.client("s3")

    # getting instance information
    describeInstance = client.describe_instances()

    instancePublicIP = []
    # fetchin public IP address of the running instances
    for ec2_info in describeInstance["Reservations"]:
        for instance in ec2_info["Instances"]:
            if instance["State"]["Name"] == "running":
                instancePublicIP.append(instance["PublicIpAddress"])

    pprint.pprint(instancePublicIP)
    if len(instancePublicIP) > 0:
        # Downloading pem file from S3 to connect ec2 innstance
        try:
            s3_client.download_file(BUCKET_NAME, "test.pem", "/Users/apple/python-ex/file.pem")
            # Reading pem file 
            key = paramiko.RSAKey.from_private_key_file("/Users/apple/python-ex/file.pem")
            # Paramiko.SSHClient
            ssh_client = paramiko.SSHClient()
            # setting policy to connect to unknown host
            ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            host = instancePublicIP[0]
            print("Connecting to : " + host)
            # connecting to server
            ssh_client.connect(hostname=host, username="ec2-user", pkey=key)
            print("Connected to :" + host)

            # command list
            commands = [
                "docker ps",
                "docker restart dazzling_poitras"
            ]

            # executing list of commands within server
            for command in commands:
                pprint.pprint("Executing {command}")
                stdin, stdout, stderr = ssh_client.exec_command(command)
                pprint.pprint(stdout.readlines())
                pprint.pprint(stderr.readlines())
                stdin.close()
        except:
            print("Code is not working as expected")        

if __name__ == "__main__":
    lambda_handler(AWS_REGION,BUCKET_NAME)    
