import json
import boto3
import requests

def updateDynamo(Item):
    client = boto3.resource('dynamodb')
    table = client.Table('Transactions')
    response = table.put_item(Item = Item)
    
def lambda_handler(event, context):
    
#     account['id'] = str(uuid.uuid4())
#   account['object'] = 'customer'
#   account["address"] = address
#   account["balance"] = '0'
#   account["created"] = str(date.today())
#   account["defaultSource"] = ' '
#   account['delinquent'] = 'true'
#   account['description'] = name
#   account['email'] = email
#   account['name'] = name
#   account['phone'] = phone
#   account['shipping'] = address
    print(event)
    parsed = json.loads(event['Records'][0]['body'])
    print(parsed)
    id = parsed['detail']['id']
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
        'id' : id,
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
