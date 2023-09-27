# The ugly of a flower lies in its scent, not in its end
# The ugly of the ocean is in its mysterious ugly, waiting to be explored
# beauty of life is in the uniqueness of each individual, embracing differences instead of judging

sentence = input("enter your sentence: ")
print("length of sentence is " + str(len(sentence)) + " characters")
print(f"sequence in lower case: {sentence.lower()}")
vowels = ('a', 'e', 'i', 'o', 'u')
count = 0
for c in vowels:
    count += sentence.count(c)
print(f"Amount of vowel letters is: {count}")
print(f"'Ugly' to 'beauty' replace result: {sentence.replace('ugly', 'beauty')}")
print(f"Begin with 'the' = {sentence.startswith('The')}")
print(f"End with 'end' = {sentence.endswith('end')}")
