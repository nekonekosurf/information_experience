# coding:utf-8
# 関数ファイル
from __future__ import print_function
import glob, string
import numpy as np
import MeCab


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
    list_values = top_ten_dict.values()
    list_values = set(list_values)
    list_values = list(list_values)
    if len(list_values) < top_n:
        return top_ten_dict
    # print(list_values)
    list_values.sort(reverse=True)
    new_dict = {}
    for i in range(top_n):
        print('{0:^5}'.format(i + 1), "　位|", end="")
        for key in top_ten_dict.keys():
            if top_ten_dict[key] == list_values[i]:
                new_dict[key] = list_values[i]
                print('{0:^15}|{1:^10}'.format(key, list_values[i]), "回|", end="")
        print("")
    return new_dict


def word_ratio(word_list, word_norms):
    ratio_dict = {}
    for a_word in word_list:
        # print(a_word)
        # print(word_list)
        if a_word in word_norms:
            if a_word not in ratio_dict:
                ratio_dict[a_word] = 1
            else:
                ratio_dict[a_word] += 1
    total_words_list = len(word_list)
    total_words_norm = sum(ratio_dict.values())
    return total_words_norm / total_words_list



def percent_noun(text):
    #mecab = MeCab.Tagger('-d /usr/lib/mecab/dic/mecab-ipadic-neologd')
    mecab.parse('')
    jtext1_node = mecab.parseToNode(text)

    hinshi_count = {}
    while jtext1_node:
        word = jtext1_node.surface
        hinshi = jtext1_node.feature.split(",")[0]
        if hinshi not in hinshi_count.keys():
            hinshi_count[hinshi] = 1
        else:
            hinshi_count[hinshi] += 1
        jtext1_node = jtext1_node.next
    total_num = sum(hinshi_count.values())

    print(hinshi_count)
    print(total_num)
    print(hinshi_count['名詞'])
    return hinshi_count['名詞'] / total_num


def jnoun(text):
    mecab = MeCab.Tagger('-Ochasen')
    mecab.parse('')
    jtext1_node = mecab.parseToNode(text)
    noun_count_dict = {}
    # ここから名詞の個数をカウントして辞書に追加
    while jtext1_node:
        word = jtext1_node.surface
        # print(word)
        hinshi = jtext1_node.feature.split(",")[0]
        # print(hinshi)
        if hinshi == '名詞':
            # print(word)
            if word not in noun_count_dict.keys():
                noun_count_dict[word] = 1
            else:
                noun_count_dict[word] += 1
        jtext1_node = jtext1_node.next
    # print(noun_count_dict)
    # ここからトップ３０をはじき出す
    list_values = noun_count_dict.values()
    list_values = set(list_values)
    list_values = list(list_values)
    list_values.sort(reverse=True)
    print(list_values)

    # new_dictに新たなトップ３０が入る辞書を作る
    new_dict = {}
    for i in range(30):
        print('{0:^5}'.format(i + 1), "　位|", end="")
        for key in noun_count_dict.keys():
            if noun_count_dict[key] == list_values[i]:
                new_dict[key] = list_values[i]
                print('{0:^10}|{1:^5}'.format(key, list_values[i]), "回|", end="")
        print("")

    # 辞書をリストへ
    # print(new_dict)
    top_30_noun_list = []
    for key in new_dict.keys():
        top_30_noun_list.append(key)

    return top_30_noun_list


def percent_jword(text, words):
    mecab = MeCab.Tagger('-d /usr/lib/mecab/dic/mecab-ipadic-neologd')
    mecab.parse('')
    jtext1_node = mecab.parseToNode(text)
    noun_count_dict = {}
    # ここから名詞の個数をカウントして辞書に追加
    while jtext1_node:
        word = jtext1_node.surface
        # print(word)
        hinshi = jtext1_node.feature.split(",")[0]
        # print(hinshi)
        if hinshi == '名詞':
            # print(word)
            if word not in noun_count_dict.keys():
                noun_count_dict[word] = 1
            else:
                noun_count_dict[word] += 1
        jtext1_node = jtext1_node.next
    # 辞書のvaluesをすべて合計したものとwordの合計値から
    # word（top 30 ）がどれくらい使われているか計算する
    total_words=sum(noun_count_dict.values())
    print("単語の総数: ",total_words)
    total_30=0
    for noun in words:
        total_30 += noun_count_dict[noun]
    print("トップ３０の名詞の数: ",total_30)
    return  total_30/total_words
