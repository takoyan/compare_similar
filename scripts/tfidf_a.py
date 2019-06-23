# -*- coding: utf-8 -*-
import math
import treetaggerwrapper as ttw
import os

TTWDIR=os.environ['HOME']+'/tree-tagger-install/'
tagger=ttw.TreeTagger(TAGLANG='en', TAGDIR=TTWDIR)

#tfの計算
def calc_tf(t,d):
    count = 0.0

    for word in d:
        if(t == word):
            count += 1.0

    return float(count / len(d))

#idfの計算
def calc_idf(t,all_d):
    sum_t = 0.0

    for d in all_d:
        for word in d:
            if(t == word):
                sum_t += 1.0
                continue

    return math.log( ( len(all_d) / (sum_t + 1) ) , 2 )

#文章の単語をリスト化
def make_d(line):
    d = []

    sectence = line.split('\n')
    sectence = sectence[0]
    words = sectence.split(' ')

    for word in words:
        if(word.rfind(',') != -1 ):
            word = word.split(',')
            #print(word[0])
            d.append(word[0])
        else:
            #print(word)
            d.append(word)
    #(d)
    return d

#main
def main():
    #ファイル読み込み
    f = open('en1.txt')
    txt_data = f.read()
    f.close()

    #各文章ごとに単語をリスト化
    all_d = []
    lines = txt_data.split('\n')
    for line in lines:
        #d = make_d(line)
        #all_d.append(d)
        # ---ここから追加
        line = line.replace(",", "")
        d = []
        tags = tagger.TagText(line.decode("utf-8"))
        for tag in tags:
            word = tag.split('\t')[2] # 表層系
            d.append(str(word))
        # ---ここまで
        all_d.append(d)

    #文章の一覧の表示
    print("----文章の一覧-------------------------------------------------------------------------------------------------------------------------------------------------------------")
    for d in all_d:
        print(d)
    print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------")
    #検索する文章と単語を決める
    t = raw_input("検索する単語or文:")
    index = raw_input("検索する文章(index番号):")
    d = all_d[int(index)]
    # ---ここから追加
    tags2 = tagger.TagText(t.decode("utf-8"))
    search_list = []
    for tag2 in tags2:
        word = tag2.split('\t')[2] # 表層系
        search_list.append(str(word)) # 検索する文章もしくは単語のリスト
    # ---ここまで


    print("\n-------計算結果---------------------------------------------------------------------------------------------------------------------------------------------------------------")

    for t in search_list:
        print("単語：" + t)
        #tfを求める
        tf = calc_tf(t,d)
        print("tf:",tf)

        #idfを求める
        idf = calc_idf(t,all_d)
        print("idf:",idf)

        #tf-idfを求める
        tf_idf = tf * idf
        print("tf-idf:",tf_idf)
        print("---------------------------------")
if __name__ == '__main__':
    main()
