import json
import boto3
import os
import sys

ec2 = boto3.client('ec2')
ec2resource = boto3.resource('ec2')

def get_instances(instance_state):
    instances = []
    print(f" Fetching instance with TAG_KEY: {os.environ['TAG_KEY']} and TAG_VALUE: {os.environ['TAG_VALUE']}")
    try:
        response = ec2.describe_instances(
            Filters=[
                {
                    'Name': 'tag:' + os.environ['TAG_KEY'],
                    'Values': [
                        os.environ['TAG_VALUE']
                    ]
                },
                {
                    'Name' : "instance-state-name",
                    'Values': [ instance_state ]
                }
            ]
        )
        print(response)
        for instance in response['Reservations']:
            instances.append(instance['Instances'][0]['InstanceId'])
        return instances
    except Exception as e:
        print(f"Error while fetching EC2 instances \n {e}")


""" start ec2 instances """
def start_instances():
    for instance in get_instances("*"):
        try:
            print(f"Starting instance: {instance}")
            response = ec2.start_instances(
                InstanceIds=[
                    instance
                ]
            )
            print(response)
            instance = ec2resource.Instance(instance)
            instance.wait_until_running()
            print

        except Exception as e:
            print(f"Error while starting instance {instance} \n {e}")


""" stop ec2 instances """
def stop_instances():
    for instance in get_instances("*"):
         try:
            print(f"Stopping instance: {instance}")
            response = ec2.stop_instances(
                InstanceIds=[
                    instance
                ]
            )
            print(response)
            instance = ec2resource.Instance(instance)
            instance.wait_until_stopped()
         except Exception as e:
             print(f"Error while stopping instance {instance} \n {e}")


def reboot_instances():
    for instance in get_instances("running"):
         try:
            print(f"Rebooting instance: {instance}")
            response = ec2.reboot_instances(
                InstanceIds=[
                    instance
                ]
            )
            print(response)
            # below logic might be not a valid usecase - jsut added so we can think of achieving this in some form in future.
            instance = ec2resource.Instance(instance)
            instance.wait_until_running()
         except Exception as e:
             print(f"Error while rebooting instance {instance} \n {e}")




def lambda_handler(event, context):
    print(f"USER ACTION REQUESTED IS {os.environ['ACTION']}")
    if os.environ['ACTION'] == "START":
        start_instances()
    elif os.environ['ACTION'] == "STOP":
        stop_instances()
    elif os.environ['ACTION'] == "REBOOT":
        if len(get_instances("running")) > 0:
            reboot_instances()
        else:
            start_instances()
    else:
        return {
            "statusCode": 500,
            "body": json.dumps({
                "message": "UNSUPPORTED ACTION - VALID VALUES ARE START, STOP OR REBOOT"
            })
        }
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Requested Action was Attempted. Refer Logs for more info."
        })
    }

