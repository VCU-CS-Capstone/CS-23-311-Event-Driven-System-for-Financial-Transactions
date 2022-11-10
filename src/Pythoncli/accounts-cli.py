import os
from stat import SF_SNAPSHOT
import sys
import json
import uuid
from datetime import date

def CreateAccount():
  account = {}
  name = input("What is your name? \n")
  address = input("What is your shipping address? \n")
  email = input("What is your email? \n")
  phone = input("What is your phone number?\n")

  account['id'] = str(uuid.uuid4())
  account['object'] = 'customer'
  account["address"] = address
  account["balance"] = '0'
  account["created"] = str(date.today())
  account["defaultSource"] = ' '
  account['delinquent'] = 'true'
  account['description'] = name
  account['email'] = email
  account['name'] = name
  account['phone'] = phone
  account['shipping'] = address

  accountUpdate = json.dumps(account)
  return accountUpdate

if len(sys.argv) > 2:
    print('You have specified too many arguments')
    sys.exit()

if len(sys.argv) < 2:
  choice = input("Enter what function you would like to do\n(1) Create Account \n ")
  if choice == "1":
    datapayload = CreateAccount()
    sqsMessageCommand = 'aws sqs send-message --queue-url https://sqs.us-east-1.amazonaws.com/072065628342/cli-sqs-lambda-db --message-body \'' + datapayload+ '\''
    os.system(sqsMessageCommand)
    print('tried to run system command: ' + sqsMessageCommand)


# print('\n'.join(os.listdir(input_path)))
