# -*- coding: utf-8 -*-
"""
Created on Fri Aug 07 17:13:35 2015

@author: umezawa

@
"""

import argparse
import train_30

def main(neko_dict):
    for sent in neko_dict:
        for m in sent:
            print type(m)
            if m['pos'] == '動詞':
                print m['surface']

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--train', dest='train', default='../data/neko.mecab', help='input training data')
    args = parser.parse_args()
    my_morph = train_30.morph(args.train)
    main(my_morph)
