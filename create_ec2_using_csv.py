# import boto3
import csv
import boto3
AWS_REGION = "us-east-1"
ec2 = boto3.resource('ec2', region_name=AWS_REGION)

def main():
    with open("a.csv", "r") as file:
        reader = csv.reader(file)
        for each in reader:
            instances = ec2.create_instances(
            ImageId=str(each[2]),
            MinCount=int(each[3]),
            MaxCount=int(each[3]),
            InstanceType=each[1],
            KeyName=str(each[4])
        )

if __name__ == "__main__":
    main()    
