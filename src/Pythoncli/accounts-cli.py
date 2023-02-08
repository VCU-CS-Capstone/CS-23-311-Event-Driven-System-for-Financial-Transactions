import os
import boto3
from stat import SF_SNAPSHOT
import sys
import json
import uuid
from datetime import date

client = boto3.client('events')

def CreateAccount():
  account = {}
  cardType = input("What card would you like to choose? \n (1) American Dragon Card \n (2) Big Baller Card \n")
  cardNum = input("Whats your card id \n")
  name = input("What is your name? \n")
  ssn = input("What is you social security? \n")
  dob = input ("What is your date of birth (mm-dd-yyyy) \n")
  address = input("What is your shipping address? \n")
  email = input("What is your email? \n")
  phone = input("What is your phone number?\n")
  cardTypeString = ""
  if cardType == 1:
    cardTypeString = 'American Dragon Card'
  elif cardType == 2:
    cardTypeString == 'Big Baller Card'
  account['id'] = str(uuid.uuid4())
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
  if cardType == 1:
    account['maxCredit'] = 400
  elif cardType == 2:
    account['maxCredit'] = 100000
 
  accountUpdate = json.dumps(account)
  return accountUpdate

if len(sys.argv) > 2:
    print('You have specified too many arguments')
    sys.exit()

if len(sys.argv) < 2:
  choice = input("Enter what function you would like to do\n(1) Create Account \n ")
  if choice == "1":
    datapayload = CreateAccount()
    sqsMessageCommand = 'aws eventbridge put-events --queue-url https://sqs.us-east-1.amazonaws.com/072065628342/sqsToLambdaToEb --message-body \'' + datapayload+ '\''
    os.system(sqsMessageCommand)
    print('tried to run system command: ' + sqsMessageCommand)


# print('\n'.join(os.listdir(input_path)))
