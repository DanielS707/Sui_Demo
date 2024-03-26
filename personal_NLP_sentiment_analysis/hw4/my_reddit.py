#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Sui
"""

import pickle
import praw
import numpy as np
from utils import *
import pandas as pd
import pytz
from datetime import datetime
from collections import deque
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

subreddit_channel = 'politics'
the_path = "D:/Git_Desk/data_works/NLP_Natural_Language_Process/hw4/"


fetch_creds = pd.read_csv(the_path + "creds.csv")

reddit = praw.Reddit(
     client_id=fetch_creds.client_id[0],
     client_secret=fetch_creds.client_secret[0],
     user_agent="testscript by u/fakebot3",
     username=fetch_creds.username[0],
     password=fetch_creds.password[0],
     check_for_async=False
 )

vectorize = read_pickle(the_path,'vectorizer')
pca = read_pickle(the_path,'pca')
#classify = read_pickle(the_path,'my_model')
with open('my_model.pk', 'rb') as f:
    classify = pickle.load(f)

# reddit = praw.Reddit(
#      client_id="",
#      client_secret="",
#      user_agent="testscript by u/fakebot3",
#      username="",
#      password="",
#      check_for_async=False
#  )

print(reddit.read_only)
import warnings
warnings.filterwarnings("ignore")

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
    
for comment in reddit.subreddit(subreddit_channel).stream.comments():
    tmp_df = get_reddit_data(comment)
    #print (tmp_df["body"])
    text_r = tmp_df['body']
    text_cl = clean_text(text_r)
    text_sw = rem_sw(text_cl)
    text_st = stem_fun(text_sw)

    X = vectorize.transform([text_st])
    X_p = pca.transform(X.toarray())
    #print (tmp_df["body"])
    print(classify.predict(X_p))
    print(classify.predict_proba(X_p))
    #my_sentiment = score_sentiment(text_st)