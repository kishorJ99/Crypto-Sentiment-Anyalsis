# Reload the web page and execute this cell
import sys
print("User Current Version:-", sys.version)

import datetime
import snscrape.modules.twitter as sntwitter
import pandas as pd

def sentimentAnaylasis(input):
  return input

start_date = datetime.date(2020, 7, 1)
tmp_start_date = datetime.date(2020, 7, 1)
end_date = datetime.date(2021, 7, 1)
delta = datetime.timedelta(days=1)

search_list = ['AAVE', 'BNB', 'BTC', 'ADA', 'LINK', 'ATOM', 'CRO', 'DOGE', 'EOS', 'ETH', 'MIOTA', 'LTC', 'XEM', 'DOT', 'SOL', 'XLM', 'USDT', 'TRX', 'USDC', 'UNI', 'WBTC', 'XRP', 'XMR']

# 'BTC', 'ETH', 'XRP', 'EOS', 'LTC', 'BCH', 'BNB' , 'XLM', 'TRX' Done XMR Errror | too add SOL, AVAX, DOGE, DOT, ADA, WBTC, TRX,

for idx, coin in enumerate(search_list):
  print('Working on ' + str(idx))

  tweets_list = []

  maxTweets = 30
  tmp_start_date = datetime.date(2020, 7, 1)

  while tmp_start_date <= end_date:
    print(tmp_start_date)

    searchQuery = '#' + coin + ' since:' + str(tmp_start_date) + ' until:' + str(tmp_start_date + delta)

    # Using TwitterSearchScraper to scrape data 
    size = 0

    try:
        for i,tweet in enumerate(sntwitter.TwitterSearchScraper(searchQuery, top=True).get_items()):
            if i>maxTweets:
                break
            tweets_list.append([tweet.date, tweet.id, tweet.content])
            size += 1
        
        if size < maxTweets:
            print('Less than ' + str(maxTweets) + ' tweets (' + str(size) + ') for search ' + searchQuery)

    except Exception as e:
        print('Error: ' + str(e))



    tmp_start_date += delta

  tweets_df = pd.DataFrame(tweets_list, columns=['Datetime', 'Tweet Id', 'Text'])

  tweets_df.to_csv(coin + '_since:' + str(start_date) + '_until:' + str(end_date) + '.csv', index=False)

  # # Display first 5 entries from dataframe
  # tweets_df.head(10)