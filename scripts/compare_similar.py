#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tfidf import calc_tf, calc_idf, make_d
from cos_similar import cos_sim
import pandas as pd
from pandas import Series, DataFrame
import re
import pickle
from calc_pearson import Calc_pearson
import numpy as np


all_txt_list=[]
txt_answer='What is this event'#sprの既存の質問文
txt_input='What these these events'#音声認識で得られるであろうご認識の含まれた文章
csvfile=pd.read_csv('Questions_32.csv')

#tfidfの計算
def calc_tfidf(txt, all_txt):
    count=0
    tf_num=[]
    idf_num=[]
    tf_idf_num=[]
    for word in txt.split(' '):
        tf_num.append(calc_tf(word, txt.split(' ')))
        idf_num.append(calc_idf(word, all_txt))
        tf_idf_num.append(tf_num[count]*idf_num[count])
        count+=1
    return tf_idf_num



for line in csvfile['Title']:
    word_list=make_d(line)
    all_txt_list.append(word_list)




print('tfidf:{}'.format(Calc_pearson(
    np.array(calc_tfidf(txt_answer, all_txt_list)),
    np.array(calc_tfidf(txt_input, all_txt_list)))))
print('cos_sim:{}'.format(cos_sim(txt_answer, txt_input)))



        
