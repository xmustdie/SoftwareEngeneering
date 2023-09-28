import collections
import re


def get_top_frequency(w_list):
    result_dic = collections.OrderedDict([])
    for word in w_list:
        result_dic[word] = result_dic.get(word, 0) + 1
    return sorted(result_dic.items(), key=lambda item: item[1], reverse=True)[:1]


words_list = []
with open('files/article.txt') as input_file:
    for line in input_file:
        words_list.extend(re.findall("[a-zA-Z_]+", line))
print(f"Words amount: {len(words_list)}")
print(f"Most frequency word is: {get_top_frequency(words_list)}")
