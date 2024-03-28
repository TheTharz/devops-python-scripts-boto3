import boto3

def get_running_databases():
    # Initialize the AWS RDS client
    rds_client = boto3.client('rds')

    # Retrieve information about all DB instances
    response = rds_client.describe_db_instances()

    # Extract information about running databases
    running_databases = []
    for db_instance in response['DBInstances']:
        if db_instance['DBInstanceStatus'] == 'available':
            running_databases.append(db_instance['DBInstanceIdentifier'])

    return running_databases

# Example usage
if __name__ == '__main__':
    running_databases = get_running_databases()
    print("Running Databases:")
    for db_name in running_databases:
        print(db_name)
