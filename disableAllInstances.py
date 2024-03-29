import boto3;

ec2_client = boto3.client("ec2");

def disable_instances(instance_ids):
  response = ec2_client.stop_instances(InstanceIds=instance_ids);
  return response;

def get_all_instances():
  response = ec2_client.describe_instances(

  );
  instances = [];
  for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
      instance_id = instance["InstanceId"];
      instance_type = instance["InstanceType"];
      instance_state = instance["State"]["Name"];

      instances.append({
        "InstanceID": instance_id,
        "InstanceType": instance_type,
        "InstanceState": instance_state,

      });
  return instances;

def disable_running_instances():
  instances = get_all_instances();
  if(instances == []):
    return "No active instances found";

  instance_ids = [];
  for instance in instances:
    if(instance["InstanceState"] == "running"):
      instance_ids.append(instance["InstanceID"]);
  if(instance_ids == []):
    return "No running instances found";
  response = disable_instances(instance_ids);
  return response;

def main():
  print("====================All Instances ======================")
  instances = get_all_instances();
  for instance in instances:
    print(f"Instance ID: {instance['InstanceID']}");
    print(f"Instance Type: {instance['InstanceType']}");
    print(f"Instance State: {instance['InstanceState']}");
    print("-" * 50);
  if(instances == []):
    print("No active instances found");
    return;
  print("====================Disabling Active Instances ======================")
  response = disable_running_instances();
  print(response);

if __name__ == "__main__":
  main()