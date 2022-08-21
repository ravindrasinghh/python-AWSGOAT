import boto3
AWS_REGION = "us-east-1"
ec2 = boto3.client('ec2', region_name=AWS_REGION)
ec2_info = ec2.describe_instances()

newlist = []
for ec2_list in ec2_info["Reservations"]:
    for instance_list in ec2_list["Instances"]:
        if instance_list["InstanceType"] == "t2.micro":
            newlist.append(instance_list["InstanceId"])

for i in  newlist:
    ec2.start_instances(InstanceIds=[i])
