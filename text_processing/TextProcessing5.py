# coding:utf-8
# 課題５．5
def files_to_list(filename):
    f = open(filename,'r')
    text = f.read()
    f.close()
    for sep in [',','.',':',';','\'' ,'-', '"','!','?']:
        text= text.replace(sep,' ')
    text= text.split()
    return text

#text =files_to_list('./example/sent2.txt')
filename = input()
text =files_to_list(filename)
print(text)
