import func
import codecs

f = codecs.open('./jsample.txt', 'r', 'utf-8')
jtext = f.read()
f.close()
ratio_noun = func.percent_noun(jtext)
print(ratio_noun)
