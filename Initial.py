import boto3

def lambda_handler(event, context):

    ec2_client = boto3.client('ec2', region_name="ap-south-1")

    response = ec2_client.describe_instances()  

    instanceList = []
    for instance in response['Reservations']['Instances']:
        instanceList.append(instance['InstanceId'])

    print(f"Found {len(response['Reservations']['Instances'])} instances")

    return instanceList