from nltk.corpus import stopwords
import func
import glob

stopwords = stopwords.words('english')
for file in glob.glob("sampletext*.txt"):
    list_words = func.files_to_list_lower(file)
    ratio_stop_words = func.word_ratio(list_words, stopwords)
    print("---------------stop words の割合 " + file + "ここから---------------")
    print(ratio_stop_words)
    print("---------------stop words の割合　" + file + "　　ここまで---------------")
    print("")
