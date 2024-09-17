import requests

headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json',
    'Request-Token': 'rkQXMnYs72qECOLs9mGD9',
}

json_data = {
    'self_cards': 'D,X,2,2,A,A,K,K,Q,J,10,9,8,7,7,6,6',
    'call_time': 1,
    'oppo_call': 0,
    'passwd': 'hk25f98y',
}

response = requests.post('http://47.116.37.81:8567/ai-poker/call-landlord', headers=headers, json=json_data)
print(f"请求结果: ", response.json())
