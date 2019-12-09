# coding:utf-8
# P課題5-8
from __future__ import print_function
import glob, string
import numpy as np
from collections import OrderedDict


def files_to_list(filename):
    f = open(filename, 'r')
    text = f.read()
    f.close()
    for sep in [',', '.', ':', ';', '\'', '"']:
        text = text.replace(sep, ' ')
    text = text.split()
    return text


def files_to_list_lower(filename):
    f = open(filename, 'r')
    text = f.read()
    f.close()
    for sep in [',', '.', ':', ';', '\'', '"']:
        text = text.replace(sep, ' ').lower()
    text = text.split()
    return text


def alphabet_freq(text_list):
    list_num_alphabet = []
    list_char_alphabet = []
    for c in string.ascii_lowercase:
        list_char_alphabet.append(c)
        list_num_alphabet.append(0)
    for word in text_list:
        for char in word.lower():
            for az in string.ascii_lowercase:
                if char == az:
                    list_num_alphabet[list_char_alphabet.index(az)] += 1
    return list_num_alphabet


def list_add(in1, in2):
    sum_list = np.array(in1, dtype=object) + np.array(in2, dtype=object)
    return sum_list.tolist()


# すべてを辞書に入れる関数
def make_dict(list_text, top_ten_dict):
    freq = 4
    for word in list_text:
        if len(word) >= freq:
            if word not in top_ten_dict:  # 辞書に存在していない
                top_ten_dict[word] = 1
            else:
                top_ten_dict[word] += 1

    return top_ten_dict


# 辞書から際頻出単語を上位n個に限定する関数
def top_ten_words(top_ten_dict, top_n):
	list_values = top_ten_dict.values() #値だけ取り出している
	list_values = set(list_values)#値を射影してかぶりが亡くなるようにしている
	list_values = list(list_values)
	if len(list_values)<top_n:#
		return top_ten_dict
	list_values.sort(reverse=True)
	new_dict = {}
	for i in range(top_n):
		print('{0:^5}'.format(i+1),"　位|",end="")
	for key in top_ten_dict.keys():
		if top_ten_dict[key] == list_values[i]:
			new_dict[key] = list_values[i]
			print('{0:^15}|{1:^10}'.format(key,list_values[i]),"回|", end="")
		print("")
	return new_dict

dict = {}
top_n_dict = {}
top_n = 10




#list_words=input()
list_words= ['Japanese', 'chemist', 'Akira', 'Yoshino', 'one', 'of', 'the', 'three', 'winners', 'of', 'this', 'year', 's', 'Nobel', 'Prize', 'in', 'chemistry', 'for', 'contributions', 'to', 'the', 'development', 'of', 'lithium', 'ion', 'batteries', 'said', 'Sunday', 'such', 'batteries', 'will', 'play', 'a', 'key', 'role', 'in', 'achieving', 'a', 'sustainable', 'society', 'Lithium', 'ion', 'batteries', 'will', 'play', 'a', 'central', 'role', 'in', 'achieving', 'a', 'sustainable', 'society', 'in', 'which', 'the', 'environment', 'economy', 'and', 'convenience', 'are', 'balanced', 'in', 'harmony', 'Yoshino', '71', 'honorary', 'fellow', 'at', 'Asahi', 'Kasei', 'Corp', 'and', 'professor', 'at', 'Meijo', 'University', 'said', 'in', 'his', 'Nobel', 'lecture', 'at', 'Stockholm', 'University', 'in', 'Sweden', 'Our', 'world', 'will', 'change', 'dramatically', 'In', 'the', 'lecture', 'titled', 'Brief', 'History', 'and', 'Future', 'of', 'Lithium', 'ion', 'Batteries', 'Yoshino', 'underscored', 'that', 'the', 'development', 'of', 'the', 'batteries', 'can', 'be', 'linked', 'with', 'that', 'of', 'AI', 'the', 'internet', 'of', 'things', 'and', 'next', 'general', 'wireless', 'networks', 'Behind', 'the', 'discovery', 'of', 'a', 'key', 'electrode', 'material', 'were', 'research', 'results', 'achieved', 'by', 'two', 'Japanese', 'Nobel', 'laureates', 'the', 'late', 'Kenichi', 'Fukui', 'and', 'University', 'of', 'Tsukuba', 'professor', 'emeritus', 'Hideki', 'Shirakawa', '83', 'Yoshino', 'said', 'Lithium', 'ion', 'batteries', 'are', 'a', 'very', 'very', 'fortunate', 'fellow', 'born', 'with', 'the', 'support', 'of', 'eight', 'Nobel', 'laureates', 'Yoshino', 'said']

	



#print(list_words)
#for word in list_word:
	

dict = make_dict(list_words, dict)

dict_={}
dict_=make_dict(list_words,dict_)
top_ten_words(dict_,top_n)


"""
for file in glob.glob("sampletext*.txt"):
    list_words = files_to_list_lower(file)
    dict = make_dict(list_words, dict)
    print("---------------単語の出現回数 " + file + "ここから---------------")
    dict_={}
    dict_=make_dict(list_words,dict_)
    top_ten_words(dict_,top_n)
    print("---------------単語の出現回数　" + file + "　　ここまで---------------")
    print("\n\n")

"""

