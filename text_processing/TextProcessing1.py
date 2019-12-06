# coding:utf-8
# 課題５．１

def contain_alphabet(list_words, alphabet):
    list=[]
    for w in list_words:
        if w.lower().find(alphabet.lower()) != -1:
            list.append(w.lower())
	 
    set_list=set(list)
    print(sorted(set_list))


word1=input()
string  =input()
contain_alphabet(word1,string)



#word1=['Hokkaido','hokkaido','University','Engineering','Department','of','Electronics','and','Information','Engineering','School','of']

