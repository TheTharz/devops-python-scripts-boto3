import boto3

def getInstances():
  ec2_client = boto3.client('ec2')
  response = ec2_client.describe_instances()
  return response

def monitor_instance():
  ec2_client = boto3.client('ec2')
  instances = getInstances()
  monitored_instances = []
  for r in instances['Reservations']:
    for i in r['Instances']:
      instance_id = i['InstanceId']
      response = ec2_client.monitor_instances(InstanceIds=[instance_id])
      instance_state = {
        'InstanceId': instance_id,
        'State': response['InstanceMonitorings'][0]['Monitoring']['State'],
      }

      monitored_instances.append(instance_state)

  return monitored_instances

def main():
  monitored_instances = monitor_instance()
  for i in monitored_instances:
    print(f"InstanceId: {i['InstanceId']}\nState: {i['State']}\n")

if __name__ == "__main__":
  main()
