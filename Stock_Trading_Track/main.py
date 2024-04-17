import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

# twilio sms alert api setup

account_sid = "****"
auth_token = "***"
client = Client(account_sid, auth_token)

# stock_api_call

STOCK_API_KEY = "9F5505RYULH3MRQJ"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "IBM",
    "apikey": STOCK_API_KEY,
}

response_stock_api = requests.get(STOCK_ENDPOINT, params=stock_params)
response_stock_api = response_stock_api.json()

# getting_closing_prices

yesterdays_closing_price = response_stock_api["Time Series (Daily)"]["2024-04-16"]["1. open"]
d_b_y_closing_price = response_stock_api["Time Series (Daily)"]["2024-04-15"]["4. close"]

# price difference as float and percentage

difference = float(yesterdays_closing_price) - float(d_b_y_closing_price)
print(difference)

percentage_difference = difference / float(d_b_y_closing_price) * 100
print(f"percentage_difference = {round(percentage_difference, 3)} %")

# get news from api

if percentage_difference > 5:
    print("Get News")

NEWS_API_KEY = "914da327c88441f88c8b8dc8fd4705fd"

news_api_parameters = {
    "q": "tesla",
    "from": "2024-03-17",
    "sortBy": "publishedAt",
    "apikey": NEWS_API_KEY
}

response_news_api = requests.get(NEWS_ENDPOINT, news_api_parameters)
response_news_api = response_news_api.json()

# articles headlines
articles = response_news_api["articles"][0:3]

# articles_title_2 = response_news_api["articles"][1]["title"]
# articles_title_3 = response_news_api["articles"][2]["title"]

massage = articles

# twilio msg (articles headlines) send to relevant phone number
for i in range(3):
    message = client.messages.create(
        from_='+12513062558',
        body=response_news_api["articles"][i]["title"],
        to='+94763384586'
    )

    print(message.sid)


