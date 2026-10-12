import re

text = "Hello World! AI is amazing. AI is useful."

# Convert to lowercase
text = text.lower()

# Remove punctuation
text = re.sub(r"[^a-z0-9\s]", "", text)

# Tokenization
tokens = text.split()

# Remove stop words
stop_words = {"is", "the", "a", "an", "and", "of"}
filtered = [word for word in tokens if word not in stop_words]

print("Original text:", "Hello World! AI is amazing. AI is useful.")
print("Lowercase text:", text)
print("Tokens:", tokens)
print("After stop-word removal:", filtered)