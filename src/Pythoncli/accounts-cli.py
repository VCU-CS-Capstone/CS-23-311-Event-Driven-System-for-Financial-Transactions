import os
from stat import SF_SNAPSHOT
import sys
import json

def CreateAccount():
  account = {}
  name = input("What is your name? ");
  address = input("What is your address? ")
  ssn = input("What is your ssn? ")
  dob = input("what is your dob? ")
  gender = input("What is your gender")

  account['AccountID'] = '004'
  account["name"] = name
  account["address"] = address
  account["ssn"] = ssn
  account["dob"] = dob
  account['gender'] = gender

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