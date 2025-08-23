# Read the number of words to process
n = int(input())

# List to keep track of unique words in the order they appear
word_list = []

# Dictionary to store each word and its frequency count
word_dict = {}

# Process each input word
for i in range(n):
    word = input()
    # If the word appears for the first time, add it to the list
    if word not in word_dict:
        word_list.append(word)
    # Update the frequency count of the word in the dictionary
    word_dict[word] = word_dict.get(word, 0) + 1

# Print the number of distinct words
print(len(word_list))

# Print the list of distinct words in input order
print(word_list)

# Print the occurrence counts of each word in input order
for word in word_list:
    print(word_dict[word], end=' ')
print()  # Print a newline after the counts

# Print the dictionary with words and their frequencies
print(word_dict)
