# We need an empty dictionary, to store and display the letter frequencies.
word_count = {}

# Text string
text = "Be happy!"

# Iterate over every character in the string.
for char in text.casefold():
    # We're only counting letters and digits (no punctuation).
    if char.isalnum():
        if char in word_count:
            word_count[char] += 1
        else:
            word_count[char] = 1

# Printing the dictionary
for letter, count in sorted(word_count.items()):
    print(letter, count)


# Printing the dictionary
for letter, count in sorted(word_count.items()):
    print(letter, count)
