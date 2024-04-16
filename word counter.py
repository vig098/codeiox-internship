import re

def word_counter(text):
    text = text.lower()
    text = re.sub('[^a-z\s]', '', text)
    words = text.split()
    word_freq = {}
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

    return word_freq

try:
    text = input("Enter a sentence or paragraph: ")

    if text == "":
        print("Error: Empty input.")
    else:
        word_counts = word_counter(text)

        for word, count in word_counts.items():
            print(f"{word}: {count}")
except Exception as e:
    print("Error: ", str(e))