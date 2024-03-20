import boto3

# Create an EC2 client using the session
ec2_client = boto3.client('ec2')

# Get all running instances
response = ec2_client.describe_instances(
    Filters=[
        {
            'Name': 'instance-state-name',
            'Values': ['running']
        }
    ]
)

# Extract instance information from the response
instances = []
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        instance_id = instance['InstanceId']
        instance_type = instance['InstanceType']
        instance_state = instance['State']['Name']
        instance_public_ip = instance.get('PublicIpAddress', 'N/A')
        instance_private_ip = instance.get('PrivateIpAddress', 'N/A')
        
        # Append instance details to the list
        instances.append({
            'InstanceID': instance_id,
            'InstanceType': instance_type,
            'InstanceState': instance_state,
            'PublicIP': instance_public_ip,
            'PrivateIP': instance_private_ip
        })

# Print the list of running instances
for instance in instances:
    print(f"Instance ID: {instance['InstanceID']}")
    print(f"Instance Type: {instance['InstanceType']}")
    print(f"Instance State: {instance['InstanceState']}")
    print(f"Public IP: {instance['PublicIP']}")
    print(f"Private IP: {instance['PrivateIP']}")
    print("-" * 50)
