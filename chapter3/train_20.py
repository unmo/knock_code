# -*- coding: utf-8 -*-
"""
Created on Fri Aug 07 17:13:35 2015

@author: umezawa
Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．問題21-29では，ここで抽出した記事本文に対して実行せよ．
"""
import sys
import json

with open(sys.argv[1],"r") as read, open(sys.argv[2],"w") as write:
    for line in read:
        line = line.strip()
        data = json.loads(line)
        if data["title"] == u"イギリス":
            write.write(data["text"].encode("utf-8"))


