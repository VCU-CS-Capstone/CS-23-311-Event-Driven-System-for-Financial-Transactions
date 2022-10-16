import json
import boto3
import requests

def lambda_handler(event,context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('MyDynamoDBTable')
    input={'accountId': '123450', 'name': 'Greg', 'transactionType': 'food', 'vendor': 'Sevo', 'amount': '12.35'}
    response = table.put_item(Item = input)
    print(event)
    print(response)
    print("hello")