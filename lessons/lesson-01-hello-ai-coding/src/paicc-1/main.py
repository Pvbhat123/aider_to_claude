with open('transcript.txt', 'r') as file:
    content = file.read()

words = content.lower().split()
word_freq = {}

for word in words:
    word = word.strip('.,!?;:')
    if word:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

sorted_freq = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)

for word, count in sorted_freq:
    if count > 3:
        print(f"{word}: {count} {'#' * count}")