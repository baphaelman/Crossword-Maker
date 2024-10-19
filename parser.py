
common_words = []

with open('words.txt', 'r') as file:
    for line in file:
        line = line.strip()
        if len(line) > 2:
            common_words.append(line)