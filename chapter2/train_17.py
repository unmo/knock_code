# -*- coding: utf-8 -*-
"""
Created on Fri Aug 07 17:13:35 2015

@author: umezawa
1列目の文字列の種類（異なる文字列の集合）を求めよ．確認にはsort, uniqコマンドを用いよ．

"""
import argparse

def main(input_file):
    with open(input_file,"r") as in_file:
        for line in in_file:
            print line.strip().split("\t")[0]
    
if __name__ == "__main__" :
    parser = argparse.ArgumentParser()
    parser.add_argument("-i","--input",dest="input",default="../data/hightemp.txt")
    args = parser.parse_args()
    main(args.input)
    
"""
import argparse

def main(train_file):
    my_dict = dict()
    for line in open(train_file):
        my_dict[line.strip().split("\t")[0]] = 0

    for key in my_dict.keys():
        print key


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--train', dest='train', default="../data/hightemp.txt", help='input training data')
    args = parser.parse_args()
    main(args.train)

"""