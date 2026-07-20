import os
import json
import requests

# Required environment variables:
# - TRADING_API_KEY
# - TRADING_API_SECRET

def run(payload: dict) -> dict:
    try:
        # Extract trading parameters from payload
        symbol = payload.get('symbol')
        action = payload.get('action')  # 'buy' or 'sell'
        amount = payload.get('amount')

        # Validate input
        if not symbol or not action or amount is None:
            return {'error': 'Missing required parameters: symbol, action, amount'}

        # Prepare API request
        api_key = os.environ.get('TRADING_API_KEY')
        api_secret = os.environ.get('TRADING_API_SECRET')
        url = f'https://api.tradingplatform.com/v1/{action}'
        headers = {'Authorization': f'Bearer {api_key}', 'Content-Type': 'application/json'}
        data = {'symbol': symbol, 'amount': amount}

        # Make the API call
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()

        # Return the response
        return response.json()
    except Exception as e:
        return {'error': str(e)}