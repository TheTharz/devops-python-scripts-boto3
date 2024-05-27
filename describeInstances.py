import boto3
ec2 = boto3.client('ec2')
response = ec2.describe_instances()
instances = response['Reservations'][0]['Instances']
print(instances)
for instance in instances:
  print(instance['InstanceId'])

