# -*- coding: utf-8 -*-
"""
Created on Fri Aug 07 17:13:35 2015
@author: umezawa
係り元の文節と係り先の文節のテキストをタブ区切り形式ですべて抽出せよ．ただし，句読点などの記号は出力しないようにせよ．
"""

import argparse
from train_41 import get_chunks_list


def main(in_file):
    sentence_number = 7
    sentences = get_chunks_list(in_file)
    for phrase_number in range(len(sentences[sentence_number])):
        # 係り先文節番号
        destination_number = sentences[sentence_number][phrase_number].dst
        # 係り元文節番号
        for source_number in sentences[sentence_number][phrase_number].srcs:
            outputs = list()
            # 係り元の文節
            if source_number == -1:
                outputs.append("None")
            else:
                outputs.append("".join([morph.surface for morph in sentences[sentence_number][source_number].morphs if not morph.pos == "記号"]))
            # 対象の文節
            outputs.append("".join([morph.surface for morph in sentences[sentence_number][phrase_number].morphs if not morph.pos == "記号"]))
            # 係り先の文節
            if destination_number == -1:
                outputs.append("None")
            else:
                outputs.append("".join([morph.surface for morph in sentences[sentence_number][destination_number].morphs if not morph.pos == "記号"]))
            # タブ区切り形式で出力
            print "\t".join(outputs)
            
if __name__ == "__main__" :
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", dest="cabocha", default="neko.txt.cabocha", help="train_40 help")
    args = parser.parse_args()
    main(args.cabocha)
    


