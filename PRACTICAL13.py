from collections import defaultdict, Counter
import re

text = """
Artificial intelligence is useful.
Artificial intelligence is growing.
Machine learning is useful.
Artificial intelligence is powerful.
"""

# Clean and tokenize
words = re.findall(r"\b[a-z]+\b", text.lower())

# Build bigram frequency table
bigrams = defaultdict(Counter)

for i in range(len(words) - 1):
    bigrams[words[i]][words[i + 1]] += 1

def predict_next(word):
    word = word.lower()

    if word not in bigrams:
        return "No prediction available"

    return bigrams[word].most_common(1)[0][0]

word = input("Enter a word: ")
print("Predicted next word:", predict_next(word))