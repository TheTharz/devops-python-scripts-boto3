import boto3

def start_ec2_instance(instance_name):
    # Initialize Boto3 EC2 client
    ec2_client = boto3.client('ec2')

    # Describe instances with the given name
    response = ec2_client.describe_instances(Filters=[
        {
            'Name': 'tag:Name',
            'Values': [instance_name]
        }
    ])

    # Extract the instance ID from the response
    instance_id = response['Reservations'][0]['Instances'][0]['InstanceId']

    # Start the instance
    ec2_client.start_instances(InstanceIds=[instance_id])
    print(f"Instance with name '{instance_name}' (ID: {instance_id}) is starting.")

# Replace 'your-instance-name' with the name of your EC2 instance
instance_name = 'Designflow'
start_ec2_instance(instance_name)
