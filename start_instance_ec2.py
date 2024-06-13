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

    if not response['Reservations']:
        print(f"No instances found with the name '{instance_name}'.")
        return

    # Extract the instance ID from the response
    instance_id = response['Reservations'][0]['Instances'][0]['InstanceId']

    # Start the instance
    ec2_client.start_instances(InstanceIds=[instance_id])
    print(f"Instance with name '{instance_name}' (ID: {instance_id}) is starting.")

    # Wait for the instance to be in a 'running' state
    waiter = ec2_client.get_waiter('instance_running')
    waiter.wait(InstanceIds=[instance_id])

    # Get the public IP address of the instance
    instance_info = ec2_client.describe_instances(InstanceIds=[instance_id])
    public_ip = instance_info['Reservations'][0]['Instances'][0]['PublicIpAddress']

    print(f"The public IP address of the instance '{instance_name}' is: {public_ip}")

# Prompt user for the instance name
instance_name = input("Enter the name of the EC2 instance: ")
start_ec2_instance(instance_name)
