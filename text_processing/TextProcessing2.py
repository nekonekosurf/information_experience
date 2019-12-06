# coding:utf-8
# 課題５．2
def three_letter_words(list_words):
    list=[]
    for w in list_words:
        if len(w) == 3:
            list.append(w.lower())
    set_list=set(list)
    print(sorted(set_list))

#word1=['She','sells','sea','shells','by','the','sea','shore']
word1= input()
three_letter_words(word1)
