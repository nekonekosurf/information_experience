# coding:utf-8
#課題5-2
from __future__ import print_function
import  glob,string
import  numpy as np

def files_to_list(filename):
    f = open(filename,'r')
    text = f.read()
    f.close()
    for sep in [',','.',':',';','\'' , '"']:
        text= text.replace(sep,' ')
    text= text.split()
    return text

def alphabet_freq(text_list):
    list_num_alphabet=[]
    list_char_alphabet= []
    for c in string.ascii_lowercase:
        list_char_alphabet.append(c)
        list_num_alphabet.append(0)
    for word in text_list:
        for char in word.lower():
            for az in string.ascii_lowercase:
                if char == az:
                    list_num_alphabet[list_char_alphabet.index(az)] +=1

    # print(list_char_alphabet)
    # print(list(map(str,list_num_alphabet)))

    return list_num_alphabet
def list_add(in1, in2):
    sum_list = np.array(in1, dtype=object) + np.array(in2, dtype=object)
    return sum_list.tolist()



list_char_alphabet= []
sum_list_num_alphabet = []
for char in string.ascii_lowercase: #initiate array.
    sum_list_num_alphabet.append(0)
    list_char_alphabet.append(char)


list_input = input()
#print(list_input)
#list_input =  ['She', 'sells', 'sea', 'shells', 'by', 'the', 'sea', 'shore']


sum_list_num_alphabet= list_add(sum_list_num_alphabet,alphabet_freq(list_input))




print(sum_list_num_alphabet)


