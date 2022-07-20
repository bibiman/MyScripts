import json

print ('loading function')

def lambda_handler(event, context): 
    return event
    
    #1. Get the values from the parameters
    tran_id    = event['queryStringParameters']['id']
    tran_key   = event['queryStringParameters']['key']
    tran_value = event['queryStringParameters']['value']
    
    #2. Construct the response
    tran_resp = {}
    tran_resp['id']    = tran_id
    tran_resp['key']   = tran_key
    tran_resp['value'] = tran_value
    
    #3 contruct the response object
    resp = {}
    resp['statusCode']              = 200
    resp['headers'] {}
    resp['headers']['Content-Type'] = "application/json"
    resp['body']                    = json.dumps(tran_resp)
    
    #4 return json
    return resp