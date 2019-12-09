# coding:utf-8
# 課題5．6
import glob
def count_words(list_words):
fro
    lower_word_list=[]
    for word in list_words:
        lower_word_list.append(word.lower())
    set_lower_word_list = set(lower_word_list)
    # print(set_lower_word_list)
    return  len(set_lower_word_list)

filelist = input()

number_of_words=count_words(filelist)
print(number_of_words)

#for file in glob.glob("text*.txt"):
 #   list_words = files_to_list(file)
  #  number_of_words=count_words(list_words)
   # print(number_of_words)


