
# install boto3
#pip install boto3

# import boto3
import boto3


def lambda_handler(event, context):

   # Impprovement: we can also use the boto3 session which allows us to load profiles directly and pass credentials from the ~/.aws/credentials file
   # session = boto3.Session(profile_name='EC2_logging')
   # ec2_client = session.client('ec2', region_name="us-east-1")

    # Create an ec2 client to interact with the EC2 sevrice	
    ec2_client = boto3.client('ec2'), 
    region_name="us-east-1",
    export AWS_ACCESS_KEY_ID=aws_access_key_id,
    export AWS_SECRET_ACCESS_KEY=aws_secret_access_key
    
    # Describe instances using the describe_instances method and store the result in the response variable
    response = ec2_client.describe_instances()  

    # create an empty list called instanceList, use a for loop to iterate over the response variable and append the result of each iteration to instanceList
    instanceList = []
    for instance in response['Reservations']:
	    for instance in instance['Instances']:
        	instanceList.append(instance['InstanceId'])

print(f"Found {len(instanceList)} instances")

lambda_handler

