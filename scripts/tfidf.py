# -*- coding: utf-8 -*-
import math

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

    #sectence = line.split('\n')
    #sectence = sectence[0]
    for word in line.split(' '):
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
    count=0
    f = open('en1.txt')
    txt_data = f.read()
    f.close()

    #各文章ごとに単語をリスト化
    all_d = []
    lines = txt_data.split('\n')
    for line in lines:
        d = make_d(line)
        all_d.append(d)

    #文章の一覧の表示
    print("----文章の一覧-------------------------------------------------------------------------------------------------------------------------------------------------------------")
    for d in all_d:
        print(count,d)
        count+=1
        print('\n')
    print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------")
    #検索する文章と単語を決める
    t = raw_input("検索する単語:")
    index = raw_input("検索する文章(index番号):")
    d = all_d[int(index)]

    print("\n-------計算結果---------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print(d)
    #tfを求める
    tf = calc_tf(t,d)
    print("tf:",tf)

    #idfを求める
    idf = calc_idf(t,all_d)
    print("idf:",idf)

    #tf-idfを求める
    tf_idf = tf * idf
    print("tf-idf:",tf_idf)

if __name__ == '__main__':
    main()
