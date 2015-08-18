# -*- coding: utf-8 -*-
"""
Created on Fri Aug 07 17:13:35 2015

@author: umezawa
自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ．
"""
import argparse

def main(num,input_file):
    with open(input_file,"r") as read_file :
        line = read_file.readlines()
        for n in range(num):
            with open("%s_%d.txt" % ("split",n+1) ,"w") as split:
                split.write(line[n])

if __name__ == "__main__" :
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--num', dest = 'num', default = 3)
    parser.add_argument('-i', '--input', dest = 'input_file', default = "../data/hightemp.txt")
    args = parser.parse_args()
    main(args.num,args.input_file)


"""

import argparse


def main(n, my_text, divide_name):
    my_list1 = []
    for line in open(my_text):
        my_list1.append(line.strip())

    l = len(my_list1) / n
    all_list = [my_list1[x:x + l] for x in xrange(0, len(my_list1), l)]
    for i in range(n):
        f = open('%s.%d.txt' % (divide_name, i), 'w')
        f.write("\n".join(all_list[i - 1]))
        f.close


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--N', dest='N', default=3)
    parser.add_argument('-t', '--train', dest='train', default="../data/hightemp.txt", help='input training data')
    parser.add_argument('-d', '--divide', dest='divide', default="../data/split_file", help='output divided data')

    args = parser.parse_args()
    main(int(args.N), args.train, args.divide)
    
"""