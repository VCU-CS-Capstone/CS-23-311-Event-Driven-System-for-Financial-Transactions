import json
import boto3


def updateDynamo(Item):
    client = boto3.resource('dynamodb')
    table = client.Table('AccountDB')
    response = table.put_item(Item = Item)
    
def lambda_handler(event, context):

    print(event)
    parsed = json.loads(event['Records'][0]['body'])
    print(parsed)
    id = parsed['detail']['id']
    print(id)
    object = parsed['detail']['object']
    address = event['detail']['address']
    balance = event['detail']['balance']
    created = event['detail']['created']
    defaultSource = event['detail']['defaultSource']
    delinquent = event['detail']['delinquent']
    description = event['detail']['description']
    email = event['detail']['email']
    name = event['detail']['name']
    phone = event['detail']['phone']
    shipping = event['detail']['shipping']
    
    Item = {
        'AccountId' : id
        'object' : object,
        'address' : address,
        'balance' : balance,
        'created' : created,
        'defaultSource' : defaultSource,
        'delinquent' : delinquent,
        'description' : description,
        'email' : email,
        'name' : name,
        'phone' : phone,
        'shipping' : shipping
    }
    response = updateDynamo(Item)
    print(Item)
    print (Item)
    return {
        'statusCode': 200,
        'body': json.dumps('Db added!')
    }
