import json
import boto3
client =boto3.client('dynamodb')

def lambda_handler(event, context):
 
    response = client.create_table(
        AttributeDefinitions=[
            {
                'AttributeName': 'CustomerID',
                'AttributeType': 'S',
            }, 
            {
                'AttributeName': 'Product',
                'AttributeType': 'S',
            },
        ],
        TableName='RetailSales0stehiurhaiti2022',
        KeySchema=[
            {
                'AttributeName': 'CustomerID',
                'KeyType': 'HASH',
            },
            {
                'AttributeName': 'Product',
                'KeyType': 'RANGE',
            },
        ],
        ProvisionedThroughput= {
                'ReadCapacityUnits': 1,
                'WriteCapacityUnits': 1,
            }
    )
    print(response)
    
# then on another lambda function after creation RESPONSE (cant be on the same)

import json
import boto3
client = boto3.client('dynamodb')
def lambda_handler(event, context):
    response = client.put_item(
    TableName='RetailSales0stehiurhaiti2022',
    Item={
        'CustomerID': {
            'S': '001',
        },
        'Product': {
            'S': 'Mangoes',
        },
        'Quantity': {
            'N': '100',
        },
        'Address': {
            'S': '192 preway Trinity',
        },
    },
    )
    print(response)
