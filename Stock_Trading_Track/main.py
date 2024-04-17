import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

# stock_api_call

STOCK_API_KEY = "UOPCN0EKYN9WQD01"

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
print(response_news_api["articles"][0:3]["title"])
print(response_news_api["articles"][1]["title"])
print(response_news_api["articles"][2]["title"])

# TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


## STEP 3: Use twilio.com/docs/sms/quickstart/python
# to send a separate message with each article's title and description to your phone number.

# TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

# TODO 9. - Send each article as a separate message via Twilio.


# Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
