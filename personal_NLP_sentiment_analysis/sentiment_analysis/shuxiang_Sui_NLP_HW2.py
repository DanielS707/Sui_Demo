# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 02:22:32 2023

@author: DanielS
"""
#Quesiton 1:
#import library
import pandas as pd
import numpy as np
import nltk
nltk.download('bader_lexicon')
from nltk.sentiment import SentimentIntensityAnalyzer

def gen_vader(test_input):
    analyzer = SentimentIntensityAnalyzer()
    all_score = analyzer.polarity_scores(test_input)
    return all_score["compound"]

def gen_senti(test_input):
    # open the text file and read its contents
    with open('C:/Users/DanielS/Desktop/NLP_Natural_Language_Processing/file/hw2/positive-words.txt', 'r') as file:
        pos_list = file.read()
    with open('C:/Users/DanielS/Desktop/NLP_Natural_Language_Processing/file/hw2/negative-words.txt', 'r') as file:
        neg_list = file.read()
        
    # split the file into a list of words
    pos_list = pos_list.split()
    neg_list = neg_list.split()
    
    #test content: the time of gloom of 2-faced world, A+, holy, good one!
    # define a test input:
    import re
    #keep the characters in pos and neg words such as + -.
    test_input_clean = re.sub("[^A-Za-z0-9+-]+", " ", test_input).lower().strip()
    test_split = test_input_clean.split()
    
    #count the positive and negative words:
    test_pos = []
    test_neg = []
    
    for word in test_split:
        # print the pos word in test input
        if word in neg_list:
            test_neg.append(word)
        elif word in pos_list:
            test_pos.append(word)
    
    #calculate and count message score:
    pc = len(test_pos)
    nc = len(test_neg)
    S = (pc-nc)/(pc+nc) if pc+nc !=0 else print("No sentiment score for this text. \n")
    print(test_pos)
    print(test_neg)
    print("========================")
    print("Sentiment Score: " + str(S) + "\n There are positive words(pc): " + str(pc) + ", and negative words(pc):" + str(nc))

    return S


#Question 2

#create the_path for corpuses file:
the_path = 'C:/Users/DanielS/Desktop/GitHub_Clone/data_works/NLP_Natural_Language_Process/corpuses/'
def clean_text(str_in):
    import re
    tmp = re.sub("[^A-Za-z']+"," ",str_in).lower().strip().replace("  ", " ")
    return tmp

def file_clean(path_in):
    f = open(path_in, encoding="UTF-8")
    tmp = f.read()
    f.close()
    tmp = clean_text(tmp)
    return tmp

def read_files(path_in):
    import os
    import pandas as pd
    file_list = pd.DataFrame()
    for root, dirs, files in os.walk(path_in, topdown=False):
        for name in files:
            try:
                t_path = root + "/" + name  #this made the file_p as the key, with format of root/file_name
                file_p = file_clean(t_path)
                t_p = root.split("/")[-1:][0]
                #remove the databody with no content
                if len(file_p) > 0:
                    file_list = file_list.append(
                        {"body": file_p, "label": t_p}, ignore_index=True)
            except:
                print (t_path)
                pass
    return file_list

#get the Question 2 data from file in the_path:
the_data = read_files(the_path)
#generate a column of scores named simple_senti, by function gen_senti:
the_data["simple_senti"] = the_data.body.apply(lambda x: gen_senti(x))
#generate a column of scores named vader, by gen_vader:
the_data["vader"] = the_data.body.apply(gen_vader)

# Calculate mean, median, and standard deviation for "simple_senti" and "vader" column
get_mean = the_data[["simple_senti", "vader"]].mean()
get_median = the_data[["simple_senti", "vader"]].median()
get_std_dev = the_data[["simple_senti", "vader"]].std()

print("mean for 2 scores: \n" + get_mean.round(3).to_string())
print("median for 2 scores: \n" + get_median.round(3).to_string())
print("standard_deviation for 2 scores: \n" + get_std_dev.round(3).to_string())
print("The End.")