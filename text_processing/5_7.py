# coding:utf-8
import os
from contextlib import redirect_stdout
import func
import codecs

f = codecs.open('./jsample.txt', 'r', 'utf-8')
jtext = f.read()
f.close()

# 部分的に
with redirect_stdout(open(os.devnull, 'w')):
    top_30_jnoun = func.jnoun(jtext)

ratio = func.percent_jword(jtext, top_30_jnoun)
print("top 30 の出現率の名詞が全体の単語に占める割合:　", ratio)
