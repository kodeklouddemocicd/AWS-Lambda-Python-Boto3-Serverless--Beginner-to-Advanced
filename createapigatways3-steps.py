import json
import boto3
client = boto3.client('s3')

def lambda_handler(event, context):
    bucket= event['bucket']
    key=event['key']

    response = client.get_object(
    Bucket=bucket,
    Key= key,
)

# converts streaming to bytes
    data_bytes = response['Body'].read()
    #print(data_bytes)
    #print(type(data_bytes))

# converts bytes to string 
    data_string = data_bytes.decode("utf-8")
    #print(data_string)
    #print(type(data_string))

# converts string to dict
    data_dict = json.loads(data_string)
    #print(data_dict)
    #print(type(data_dict))
    return {
    'statusCode': 200,
        'body':data_dict
}

# step 2 = create test event after deploying code

{
  "bucket": "apigatways3p1",
  "key": "Use+Case+2_Bucket1_Json.json"
}

# step 3 create the api resource add as a trigger on lamdba 
# step 6 for url interagration

{
  "bucket": "$input.params('bucket')",
  "key": "$input.params('key')"
}
