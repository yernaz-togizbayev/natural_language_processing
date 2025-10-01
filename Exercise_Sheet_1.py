# %% [markdown]
# # Natural Language Processing
# 
# ## Exercise Sheet 1

# %%
!pip install numpy
!pip install matplotlib
!pip install nltk

# %%
#imports for all exercises
import nltk
# nltk.download('gutenberg')
# nltk.download('genesis')
# nltk.download('inaugural')
# nltk.download('nps_chat')
# nltk.download('webtext')
# nltk.download('treebank')
# nltk.download('stopwords')
nltk.download()

from nltk.book import *
from nltk import FreqDist

# %% [markdown]
# ### Exercise 1
# 
# How many words are there in `text2` from `nltk.book`? How many distinct words are there? Calculate the lexical diversity.
# 

# %%
# Calculate the total number of words
total_words = len(text2)
print(f"Total number of words in text2: {total_words}")

# Calculate the number of distinct words
distinct_words = len(set(text2))
print(f"Number of distinct words in text2: {distinct_words}")

# Calculate the lexical diversity
lexical_diversity = distinct_words / total_words
print(f"Lexical diversity of text2: {lexical_diversity:.4f}")

# %% [markdown]
# ### Exercise 2
# 
# Produce a dispersion plot of the four main protagonists in Sense and Sensibility: Elinor, Marianne, Edward, and Willoughby. What can you observe about the different roles played by the males and females in this novel? Can you identify the couples?

# %%
text2.dispersion_plot(["Elinor", "Marianne", "Edward", "Willoughby"])

# %% [markdown]
# ### Exercise 3
# 
# Find the collocations in `text6`.

# %%
# Find the collocations in text6
text6.collocations()

# %% [markdown]
# ### Exercise 4
# 
# Use only the `index()` function to find all the indexes of the word "sunset" in `text9`.

# %%
# List indexes of word 'sunset' in text9
indexes = [idx for idx, word in enumerate(text9) if word == 'sunset']

print(f"The indexes of 'sunset' in text9 are: {indexes}")

# %% [markdown]
# ### Exercise 5
# 
# What is the difference between the following two lines? Calculate the two values:
# 
#     len(sorted(set(w.lower() for w in text1)))
#     len(sorted(w.lower() for w in set(text1)))

# %% [markdown]
# In the first case, text1 will be iterated firstly and completely converted to lower case, which means, if there were for example 2 words which started once with lower case letter and once with capital letter, after lower() function, two words will become the same word after calling set(), there will stay only 1 word. So, if for example there were multiple similar words like ['Sunset', 'sunset', 'sunSET', 'SUNset'], after set() it will stay only one ['sunset'].
# 
# In the second case, set() called first. This means, it will first create a set of unique words and only then interate through this set of unique words and convert them into lower case. Then it sorts the set and calculate the length.
# 
# So the key point is here how the set() operation was applied. In the first scenario, it was covnerted to lower case and only then build a set of unique words. And in the second scenrio, since set was build first, and only then converted them into a lower case, some of words and be repeated in the set. So for example, if there were 'Sunset' and 'sunset', first expression will count them as a one unique word, and second one as two unique words.

# %%
len1 = len(sorted(set(w.lower() for w in text1)))
len2 = len(sorted(w.lower() for w in set(text1)))

print(f"len1: {len1}")
print(f"len2: {len2}")

# %% [markdown]
# ### Exercise 6
# 
# Write the slice expression that extracts the last two words of `text2`.

# %%
# Last two words in text2
text2[-2:]

# %% [markdown]
# ### Exercise 7
# 
# Find all the four-letter words in `text6`. With the help of a frequency distribution (`FreqDist`), show these words in decreasing order of frequency.
# 

# %%
# Find all four-letter words
four_letter_words = [word for word in text6 if len(word) == 4]

# Frequency distribution
fdist = FreqDist(four_letter_words)

# Show words in decreasing order of frequency
for item in fdist.most_common():
    print(item)

# %% [markdown]
# ### Exercise 8
# 
# Create a set for the words in `text6`. Use a `for` and an `if` statement to loop over the words in the set and print all titlecased words with more than one character, one per line.
# 

# %%
# Create a set for words in text6
text6_set = sorted(set(text6))

# Loop over the words in the set and print all titlecased words with more than one character
for word in text6_set:
    if word.istitle() and len(word) > 1:
        print(word)

# %% [markdown]
# ### Exercise 9
# 
# Write expressions for finding all words in `text6` that meet the conditions listed below:
# 
# a) ending in "ing",
# 
# b) containing the letter "z",
# 
# c) containing the letter sequence "pt".
# 

# %%
# a) words ending in "ing"
print("Words ending in 'ing':")
print(sorted(word for word in set(text6) if word.endswith("ing")))

# b) words containing the letter "z"
print("\nWords containing the letter 'z':")
print(sorted(word for word in text6 if "z" in word or "Z" in word))

# c) words containing the letter sequence "pt"
print("\nWords containing the letter sequence 'pt':")
print(sorted(word for word in set(text6) if "pt" in word or "Pt" in word))

# %% [markdown]
# ### Exercise 10
# 
# Define `sent` to be the list of words `['she', 'sells', 'sea', 'shells', 'by', 'the', 'sea', 'shore']`. Now write code to perform the following tasks:
# 
# a) print all words beginning with "sh",
# 
# b) print all words longer than four characters.

# %%
# Exercise 10

# Define the list 'sent'
sent = ['she', 'sells', 'sea', 'shells', 'by', 'the', 'sea', 'shore']

# a) print all words beginning with "sh"
print("Words beginning with 'sh':")
print(sorted(word for word in sent if word.startswith("sh")))

# b) print all words longer than four characters
print("\nWords longer than four characters:")
print(sorted(word for word in sent if len(word) > 4))

# %% [markdown]
# ### Exercise 11
# 
# What does the following Python code do?
# 
# `sum(len(w) for w in text1)`
# 
# Can you use it to work out the average word length of `text1`?

# %% [markdown]
# This Python code iterates through the `text1`, counts the length of word and then sumup all together. So it means, it will calculate the number of all characters in the `text1`, so not only the letters, but also punctuation characters and so on.

# %%
# Calculate the total number of characters
characters_total = sum(len(w) for w in text1)

# Calculate the total number of words
words_total = len(text1)

# Calculate the average word length
average_word_length = characters_total / words_total

print(f"Total number of characters in text1: {characters_total}")
print(f"Total number of words in text1: {words_total}")
print(f"Average word length in text1: {average_word_length}")

# %% [markdown]
# ### Exercise 12
# 
# Define a function `freq(word, text)` that calculates how often a given word occurs in a text, not using `count()` but a `FreqDist`. Use the function to calculate how often "promise" appears in `text4`.

# %%
# Function to calculate how often a given word occurs in a text
def freq(word, text):
  return FreqDist(text)[word]

# Calculate how often 'promise' appears in text4
print(f"The word 'promise' appears {freq('promise', text4)} times in text4.")

# %%



