import requests

headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json',
    'Request-Token': 'rkQXMnYs72qECOLs9mGD9',
}

json_data = {
    'player_position': 'landlord_up',
    'player_hand_cards': '2,2,2,A,5,5,5,6,6,6,7,7,7,8,8,9,9',
    'three_landlord_cards': 'T,Q,2',
    'card_play_action_seq': [
        '5,T,T,T',
        '6,J,J,J',
    ],
    'played_cards_dict': {
        'landlord': '5,T,T,T',
        'landlord_down': '6,J,J,J',
        'landlord_up': '',
    },
    'last_move_dict': {
        'landlord': '5,T,T,T',
        'landlord_down': '6,J,J,J',
        'landlord_up': '',
    },
    'passwd': 'hk25f98y',
}

response = requests.post('http://47.116.37.81:8568/ai-poker-triple/play-card', headers=headers, json=json_data)
print(f"请求结果: ", response.json())
