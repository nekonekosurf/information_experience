# なぜか外部入力からだとうまくいかない
# 課題５．3
def end_ten(list_words):
    list=[]
    for w in list_words:
        if w.lower().endswith('ten'):
            list.append(w.lower())
    set_list=set(list)
    print(sorted(set_list))

def caption_pt(list_words):
    list=[]
    for w in list_words:
        if w.lower().find('pt') != -1:
            list.append(w.lower())
    set_list=set(list)
    print(sorted(set_list))

def begin_upper(list_words):
    list=[]
    for w in list_words:
        flag=0
        if w[0].isupper():       #先頭大文字抽出
            for i in range(1,len(w)):
                if w[i].islower()==False:
                    flag=1
            if flag== 0:
                list.append(w)


    set_list=set(list)
    print(sorted(set_list))

word1=['caption','option','section','written','given','English','USA','engine','iPad','Ten']

# word1=input("word1")
end_ten(word1)
caption_pt(word1)
begin_upper(word1)
