import pandas as pd
import numpy as ny
import smtplib
import yfinance as yf
from datetime import date
import datetime
import pytz
from email.mime.text import MIMEText
import time
from IPython import embed
import pywhatkit as whatsapp

api_key = '' #alphapAdvantage API Key

print("StockMarket Program is Started...Please visit www.youtube.com/AbhishekBhuva")

x = datetime.datetime.now()
print("Current Date and Time : ",x)
print("Curret Date, time and timestamp and Day", x.strftime('%Y/%m/%d %I:%M:%S %p:%A'))
y = datetime.datetime.now() + datetime.timedelta(minutes = 1)

yesterday = print(x.day-1)
today = print(x.day)
month = print(x.month-11)
#print(x.month)
#print(x.year)
#define the ticker symbol
tickerSymbol = ['AAPL','ROKU']
#tickerSymbol = ['CAKE','TSLA']
print(tickerSymbol)

position = 0
while True:
    if position >= len(tickerSymbol):
        break
    #get data on this ticker
    tickerData = yf.Ticker(tickerSymbol[position])
    #get the historical prices for this ticker
    tickerDf = tickerData.history(period='1d', start=yesterday, end=today)
    print(tickerSymbol[position])
    type(tickerDf)
    #tickerDf = str(tickerDf)
    tickerDf = tickerSymbol[position] + " : Ticker reported by yfinance, visit: www.youtube.com/AbhishekBhuva \n" + str(tickerDf)
    #tickerDf = ("Below is " + str(tickerSymbol[position]) + " Ticker Data of Today(" + x.strftime('%m/%d/%Y-%I:%M:%S-%p:%A') + ")\n" + tickerDf)
    type(tickerDf)
    x = datetime.datetime.now()
    y = datetime.datetime.now() + datetime.timedelta(minutes = 1)
    print("y : ",y)
    if (x.strftime('%p') == 'PM'):
        x_minute = int(x.strftime('%I'))+12
        print("x_minute : ", x_minute)
    else:
        x_minute = int(x.strftime('%I'))
        print("x_minute : ", x_minute)
    if (y.strftime('%S') > '50'):
        time.sleep(15)
    else:
        print("y_seconds : ", y.strftime('%S'))
    print(tickerDf)
    whatsapp.sendwhatmsg("+16178038810",tickerDf,x_minute,int(y.strftime('%M')))
    position = position + 1
print("All Ticker Listed SuccessFully...Please visit www.youtube.com/AbhishekBhuva")


#html_table = tickerDf.to_html()

#tickerDf.write.csv("stockmarket.csv")

#print(html_table)

sender_email ="ruchivihal@gmail.com"
receiver_email = "sbaldha@mail.com,abhuva@my.com"
password = "RuchiVihal@2020"
current_time = str(x.year)
print("Current year is : ", current_time)
msg= "Message from StockMarket.py. " + x.strftime('%Y/%m/%d %I:%M:%S %p: %A')
message = str(msg)
print(message)
'''
subject = "Data of StockMarket"

#body = "<h1>Dear ABC</h1>This is the Table <br><br>   "+html_table+"  <br><br>Thanks"
#text = MIMEText(tickerDf)
#full = message + "\n" TSLA
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender_email,password)
print("Login Success.")
server.sendmail(sender_email,receiver_email,message)
print("Email has been sent to: " + receiver_email)
'''
#print("Company = Amazon ")
#data, meta_data = ts.get_intraday(symbol='AMZN', interval = '1min', outputsize = '10')
#print(data)
