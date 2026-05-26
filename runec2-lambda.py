import json
import boto3

client = boto3.client('ec2')
def lambda_handler(event, context):
    automation_ec2 = client.run_instances(
    ImageId='ami-0236922087fa98b6e',
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro',)
    print(automation_ec2['Instances'][0]['InstanceId'])
#print is from documentation brackets reps[]
