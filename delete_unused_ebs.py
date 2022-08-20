import boto3
AWS_REGION = "us-east-1"
ec2 = boto3.client('ec2', region_name=AWS_REGION)
ec2_info = ec2.describe_volumes()
newlist = []
for volume in ec2_info["Volumes"]:
    if volume["State"]=="available" and volume["AvailabilityZone"] == "us-east-1a":
       newlist.append(volume["VolumeId"])
for i in  newlist:
    ec2_info = ec2.describe_volumes()
    print("volumes are deleted" + str(i))
    ec2.delete_volume(VolumeId=i)
    
