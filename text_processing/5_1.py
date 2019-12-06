# coding:utf-8
#課題5-1


import  glob
def files_to_list(filename):
    f = open(filename,'r')
    text = f.read()
    f.close()
    for sep in [',','.',':',';','\'' , '"']:
        text= text.replace(sep,' ')
    text= text.split()
    return text

def count_words(list_words):

    lower_word_list=[]
    for word in list_words:
        lower_word_list.append(word.lower())
    set_lower_word_list = set(lower_word_list)
    # print(set_lower_word_list)
    return  len(set_lower_word_list)

list_words=files_to_list('./sampletext.txt')
print(list_words)



#ここまででテキストをリストに格納
# text = input()
number_of_words=count_words(list_words)
print(number_of_words)




for file in glob.glob("text*.txt"):
    list_words = files_to_list(file)
    number_of_words=count_words(list_words)
    print(number_of_words)


