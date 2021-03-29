import requests
import json
def lambda_handler(event, context):
    print("Event is : ")
    print(event)
    records = event['Records']
    for record in records:
        message = record['body']
        body_without_new_line = message.replace('\\n','')
        body = json.loads(body_without_new_line)
        print(body['Message'])
        response = requests.post('http://sahuppal-aws.com/persist', json=json.loads(body['Message']))
        print(response)
    print("I am updated from github!!!")
    return json.loads(body['Message'])