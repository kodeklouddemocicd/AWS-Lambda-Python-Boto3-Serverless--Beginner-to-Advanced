#must have s3 and dynamodb: partition-key: CustomerID, sort-key Product
import json
import boto3

client =boto3.client('s3')
dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    response = client.get_object(
    Bucket='s3bucketforlamdanddynamodb101',## CHANGE
    Key='DynamoDB_Samplefile.json', ## CHANGE 
   )
 # convert from streaming data to bytes
    json_data = response['Body'].read()
    #print(json_data)
    #print(type(json_data))

 # convert from byte to string 
    data_string = json_data.decode('UTF-8')
    #print(data_string)
    #print(type(data_string))

 # convert from string to json
    data_dict = json.loads(data_string)
    print(data_dict)
    print(type(data_dict))

  # insert data to dynamodb (also create the boto3.resource and got example from documentation dynamodb not client or resource tabs)
    table = dynamodb.Table('dynamodbfors3andlamda') ##CHANGE 
    
    table.put_item(Item=data_dict)

## lastly add s3 as a trigger to lambda for all events >> now when uploading files it will active the lambda and covert string to dict for dynamodb