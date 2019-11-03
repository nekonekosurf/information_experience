
# なぜか外部入力からだとうまくいかない
# 課題５．4
def palindrome(text):
    text= text.replace('.','')
    re_word_list=[]
    word_list=text.lower().split(" ")
    word_list.reverse()
    cnt=0
    for w in word_list:
        if cnt == 0:
            ww=(w[::-1])
            ww = ww.replace(ww[0], ww[0].upper(), 1)
            re_word_list.append(ww)
        else:
            re_word_list.append(w[::-1])
        cnt +=1

    # re_word_list[0][1] = re_word_list[0][1].upper()
    re_text=' '.join(re_word_list)
    re_text = re_text.replace(' i ',' I ')
    if re_text.endswith('i '):
        re_text = re_text.replace('i ', 'I ')
    print(re_text)

text1="She sells sea shells by the sea shore."
text2 = "I am Taro kami asdf."
palindrome(text1)
palindrome(text2)
