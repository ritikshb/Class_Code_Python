
from multiprocessing.connection import Client
import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
account_sid = "ACe3a61223f7f65919225612bf059e8107"
auth_token = "2a2fee8b1bfa9eaf63ea6edbf63c72c6"
STOCK_KEY = "KD6N2PWY9IT7C0MH"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_KEY = "5b2cc29e97b2456fb2e721ce89a43a49"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

parameter_stock = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "outputsize":"compact",
    "apikey":STOCK_KEY
}
parameter_news = {
    'q': COMPANY_NAME,
    'apikey': NEWS_KEY
}

## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

stock = requests.get(url=STOCK_ENDPOINT,params=parameter_stock)
stock_data = stock.json()["Time Series (Daily)"]
stock_list = [value for (key,value) in stock_data.items()]
stock_yesterday = float(stock_list[0]['4. close'])
print(stock_yesterday)
stock_day_before_yesterday = float(stock_list[1]['4. close'])
print(stock_day_before_yesterday)
positive_difference = abs(stock_yesterday-stock_day_before_yesterday)
print(positive_difference)

percentage = (positive_difference/stock_yesterday)*100
print(percentage)
#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if percentage> 0:
    news = requests.get(url=NEWS_ENDPOINT,params=parameter_news)
    news_data = news.json()
    # print(news_data)
    # news_yesterday = [news_data["articles"][new_value] for new_value in range(0,3)]
    three_news = news_data["articles"][:3]
        # print(news_data["articles"][:3])

        ## STEP 3: Use twilio.com/docs/sms/quickstart/python
        #to send a separate message with each article's title and description to your phone number. 

    #TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
    news_message = [f'Headline: {i["title"]} \nDescription: {i["description"]}' for i in three_news]
    # print(news_message)
    client = Client(account_sid,auth_token)
    for article in news_message:
        message = client.messages.create(
                                        body = article,
                                        from_ = "+18596597910",
                                        to= "+919119059393"
                                        )


