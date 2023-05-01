def unique_word(document_count):
    num_of_lines = len(document_count.split('\n'))  
    num_of_chars = len(document_count.replace(' ', ''))
    document_count = document_count.replace('\t', ' ').replace('\n', ' ')
    frequency = document_count.split(' ')
    word_count = {}
    for text in frequency:
        if text == '':
            continue
        if text.endswith(",") or text.endswith(".") or text.endswith("?") or text.endswith("!"):
            if text[:-1] not in word_count:
                word_count[text[:-1]] = 1
            else:
                word_count[text[:-1]] += 1
            if text[-1] not in word_count:
                word_count[text[-1]] = 1
            else:
                word_count[text[-1]] += 1
        else:
            if text not in word_count:
                word_count[text] = 1
            else:
                word_count[text] += 1
    return word_count, num_of_lines, num_of_chars

document_count = "In the ,    project, \nThe project has to\tcount the frequency of each unique word"
word_count, num_of_lines, num_of_chars = unique_word(document_count)
print("Word count: ", word_count)
print("Number of lines: ", num_of_lines)
print("Number of characters: ", num_of_chars)

