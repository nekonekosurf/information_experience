# coding:utf-8
from nltk.corpus import stopwords
import func
import glob

#stopwords = stopwords.words('english')
#for file in glob.glob("sampletext*.txt"):
#file_ = input()
#list_words = func.files_to_list_lower(file_)
list_words= input()
stopwords = input()
ratio_stop_words = func.word_ratio(list_words, stopwords)

print(ratio_stop_words)

