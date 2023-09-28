import re

lines, words, letters = 0, 0, 0
with open('files/latin_text.txt') as input_file:
    for line in input_file:
        lines += 1
        words_list = re.findall("[a-zA-Z_]+", line)
        words += len(words_list)
        letters += sum(len(word) for word in words_list)

print("Input file contains:")
print(f"{letters} letters")
print(f"{words} words")
print(f"{lines} lines")
