import func
import codecs

f = codecs.open('./jsample.txt', 'r', 'utf-8')
jtext = f.read()
f.close()
top_30_jnoun = func.jnoun(jtext)
print(top_30_jnoun)
