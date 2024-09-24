import requests
from datetime import datetime, timedelta

def get_currency_value(curr1, curr2):
    url = f"https://api.tiingo.com/tiingo/daily/{curr1}{curr2}/prices"
    start_date = (datetime.today() - timedelta(days=1)).strftime("%Y-%m-%d")
    token = "379675600c272f6163caae182d8894f26cd9bddc"

    response = requests.get(url, params={'startDate':start_date, 'token':token})

    if response.status_code == 200:
        data = response.json()

        date = data[0].get('date')[:10]
        adj_open = data[0].get('adjOpen')
        adj_close = data[0].get('adjClose')
        adj_high = data[0].get('adjHigh')
        adj_low = data[0].get('adjLow')


        result_sentence = (f"On {date}, {curr1.upper()}/{curr2.upper()} opened at {adj_open}, "
                           f"reached a high of {adj_high}, a low of {adj_low}, and closed at {adj_close}.")

        return result_sentence
    else:

        print(f"Error : {response.status_code}, {response.text}")
        return None