common_words = {3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []}

with open('30k.txt', 'r') as file:
    for line in file:
        word = line.strip()
        word_length = len(word)
        if word_length > 2 and word_length < 9:
            common_words[word_length].append(word)