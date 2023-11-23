#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 10:22:40 2022

@author: simonlesflex
"""

from finance_calendars import finance_calendars as fc
from datetime import datetime, date, timedelta
import pandas as pd
import telegram_send
import time

G_REPORTTITLE = '*FINANCE CALENDAR*'
Gsepstring = '_______________________'
GWAIT = 60

GtomorrowFlag = True
Gtodayflag = False

todaydate = date.today()
tomorrowdate = date.today() + timedelta(1)
daysdate2 = date.today() + timedelta(2)
daysdate3 = date.today() + timedelta(3)


def TelEarnings(iearn, itomorrowearn):
    TText = []
    TTomText = []
    for index, row in iearn.iterrows():
        row.marketCap = row.marketCap.replace("$", "")
        row.marketCap = row.marketCap.replace(",", "")
        T = ('Name: ' + str(row.name) + 
            '  MarketCap(mln): ' + '$' + str(round(float(row.marketCap)/1000000)) +
            '  epsForecast: ' + str(row.epsForecast) + 
            '  lastYearEPS: ' + str(row.lastYearEPS) )
        TText.append(T)
        
    for index, row in itomorrowearn.iterrows():
        row.marketCap = row.marketCap.replace("$", "")
        row.marketCap = row.marketCap.replace(",", "")
        T = ('Name: ' + str(row.name) + 
            '  MarketCap(mln): ' + '$' + str(round(float(row.marketCap)/1000000)) + 
            '  epsForecast: ' + str(row.epsForecast) + 
            '  lastYearEPS: ' + str(row.lastYearEPS) )
        TTomText.append(T)    
    
    TText.append(Gsepstring), TTomText.append(Gsepstring)
    return TText, TTomText

def TelDividend(idiv, itomorrowdiv):
    TText = []
    TTomText = []
    for index, row in idiv.iterrows():
        T = ('Name: ' + str(row.companyName) + 
            '  dividend_Ex_Date: ' + str(row.dividend_Ex_Date) +
            '  payment_Date: ' + str(row.payment_Date) + 
            '  DividendRate: ' + str(row.dividend_Rate) + '%' + 
            '  AnnualDividend' + str(row.indicated_Annual_Dividend) + '%' )
        TText.append(T)
        
    for index, row in itomorrowdiv.iterrows():
        T = ('Name: ' + str(row.companyName) + 
            '  dividend_Ex_Date: ' + str(row.dividend_Ex_Date) +
            '  payment_Date: ' + str(row.payment_Date) + 
            '  DividendRate: ' + str(row.dividend_Rate) + '%' +
            '  AnnualDividend ' + str(row.indicated_Annual_Dividend) + '%')
        TTomText.append(T)    
    
    TText.append(Gsepstring), TTomText.append(Gsepstring)
    return TText, TTomText


telegram_send.send(messages=[G_REPORTTITLE], parse_mode="markdown")


telegram_send.send(messages=['*EARNINGS Calendar Today/Tomorrow*'], parse_mode="markdown")
earnings =fc.get_earnings_today()
print(earnings[:5])
tomorrowearnings = fc.get_earnings_by_date(tomorrowdate)
print(tomorrowearnings[:5])
TText, TTomText = TelEarnings(earnings, tomorrowearnings)
if Gtodayflag:
    telegram_send.send(messages=TText)
    time.sleep(GWAIT)
if GtomorrowFlag:
    telegram_send.send(messages=TTomText)
    time.sleep(GWAIT)

telegram_send.send(messages=['*DIVIDENDS Calendar Today/Tomorrow*'], parse_mode="markdown")
dividends = fc.get_dividends_today()
print(dividends[:5])
#dividends = fc.get_dividends_by_date(datetime(2021, 8, 16, 0, 0))
tomorrowdividends = fc.get_dividends_by_date(tomorrowdate)
print(dividends[:5])
TText, TTomText = TelDividend(dividends, tomorrowdividends)
if Gtodayflag:
    telegram_send.send(messages=TText)
    time.sleep(GWAIT)
if GtomorrowFlag:
    telegram_send.send(messages=TTomText)
    time.sleep(GWAIT)


ipos = fc.get_priced_ipos_this_month()
print(ipos[:5])

ipos = fc.get_priced_ipos_by_month(datetime(2021, 7, 1, 0, 0))
print(ipos[:5])

ipos = fc.get_filed_ipos_this_month()
print(ipos[:5])

ipos = fc.get_filed_ipos_by_month(datetime(2021, 7, 1, 0, 0))
print(ipos[:5])

ipos = fc.get_withdrawn_ipos_this_month()
print(ipos[:5])

ipos = fc.get_withdrawn_ipos_by_month(datetime(2021, 7, 1, 0, 0))
print(ipos[:5])

ipos = fc.get_upcoming_ipos_this_month()
print(ipos[:5])

ipos = fc.get_upcoming_ipos_by_month(datetime(2021, 7, 1, 0, 0))
print(ipos[:5])

splits = fc.get_splits_today()
print(splits[:5])

splits = fc.get_splits_by_date(datetime(2021, 8, 16, 0, 0))
print(splits[:5])

div_hist = fc.get_div_hist_per_stock('AAPL')
print(div_hist)

div_hist = fc.get_div_hist_per_etf('VIG')
print(div_hist)