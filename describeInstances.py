import boto3

ec2 = boto3.client('ec2')
response = ec2.describe_instances()

# Iterate over reservations and instances
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        instance_id = instance['InstanceId']

        # Get instance tags
        tags = instance.get('Tags', [])
        
        # Find the 'Name' tag if it exists
        name_tag = next((tag['Value'] for tag in tags if tag['Key'] == 'Name'), None)

        # Print instance ID and Name tag (if available)
        print(f"Instance ID: {instance_id}, Name: {name_tag}")
