import json
import boto3
import requests

def lambda_handler(event,context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('MyDynamoDBTable')
    input = event['Records'][0]['body']
    response = table.put_item(Item = input)