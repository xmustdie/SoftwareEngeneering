from task04 import remove_bad_words


test_sequence = "Hello, world! Python IS the programming language of thE future. My EMAIL is… PYTHON is awesome!!!!"

if __name__ == '__main__':
    censored_text = remove_bad_words(test_sequence)
    with open('files/censored.txt', 'w') as file:
        file.write(censored_text)
