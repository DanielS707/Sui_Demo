# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 18:43:11 2023

@author: pathouli
last_update: 02_20_2023
"""

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

def wrd_dictionary(df_in, col_name_in):
    import collections
    my_dictionaty_t = dict()
    for topic_t in df_in.label.unique():
        tmp = df_in[df_in.label == topic_t]
        tmp = tmp[col_name_in].str.cat(sep=" ")
        wrd_freq = collections.Counter(tmp.split())
        my_dictionaty_t[topic_t] = wrd_freq
    return my_dictionaty_t



#check the stopwords words and updating utils that did we kick out some stop words?

"""remove stopwords"""
def rem_sw(var_in):
    import nltk
    from nltk.corpus import stopwords
#import english stopwords
    sw = stopwords.words("english")
    tmp = var_in.split()
    """
    tmp_ar = list() #create a append list add the words not in the stopwords list.
    for word_t in tmp:
        if word_t not in sw:
            tmp_ar.append(word_t)
    """
    tmp_ar = [word_t for word_t in tmp if word_t not in sw]
    tmp_o =' '.join(tmp_ar)
    return tmp_o

print("\nStop words are removed.")


def write_pickle(obj_in, path_in, name_in):
    import pickle
    pickle.dump(obj_in, open(path_in + name_in + '.pk', 'wb')) #pk doesn't matter but just meaning package
#wb is write

def read_pickle(path_in, name_in):
    import pickle
    the_data_t = pickle.load(open(path_in + name_in + ".pk", "rb")) #rb is read
    return the_data_t