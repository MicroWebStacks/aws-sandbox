import boto3
import json
from datetime import datetime

def lambda_handler(event, context):
    print("Start Launching the Py-Job-Far")
    ecs_client = boto3.client('ecs')
    response = ecs_client.run_task(
        cluster='HelloWebCluster',
        launchType='FARGATE',
        taskDefinition='Simple-Py-Job-Far:1',
        count=1, # Number of tasks to run
        networkConfiguration={
            'awsvpcConfiguration': {
                'subnets': [
                    'subnet-006b59ece71a59770', 'subnet-0e4b731047303872c', 'subnet-0501df34b5112497a'
                ],
                'securityGroups': [
                    'sg-0d64d3461aee4f85a'
                ],
                'assignPublicIp': 'ENABLED'
            }
        }
    )
    print("Done Launching the Py-Job-Far")
    print(response)
    clean_response = {key: val for key, val in response.items() if not isinstance(val, datetime)}
    clean_response['tasks'] = [{k: v if not isinstance(v, datetime) else v.isoformat() for k, v in task.items()} for task in response['tasks']]
    
    return json.dumps(clean_response)
