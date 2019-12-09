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



#対話型でうまくいくように関数化 名前もkつける
def main(list_words):
	#list_words=['The', 'organizers', 'of', 'the', 'large', 'scale', 'demonstrations', 'which', 'kicked', 'off', 'Hong', 'Kong', 's', 'months', 'long', 'protest', 'movement', 'earlier']
	list_char_alphabet= []
	sum_list_num_alphabet = []
	for char in string.ascii_lowercase:	
	    sum_list_num_alphabet.append(0)
	    list_char_alphabet.append(char)

	
	sum_list_num_alphabet= list_add(sum_list_num_alphabet,alphabet_freq(list_words))
	total_chars=sum(sum_list_num_alphabet)
	print("アルファベットの合計個数： ",total_chars)
	print("---------------すべてのアルファベットの出現頻度  --------------")
	ratio_list=[]
	for n in sum_list_num_alphabet:
		ratio_list.append(round(float(n)/float(total_chars),3))

# print(list_char_alphabet)
# print(ratio_list)

	for i in list_char_alphabet:
		print('{0:^6}|'.format(i),end="")
	print("")
	for i in ratio_list:
		print('{0:^6}|'.format(i),end="")
	print("")
	print(sum(ratio_list))

if __name__ == '__main__':
	main()

	
	


"""
list_char_alphabet= []
sum_list_num_alphabet = []
for char in string.ascii_lowercase:
    sum_list_num_alphabet.append(0)
    list_char_alphabet.append(char)

for file in glob.glob("sample*.txt"):
    list_words = files_to_list(file)
    sum_list_num_alphabet= list_add(sum_list_num_alphabet,alphabet_freq(list_words))

    print("---------------アルファベットの出現回数 " +file+  "ここから---------------")
    for i in list_char_alphabet:
        print('{0:^3}|'.format(i), end="")
    print("")
    for i in alphabet_freq(list_words):
        print('{0:^3}|'.format(i), end="")
    print("")

    print("---------------アルファベットの出現回数　" +file+  "　　ここまで---------------")
    print("")


print("---------------アルファベットの出現回数　合計　　ここまで---------------")
for i in list_char_alphabet:
    print('{0:^4}|'.format(i), end="")
print("")
for i in sum_list_num_alphabet:
    print('{0:^4}|'.format(i), end="")
print("")
print("")
total_chars=sum(sum_list_num_alphabet)
print("アルファベットの合計個数： ",total_chars)
print("")

print("---------------すべてのアルファベットの出現頻度  --------------")
ratio_list=[]
for n in sum_list_num_alphabet:
    ratio_list.append(round(float(n)/float(total_chars),3))

# print(list_char_alphabet)
# print(ratio_list)

for i in list_char_alphabet:
    print('{0:^6}|'.format(i),end="")
print("")
for i in ratio_list:
    print('{0:^6}|'.format(i),end="")
print("")
print(sum(ratio_list))


"""
