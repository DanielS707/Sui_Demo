# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 18:08:40 2023

@author: pathouli
"""

from func.utils import *

the_path = "C:/Users/pathouli/myStuff/academia/columbia/socialSciences/GR5067/2023_spring/data/"
out_path = "C:/Users/pathouli/myStuff/academia/columbia/socialSciences/GR5067/2023_spring/output/"

the_data = read_files(the_path)

topic_fun = wrd_dictionary(the_data, "body")

the_data["body_sw"] = the_data.body.apply(rem_sw)

#in class exercise create function that creates a new column called "cnt"
#which will be the count of UNIQUE tokens in each corpus
#allow user to pass in a specific column

the_data["cnt"] = the_data.body.apply(wrd_cnt)
the_data["cnt_sw"] = the_data.body_sw.apply(wrd_cnt)

total_unique_body = wrd_cnt(the_data.body.str.cat(sep=" "))
total_unique_body_sw = wrd_cnt(the_data.body_sw.str.cat(sep=" "))

#stemming truncates words to their root word
#some root words dont show up the english

#build a function that returns a arbitrary corpus with all
#tokens stemmed and rejoin the text as one string
#apply this to a new column called body_sw_stem for ALL corpuses
#for body_sw

the_data["body_sw_stem"] = the_data.body_sw.apply(stem_fun)
the_data["cnt_sw_stem"] = the_data.body_sw_stem.apply(wrd_cnt)
total_unique_body_sw_stem = wrd_cnt(
    the_data.body_sw_stem.str.cat(sep=" "))

xform_d = vec_fun(the_data.body_sw_stem, 1, 1, "vec", out_path)

chi_fun_out = chi_fun(xform_d, the_data.label, 1000, out_path, "chi")

#principle component analysis

# print (jaccard_dist("columbia is awesome", "columbia is in nyc"))
# print (jaccard_dist(
#    the_data.body_sw_stem.iloc[0], the_data.body_sw_stem.iloc[1]))

# est = cos_sim_fun(chi_fun_out, chi_fun_out, the_data.label)

#turn into a function called pca_fun, have an input to pass the desired
#explained variance and save the model via arbitrary name that you pass

# my_pca_data = pca_fun(xform_d, 0.95, out_path, "pca")

lib = 'models/word2vec_sample/pruned.word2vec.txt'
emb_data, my_model = extract_embeddings_pre(the_data.body, out_path, lib)
#my_model.similar_by_key("trout", 10)
#print (my_model.most_similar(
#    positive=['world','human'], negative=['water'], topn = 5))

domain_data, domain_model = domain_train(the_data.body, out_path, "body")

"""turn into a function and let user select test_size
let user switch between randomforest, gaussian naive bayes and svm"""

#train a ML algo
#sw = "rf"
#model_o = model_train(
#    chi_fun_out, the_data.label, 0.20, sw, out_path)

"""
create a function out of the below
add randomforest, svc, gnb
"""

grid_in_rf = {'max_depth': [None, 10, 100],
              'n_estimators': [10, 100],
              'random_state': [123]}
grid_in_nb = {'var_smoothing': [0.000001, 0.00001, 0.0001, 0.001]}
grid_in_svc = {'C': [0.001, 0.1, 1],
              'kernel' : ('rbf', 'sigmoid')}

model_o_fun = grid_fun(
    chi_fun_out, the_data.label, grid_in_rf, 0.2, 6, out_path, "rf")




