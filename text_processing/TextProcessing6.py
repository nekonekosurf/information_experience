# coding:utf-8
# 課題５．6
import glob
def count_words(list_words):

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

#['Japan', 'is', 'losing', 'its', 'final', 'pager', 'service', 'decades', 'after', 'the', 'technology', 'was', 'rendered', 'obsolete', 'by', 'cell', 'phones', 'Tokyo', 'Telemessage', 'the', 'only', 'telecommunications', 'company', 'still', 'operating', 'the', 'service', 'said', 'it', 'would', 'terminate', 'its', 'pager', 'offerings', 'in', 'September', 'twenty', 'nineteen', 'due', 'to', 'lack', 'of', 'demand', 'The', 'company', 'said', 'the', 'number', 'of', 'users', 'has', 'fallen', 'to', 'below', 'one', 'thousand', 'five', 'hundred', 'despite', 'the', 'fact', 'that', 'it', 'stopped', 'producing', 'the', 'actual', 'devices', 'twenty', 'years', 'ago', 'Pagers', 'were', 'popular', 'in', 'Japan', 'and', 'the', 'rest', 'of', 'the', 'world', 'in', 'the', 'nineteen', 'ninty', 'before', 'cell', 'phones', 'became', 'widely', 'available', 'to', 'the', 'public', 'Tokyo', 'Telemessage', 'said', 'its', 'subscriber', 'base', 'peaked', 'in', 'nineteen', 'ninety', 'six', 'at', 'one', 'point', 'two', 'million', 'For', 'those', 'too', 'young', 'to', 'have', 'ever', 'used', 'one', 'pagers', 'are', 'a', 'personal', 'radio', 'device', 'that', 'is', 'used', 'to', 'receive', 'messages', 'sent', 'via', 'a', 'switchboard', 'When', 'the', 'pager', 'beeps', 'or', 'buzzes', 'the', 'owner', 'usually', 'needs', 'to', 'find', 'a', 'phone', 'to', 'return', 'the', 'message', 'It', 'is', 'not', 'clear', 'who', 'still', 'uses', 'them', 'but', 'Japan', 'Times', 'says', 'pagers', 'are', 'popular', 'with', 'people', 'working', 'in', 'hospitals', 'because', 'they', 'do', 'not', 'emit', 'electromagnetic', 'waves', 'A', 'reluctance', 'to', 'part', 'with', 'the', 'old', 'technology', 'may', 'also', 'be', 'due', 'to', 'aging', 'population', 'of', 'Japan', 'The', 'country', 'is', 'considered', 'a', 'super', 'aged', 'nation', 'defined', 'as', 'one', 'where', 'more', 'than', 'twenty', 'percent', 'of', 'the', 'population', 'is', 'over', 'sixty', 'five', 'This', 'year', 'new', 'government', 'figures', 'showed', 'the', 'number', 'of', 'children', 'fell', 'in', 'Japan', 'for', 'the', 'thirty', 'seventh', 'year', 'in', 'a', 'row']

#['a','a','a','a','b']
