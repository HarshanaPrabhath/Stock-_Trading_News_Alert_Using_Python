# Stock-_Trading_News_Alert_Using_Python

# Stock News Alert System

The Stock News Alert System is a Python script that retrieves stock market data for a specific company and sends an SMS alert with relevant news articles if the stock price fluctuates significantly.

## Components

### 1. Stock Data Retrieval

The script fetches daily stock market data using the Alpha Vantage API. It retrieves the opening price of the current day (`yesterdays_closing_price`) and the closing price of the previous day (`d_b_y_closing_price`) for the specified stock symbol (`TSLA` for Tesla Inc).

### 2. Price Difference Calculation

It calculates the difference (`difference`) and percentage difference (`percentage_difference`) between the opening price of the current day and the closing price of the previous day. If the percentage difference is greater than 5%, the script proceeds to fetch relevant news articles.

### 3. News Data Retrieval

Using the News API, the script fetches news articles related to the specified company (Tesla Inc). It filters articles published after a certain date (`from` parameter) and sorts them by publication date (`sortBy` parameter).

### 4. SMS Alert

If the stock price fluctuation exceeds the threshold (5%), the script sends an SMS alert to a specified phone number using the Twilio API. It sends the titles of the top 3 news articles related to the company.

## Dependencies

- **Requests**: HTTP library for making API requests.
- **Twilio**: Library for interacting with the Twilio API for sending SMS alerts.
- **Alpha Vantage API**: Provides stock market data including daily stock prices.
- **News API**: Offers access to a vast database of news articles from various sources.

## Setup

1. Obtain API keys for Alpha Vantage, News API, and Twilio.
2. Install the required Python libraries: `requests`, `twilio`.
3. Replace the placeholders (`****`) with your API keys, Twilio credentials, and phone numbers.
4. Run the Python script to monitor stock price fluctuations and receive SMS alerts for relevant news articles.

