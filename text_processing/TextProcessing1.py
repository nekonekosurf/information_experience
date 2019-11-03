# なぜか外部入力からだとうまくいかない
# 課題５．１
def contain_alphabet(list_words, alphabet):
    list=[]
    for w in list_words:
        if w.lower().find(alphabet.lower()) != -1:
            list.append(w.lower())
    set_list=set(list)
    print(sorted(set_list))

# word1=['Hokkaido','University','Engineering','Department','of','Electronics','and','Information','Engineering','School','of']

while 1 :
    word1=input("word1")
    print(word1)
    string  = input("alphabet")
    contain_alphabet(word1,string)