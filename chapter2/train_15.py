# -*- coding: utf-8 -*-
"""
Created on Fri Aug 07 17:13:35 2015

@author: umezawa
自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．確認にはtailコマンドを用いよ．
"""

import argparse

def main(num,input_file):
    with open(input_file,"r") as read_file :
        line = read_file.readlines()
        for n in range(-num,0):
            print line[n]

if __name__ == "__main__" :
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--num', dest = 'num', default = 5)
    parser.add_argument('-i', '--input', dest = 'input_file', default = "../data/hightemp.txt")
    args = parser.parse_args()
    main(args.num,args.input_file)
    
"""
import sys

count = 0
limit = int(sys.argv[2])
result = list()
for line in open(sys.argv[1]):
    result.append(line.strip())
    if count >= limit:
        result.pop(0)
    count += 1
    

for line in result:
    print line


"""