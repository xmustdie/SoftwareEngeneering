test_sequence = "Hello, world! Python IS the programming language of thE future. My EMAIL is… PYTHON is awesome!!!!"


def remove_bad_words(sequence):
    with open('files/input.txt') as input_file:
        bad_words = input_file.readline().split()
        for bad_word in bad_words:
            while True:
                bad_index = sequence.lower().find(bad_word)
                if bad_index == -1:
                    break
                word_len = len(bad_word)
                sequence = sequence[:bad_index] + '*' * word_len + sequence[bad_index + word_len:]
    return sequence


if __name__ == '__main__':
    print(remove_bad_words(test_sequence))
