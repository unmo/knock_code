# -*- coding: utf-8 -*-
"""
Created on Fri Aug 07 17:13:35 2015

@author: umezawa
12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．確認にはpasteコマンドを用いよ．
"""
import argparse
import sys

def merge(col1,col2):
    with open("merge.txt","w") as merge:
        for a,b in zip(open(col1,"r"),open(col2,"r")):
            a = a.strip()
            b = b.strip()
            merge.write(a + "\t"+ b + "\n")
    
if __name__ == "__main__" :
    parser = argparse.ArgumentParser()
    parser.add_argument('-c1', '--col1', dest = 'col1', default="col1.txt")
    parser.add_argument('-c2', '--col2', dest = 'col2', default="col2.txt")
    args = parser.parse_args()
    merge(args.col1,args.col2)

"""
答え例

if __name__ == '__main__':
    for line1, line2 in zip(open(sys.argv[1]), open(sys.argv[2])):
        print '%s\t%s' % (line1.strip(), line2.strip())

import argparse
import sys

def main(col1, col2):
    my_list1 = []
    my_list2 = []
    for line1 in open(col1):
        my_list1.append(line1.strip()) 

    for line2 in open(col2):
        my_list2.append(line2.strip())

    if len(my_list1) != len(my_list2):
        print >> sys.stderr, "Total lines are not same."
    else:
        for i in range(len(my_list1)):
            print my_list1[i] + "\t" + my_list2[i]


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--col1', dest='col1', default="../data/col1.txt")
    parser.add_argument('-o', '--col2', dest='col2', default="../data/col2.txt")
    args = parser.parse_args()
    main(args.col1, args.col2)
"""