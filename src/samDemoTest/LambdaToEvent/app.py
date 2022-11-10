import json
import boto3 
import datetime

client = boto3.client('events')

def lambda_handler(event, context):
    response = client.put_events(
        Entries=[
            {
            'Time': datetime.datetime.now(),
            'Source': 'Lambda Publish',
            'Resources': [
                ],
            'DetailType': 'Custom event demo',
            'Detail': json.dumps(event), #converts from json to string VERY IMPORTANT EVENT THIGY DHREER DONT FOREGET. no new message comes when its false so it doesnt trigger event bus
            'EventBusName': 'arn:aws:events:us-east-1:072065628342:event-bus/eventBus', #make sure u get this from the right event bus. make sure rules are in the right busself.
            'TraceHeader': 'testdemo'
            },
                ]
            )
            
    return response