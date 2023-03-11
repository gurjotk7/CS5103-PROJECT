def unique_word(document_count):
    document_count = document_count.replace('\t', ' ').replace('\n', ' ')
    frequency = document_count.split(' ')
    word_count = {}
    for text in frequency:
        if text == '':
            continue
        if text not in word_count:
            word_count[text] = 1
        else:
            word_count[text] += 1
    return word_count
document_count = "In the , project\nThe project has to\tcount the frequency of each unique word"
word_count = unique_word(document_count)
print(word_count)




