# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 18:59:23 2023

@author: suisx
"""
"""
Please create a function (def) called gen_senti that Tokenizes arbitrary text and 
compares each token with the positive and negative lexicons of each dictionary and 
outputs the sentiment score, S.  
Positive and negative words, pw and nw, count as a score of 1 and -1 respectively for each word matched. 

The total count for pw and nw are pc and nc, respectively.  
Each message sentiment, S, is normalized between -1 and 1.  
Any text that does not any positive AND negative words would have to be ignored, and not scored. (60 points)
"""
# Get user input from the console
user_input = input("Enter some text: ")

def gen_senti(text):
    # Load positive and negative lexicons
    with open('D:/Git_Desk/data_works/NLP_Natural_Language_Process/hw2/positive-words.txt', 'r') as f:
        pw = set([line.strip() for line in f])

    with open('D:/Git_Desk/data_works/NLP_Natural_Language_Process/hw2/negative-words.txt', 'r') as f:
        nw = set([line.strip() for line in f])

    # Tokenize the input text
    tokens = list(text.split())
    print(tokens)

    # Initialize counts for positive and negative words
    pc_count = 0
    nc_count = 0

    # Iterate over the tokens and count positive and negative words
    for tk in tokens:
        if tk in pw:
            pc_count += 1
        elif tk in nw:
            nc_count += 1
    # Calculate sentiment score as the difference between positive and negative counts
    sentiment = pc_count - nc_count

    return sentiment

sentiment_score = gen_senti(user_input)

if sentiment_score is not None:
    print("Sentiment score:", sentiment_score)
else:
    print("No positive or negative words found in the input text.")



"""
    # If there are no positive or negative words, return None
    if pc == 0 and nc == 0:
        return None

    # Compute the sentiment score
    S = (pc - nc) / (pc + nc)

    return S

# Call the gen_senti function with the user input
sentiment_score = gen_senti(user_input)

# Print the sentiment score if it's not None
if sentiment_score is not None:
    print("Sentiment score:", sentiment_score)
else:
    print("No positive or negative words found in the input text.")
    """