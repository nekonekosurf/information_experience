import func
import codecs

f = codecs.open('./example/wagahaiwa_nekodearu_utf8_cmd.txt', 'r', 'utf-8')
jtext = f.read()
print(f)
f.close()
ratio_noun = func.percent_noun(jtext)
print(ratio_noun)
