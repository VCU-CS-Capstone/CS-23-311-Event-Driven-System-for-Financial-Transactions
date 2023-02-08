import os
import boto3
from stat import SF_SNAPSHOT
import sys
import json
import uuid
import time
from datetime import datetime

print(datetime.now()) #
client = boto3.client('events')

account = {}
transaction = {}

def CreateAccount():
  cardType = input("What card would you like to choose? \n (1) American Dragon Card \n (2) Big Baller Card \n")
  cardNum = input("Whats your card id \n")
  name = input("What is your name? \n")
  ssn = input("What is you social security? \n")
  dob = input ("What is your date of birth (mm-dd-yyyy) \n")
  address = input("What is your shipping address? \n")
  email = input("What is your email? \n")
  phone = input("What is your phone number?\n")
  if cardType == '1':
    cardTypeString = 'American Dragon Card'
  elif cardType == '2':
    cardTypeString = 'Big Baller Card' #Error handling for other card types? 
  # account['id'] = str(uuid.uuid4()) #Use an expanded form for setting the account variable (see below)
  account['id'] = '4444' #Can this not be hardcoded? Use .env or maybe lookup the account in Dyanmo?
  account['creditCardId'] = cardNum
  account['name'] = name
  account['address'] = address
  account['ssn'] = ssn
  account['birthdate'] = dob
  account['email'] = email
  account['phone'] = phone
  account['cardType'] = cardTypeString
  account['currentBalance'] = 0
  account['previousBalance'] = 0
  account['Type'] = "Book New Account"
  if cardType == '1':
    account['maxCredit'] = 400
  elif cardType == '2':
    account['maxCredit'] = 100000
  
  print(account) #Can add statement before print print("account:", account)
  response = client.put_events(
        Entries=[
            {
            'Time' : datetime.now(),
            'Source' : 'Lambda Publish',
            'Resources' : [
            ],
            'DetailType' : 'Custom event demo from ToEventbridge Lambda',
            'Detail' : json.dumps(account),
            'EventBusName' : 'arn:aws:events:us-east-1:072065628342:event-bus/FinalEventBus',
            'TraceHeader' : 'testdemo'
            },
                ]
            )
  print(json.dumps(account))
  print(response)

def CreateNewTransaction():
  CreditCard = input('What credit card did you make this transaction on? \n')
  Merchant = input('What merchant did this transaction occur at? \n')
  Location = input('Where did this transaction occur at? \n')
  Price = input('What was the cost of this transaction? \n')
  
  
  transaction['TransactionId'] = str(uuid.uuid4())
  transaction['CreditCardId'] = CreditCard
  transaction['Status'] = 'Authorize'
  transaction['Merchant'] = Merchant
  transaction['Date'] = str(datetime.now())
  transaction['Time'] = 'Time will be fixed'
  transaction['Location'] = Location
  transaction['Price'] = Price
  transaction['Type'] = 'Create New Transaction'
  transaction['AccountId'] = '4444'
  print(transaction)
  response = client.put_events(
        Entries=[
            {
            'Time' : datetime.now(),
            'Source' : 'Lambda Publish',
            'Resources' : [
            ],
            'DetailType' : 'Custom event demo from ToEventbridge Lambda',
            'Detail' : json.dumps(transaction),
            'EventBusName' : 'arn:aws:events:us-east-1:072065628342:event-bus/FinalEventBus',
            'TraceHeader' : 'testdemo'
            },
                ]
            )
  print(response)
  time.sleep(15) #Why is sleep needed here? 
  Authorization(transaction['AccountId'], transaction['CreditCardId'], transaction['Price'], transaction)

def Authorization(AccountId, creditCardId, costOfTransaction, transaction):
  client2 = boto3.resource('dynamodb') #Use semantic naming, not client2 so you know what it is
  table = client2.Table('AccountDB') #same as above
  response = table.get_item(Key={'AccountId': AccountId, 'creditCardId' : creditCardId })
  entry=response['Item']
  currentBalance = float(entry['currentBalance']) #What are these values if you don't cast them as float?
  maxCredit = float(entry['maxCredit'])
  cost = float(transaction['Price'])
  if currentBalance + cost< maxCredit: #What if it is equal?
    MerchentFunded = input("Press a key to fund merchant\n")
    fund(transaction)
  else:
    print("Insufficent Balance")

def fund(transaction):
  print('price is')#Combine print statements
  print(transaction['Price'])
  client4 = boto3.client('events')
  Item = { #This sytax is good!
    'TransactionId' : transaction['TransactionId'],
    'CreditCardId' : transaction['CreditCardId'],
    'Status' : 'Merchent Funded',
    'Merchant' : transaction['Merchant'],
    'Date' : transaction['Date'],
    'Time' : transaction['Time'],
    'Location' : transaction['Location'],
    'Price' : [transaction['Price']],
    'Type' : 'Settlement',
    'AccountId' : transaction['AccountId']
  }
  response = client4.put_events(
        Entries=[
            {
            'Time' : datetime.now(),
            'Source' : 'Lambda Publish',
            'Resources' : [
            ],
            'DetailType' : 'Custom event demo from ToEventbridge Lambda',
            'Detail' : json.dumps(Item),
            'EventBusName' : 'arn:aws:events:us-east-1:072065628342:event-bus/SettlementEventBus',
            'TraceHeader' : 'testdemo'
            },
                ]
            )
  print('Merchant Funded')


choice = input("What would you like to do \n (1) Create a new Account \n (2) Make a new Transaction \n")

if choice == '1':
  CreateAccount()
if choice == '2': #Use elif, plus else
  CreateNewTransaction()





#Example
# account = {
#   "name" = name
#   "address" = address
# }