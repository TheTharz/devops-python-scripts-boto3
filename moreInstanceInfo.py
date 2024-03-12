import boto3

def list_instances():
    ec2_client = boto3.client('ec2')
    response = ec2_client.describe_instances()

    instances = []

    for r in response['Reservations']:
        for i in r['Instances']:
            instance_info = {
                'InstanceId': i['InstanceId'],
                'LaunchTime' : i['LaunchTime'],
                'AvailabilityZone': i['Placement']['AvailabilityZone'],
                'Architecture': i['Architecture'],
                'InstanceType': i['InstanceType'],
            }
            instances.append(instance_info)


    return instances

def main():
    instances = list_instances()

    for i in instances:
        print(f"InstanceId: {i['InstanceId']}\nLaunchTime: {i['LaunchTime']}\nAvailabilityZone: {i['AvailabilityZone']}\nArchitecture: {i['Architecture']}\nInstanceType: {i['InstanceType']}\n")

if __name__ == "__main__":
    main()