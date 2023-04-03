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


def stem_fun(txt_in):
    from nltk.stem import PorterStemmer  #add doc after to see what excit there
    stem_tmp = PorterStemmer()
    tmp = [stem_tmp.stem(word) for word in txt_in.split()]
    tmp = ' '.join(tmp)
    return tmp
    #tmp = list()
    #for word in txt_in.split()
        #tmp.append(stem_tmp.stem(word))


def vec_fun(df_in, m_in, n_in, name_in, out_p_in):
    #turn into a function called vec_fun and give user avility to set arbitrary ngrams.
    #and an arbitrary name for the saved pk object.
    import pandas as pd
    from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
    #build a function that allows a user to switch CV or TF-IDF:
    if name_in == "vec":
        xform = CountVectorizer(ngram_range=(m_in, n_in))
    else:
        xform = TfidfVectorizer(ngram_range=(m_in, n_in))

    #produce fitted transformed data
    xform_data = pd.DataFrame(xform.fit_transform(df_in).toarray())
    #be careful with toarray because it is memory saving.
    xform_data.columns = xform.get_feature_names() #get feature and add it as the name to the column
    write_pickle(xform, out_p_in, name_in) 
    return xform_data


def chi_fun(df_in, label_in, k_in, path_out, name_in):
    from sklearn.feature_selection import chi2
    from sklearn.feature_selection import  SelectKBest
    import pandas as pd
    feat_sel = SelectKBest(score_func=chi2, k=k_in)
    dim_data = pd.DataFrame(feat_sel.fit_transform(
        df_in, label_in))
    feat_index = feat_sel.get_support(indices = True)
    feature_names = df_in.columns[feat_index]
    dim_data.columns = feature_names
    write_pickle(feat_sel, path_out, name_in)
    return dim_data

def jaccard_dist(corp_1, corp_2):
    intersection = set(corp_1.split()).intersection(corp_2.split())
    union = set(corp_1.split()).union(set(corp_2.split()))
    return len(intersection) / len(union)

def cos_sim_fun(df_a, df_b, label_in):
    #0 means no similarity and 1 means exact the same.
    from sklearn.metrics.pairwise import cosine_similarity
    import pandas as pd
    import numpy as np
    cos_matrix = pd.DataFrame(cosine_similarity(
        df_a, df_b))
    cos_matrix.index = label_in
    cos_matrix.columns = label_in
    np.array(cos_matrix)
    print(np.average(np.array(cos_matrix)))
    return 


