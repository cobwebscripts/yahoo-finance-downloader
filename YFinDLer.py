# Copyright (c) 2023 Purchaser of cobwebscripts.com in March 2023.
# Subject to the MIT (Expat) license.
# See file LICENSE for full license details.

# Yahoo Finance Downloader
# Version: 2023_03_27_v1
import datetime
import urllib.request

###Define fuctions###
def epochConvert(day):
    epoch = datetime.date(1970, 1, 1)
    secondsInDay = 86400
    diff = day - epoch #diff is a timedelta object
    seconds = (diff.days) * secondsInDay
    return seconds

def createDate():
    year, month, day = input("").split()
    year = int(year)
    month = int(month)
    day = int(day)
    term = datetime.date(year, month, day)
    return term

def intervalChoice(intChoice):
    if (intChoice == 1):
        return "1d"
    elif (intChoice == 2):
        return "1wk"
    elif (intChoice == 3):
        return "1mo"
    
def queryYahoo(ticker, start, end, interval):
    url = "https://query1.finance.yahoo.com/v7/finance/download/"
    url += ticker
    url += "?period1="
    url += str(start)
    url += "&period2="
    url += str(end)
    url += "&interval="
    url += interval
    url += "&events=history&includeAdjustedClose=true"
    
    fileType = ".csv"
    
    try:
        urllib.request.urlretrieve(url, ticker + fileType)
        print("Download succeeded")
    except:
        print("Download failed")


###CONSTANTS###
#The end goal it to convert to epoch time in seconds
#So we skip conversion and make the start a large negative value in epoch time
#This -9999999999 seconds translates to Feb 10, 1653
OLDEST = -9999999999

#Grab the current local time of system
#Set it as our end parameter
#I know this breaks the definition of a constant but logically it acts as one in this case
NEWEST = datetime.date.today()
NEWEST = epochConvert(NEWEST)
    

###DRIVER###
wantAll = int(input('''What date range
[1] All
[2] Manual Entry
Just enter number: '''))

if (wantAll == 1):
    first = OLDEST
    second = NEWEST

elif(wantAll == 2):
    print("Start date (YYYY MM DD): ", end="")
    first = createDate()

    print("End date (YYYY MM DD): ", end="")
    second = createDate()

    first = epochConvert(first)
    second = epochConvert(second)

tick = input("Ticker (per Yahoo Finance): ")
print('''What time scale
[1] Day
[2] Week
[3] Month
Just enter number: ''', end="")
timing = int(input(""))
timing = intervalChoice(timing)

queryYahoo(tick, first, second, timing)
input("Press any key to exit...")