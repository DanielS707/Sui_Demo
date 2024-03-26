#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Sui
"""

import praw
import pandas as pd
import pytz
from datetime import datetime
from collections import deque
import numpy as np
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

the_path = "C:/Users/pathouli/myStuff/academia/columbia/socialSciences/GR5067/2022_fall/code/"
subreddit_channel = 'makemesmile'

fetch_creds = pd.read_csv(the_path + "creds.csv")

reddit = praw.Reddit(
     client_id=fetch_creds.client_id[0],
     client_secret=fetch_creds.client_secret[0],
     user_agent="testscript by u/fakebot3",
     username=fetch_creds.username[0],
     password=fetch_creds.password[0],
     check_for_async=False
 )

print(reddit.read_only)

def conv_time(var):
    tmp_df = pd.DataFrame()
    tmp_df = tmp_df.append(
        {'created_at': var},ignore_index=True)
    tmp_df.created_at = pd.to_datetime(
        tmp_df.created_at, unit='s').dt.tz_localize(
            'utc').dt.tz_convert('US/Eastern') 
    return datetime.fromtimestamp(var).astimezone(pytz.utc)

def get_reddit_data(var_in):
    import pandas as pd
    tmp_dict = pd.DataFrame()
    tmp_time = None
    try:
        tmp_dict = tmp_dict.append({"created_at": conv_time(
                                        var_in.created_utc)},
                                    ignore_index=True)
        tmp_time = tmp_dict.created_at[0] 
    except:
        print ("ERROR")
        pass
    tmp_dict = {'msg_id': str(var_in.id),
                'author': str(var_in.author),
                'body': var_in.body, 'datetime': tmp_time}
    return tmp_dict
  
def score_sentiment(var):
    senti_score = round(
            sentiment_score_var.polarity_scores(var)['compound'], 4)
    var = var.lower()
    the_sentiment_dict['sentiment'].pop()
    the_sentiment_dict['sentiment'].appendleft(senti_score)    
    return the_sentiment_dict  
  
the_look_back = 100

global the_sentiment_dict
senti_score = [0] * the_look_back
the_sentiment_dict = {'sentiment':deque(senti_score)}
global sentiment_score_var
sentiment_score_var = SentimentIntensityAnalyzer()
  
for comment in reddit.subreddit(subreddit_channel).stream.comments():
    tmp_df = get_reddit_data(comment)
    #print (tmp_df["body"])
    my_sentiment = score_sentiment(tmp_df["body"])
    print ("sentiment trend", np.mean(my_sentiment["sentiment"]))
    
    
    
    
    