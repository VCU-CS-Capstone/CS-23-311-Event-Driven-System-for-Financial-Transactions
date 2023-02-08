import json
import boto3


# "id": "0f2f3c91-73b4-45d1-92ec-3eca6564952e",
#   "creditCardId": "test",
#   "name": "test",
#   "address": "test",
#   "ssn": "test",
#   "birthdate": "test",
#   "email": "test",
#   "phone": "test",
#   "cardType": "",
#   "currentBalance": 0,
#   "previousBalance": 0,
#   "Type": "Book New Account"

def updateDynamo(Item):
    client = boto3.resource('dynamodb')
    table = client.Table('DynamoDBTableV2')
    response = table.put_item(Item = Item)
    
def lambda_handler(event, context):

    print(event)
    parsed = json.loads(event['Records'][0]['body']) #Don't hardcode 
    print(parsed)
    id = parsed['detail']['id']
    print(id) 
    creditCardId = parsed['detail']['creditCardId']
    name = parsed['detail']['name']
    address = parsed['detail']['address']
    ssn = parsed['detail']['ssn']
    birthdate = parsed['detail']['birthdate']
    email = parsed['detail']['email']
    phone = parsed['detail']['phone']
    cardType = parsed['detail']['cardType']
    currentBalance = parsed['detail']['currentBalance']
    previousBalance = parsed['detail']['previousBalance']
    
    
    Item = {
        'AccountId' : id,
        'creditCardId' : creditCardId,
        'name' : name,
        'address' : address,
        'ssn' : ssn,
        'birthdate' : birthdate,
        'email' : email,
        'phone' : phone,
        'cardType' : cardType,
        'currentBalance' : currentBalance,
        'previousBalance' : previousBalance
    }
    response = updateDynamo(Item) #Does the response provide any value? 
    print(Item)
    print (Item) #Duplicate
    return { #What about errors?
        'statusCode': 200,
        'body': json.dumps('Db added!')
    }
