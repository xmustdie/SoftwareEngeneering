import collections


def get_top_three_frequency(some_string):
    result_dic = collections.OrderedDict([])
    for c in some_string:
        result_dic[c] = result_dic.get(c, 0) + 1
    return sorted(result_dic.items(), key=lambda item: item[1], reverse=True)[:3]


int_string = input("Input string with digit from keypad(min 15): ")
if len(int_string) >= 15:
    print(get_top_three_frequency(int_string))
else:
    print("Too low digit, have to 15 ")
