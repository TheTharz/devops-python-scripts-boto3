import boto3

def start_instances(instance_ids):
    ec2_client = boto3.client("ec2")
    response = ec2_client.start_instances(InstanceIds=instance_ids)
    return response

def main():
    instance_ids = ['i-06f0a0001f4439698','i-061caf661fc241a18','i-033664e5a2570d1f7']
    response = start_instances(instance_ids)
    print(response)

if __name__ == "__main__":
    main()