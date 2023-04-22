# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 17:02:15 2023

@author: suisx
"""
#create my path for read and write

the_path = 'D:/Git_Desk/data_works/NLP_Natural_Language_Process/project/tweets/'
out_path = 'D:/Git_Desk/data_works/NLP_Natural_Language_Process/project/output/'

import pandas as pd
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
import re

def clean_text(str_in):
    tmp = re.sub(r'http\S+', '', str_in).replace("  ", " ")
    tmp = re.sub("[^A-Za-z']+", " ", tmp).lower().strip().replace("  ", " ")
    return tmp

def stem_fun(txt_in):
    stem_tmp = PorterStemmer()
    tmp = [stem_tmp.stem(word) for word in txt_in.split()]
    tmp = ' '.join(tmp)
    return tmp

def rem_sw(var_in):
    sw = stopwords.words("english")
    tmp = var_in.split()
    tmp_ar = [word_t for word_t in tmp if word_t not in sw]
    tmp_o = ' '.join(tmp_ar)
    return tmp_o



# Clean the text in the second column and remove stop words
#df_tw.iloc[:, 1] = df_tw.iloc[:, 1].apply(clean_text).apply(rem_sw)


# Write the cleaned data to a new CSV file
#df_tw.to_csv(out_path + "cleaned_tweets.csv", index=False)

# Read the CSV file using pandas and keep only the first 4 columns(Tweeting date, context, user, user_location)
tmp_tw = pd.read_csv(the_path + "tweets0408.csv", usecols=[0,1,2,3])
#tmp_tw = pd.read_csv(the_path, usecols=[0, 1, 2, 3])
tmp_tw.iloc[:, 1] = tmp_tw.iloc[:, 1].apply(lambda x: clean_text(str(x)))
tmp_tw.iloc[:, 1] = tmp_tw.iloc[:, 1].apply(lambda x: stem_fun(x))
tmp_tw.iloc[:, 1] = tmp_tw.iloc[:, 1].apply(lambda x: rem_sw(x))


tmp_tw.to_csv(out_path + "tw_output.csv", index=False)
#df_tw = tmp_tw.to_csv(out_path + 'output.csv', index=False)


"""
the_data["body_sw_stem"] = the_data.body_sw.apply(stem_fun)
the_data["cnt_sw_stem"] = the_data.body_sw_stem.apply(wrd_cnt)
total_unique_body_sw_stem = wrd_cnt(
    the_data.body_sw_stem.str.cat(sep=" "))

xform_d = vec_fun(the_data.body_sw_stem, 1, 1, "vec", out_path)

chi_fun_out = chi_fun(xform_d, the_data.label, 100, out_path, "chi")
"""