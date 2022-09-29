import json
import boto3
import requests


def lambda_handler(event, context):
    

    item = {
        'accountID': "accountID",
        'name' : "name",
        'transaction_type' : "transaction_type",
        'vendor' : "vendor",
        'amount' : "amount"
    }
    sqs = boto3.client('sqs')
    
    sqs.send_message(
        QueueUrl="https://sqs.us-east-1.amazonaws.com/xxxxxxxxxxxx/current-time",
        MessageBody = item
    )
    return {
        'statusCode': 200,
        'body': json.dumps(item)
    }
