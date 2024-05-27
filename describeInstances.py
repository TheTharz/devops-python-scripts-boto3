import boto3

# Create a session to interact with AWS services
session = boto3.Session()

# Get all available regions
regions = session.get_available_regions('ec2')

# Iterate over each region
for region in regions:
    print(f"Instances in region: {region}")

    # Create an EC2 client for the current region
    ec2 = session.client('ec2', region_name=region)

    # Describe instances in the current region
    response = ec2.describe_instances()

    # Extract instance information and print
    instances = [instance['InstanceId'] for reservation in response['Reservations'] for instance in reservation['Instances']]
    print(instances)
