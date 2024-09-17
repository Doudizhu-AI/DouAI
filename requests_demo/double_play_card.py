import requests

headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json',
    'Request-Token': 'rkQXMnYs72qECOLs9mGD9',
}

json_data = {
    'history': [
        '5,6,7,8,9,10,J,Q,K,A',
        '',
        '6',
        '2',
    ],
    'self_cards': 'D,X,2,2,2,Q,Q,J,7',
    'self_out': '5,6,7,8,9,10,J,Q,K,A,6',
    'oppo_last_move': '2',
    'oppo_out': '2',
    'self_win_card_num': 0,
    'oppo_win_card_num': 1,
    'oppo_left_cards': 16,
    'passwd': 'hk25f98y',
}

response = requests.post('http://47.116.37.81:8567/ai-poker/play-card', headers=headers, json=json_data)
print(f"请求结果: ", response.json())