# -*- coding: utf-8 -*-
"""
Created on Fri Aug 07 17:13:35 2015

@author: umezawa
各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．確認にはcut, uniq, sortコマンドを用いよ．
"""
import sys
import argparse
from collections import Counter

cols_list = []

def main(input_file):
    with open(input_file,"r") as in_file:
        for line in in_file:
            cols = line.split("\t")[0]
            cols_list.append(cols)
        #print cols_list
        count = Counter(cols_list)
        #print count
        for k,v in sorted(count.items(), key=lambda x:x[1], reverse = True):
            print "%s:%d" % (k,v)
        
        
if __name__ == "__main__" :
    parser = argparse.ArgumentParser()
    parser.add_argument("-i","--input",dest="input",default="../data/hightemp.txt")
    args = parser.parse_args()
    main(args.input)
    
"""
import sys
from collections import defaultdict


with open("hightemp.txt", "r") as f:
    lines = f.readlines()

    freq_dict = defaultdict(int)
    for line in lines:
        col1 = line.split("\t")[0]
        freq_dict[col1] += 1

    for s, f in sorted(sorted(freq_dict.items(), reverse=True), key=lambda x: x[1], reverse=True):
        print s,f



# コマンド
# cut -f 1 hightemp.txt | sort | uniq -c| sort -k 1 -r 




import argparse
from collections import defaultdict


def main(my_file):
    my_dict = defaultdict(lambda:int())
    for line in open(my_file):
        my_dict[line.strip().split()[0]] += 1

    for key, value in sorted(my_dict.items(), key=lambda x: -x[1]):
        print key, value


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--train', dest='train', default="../data/hightemp.txt", help='input training data')
    args = parser.parse_args()
    main(args.train)

"""