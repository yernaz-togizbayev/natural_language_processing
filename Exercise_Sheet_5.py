# -*- coding: utf-8 -*-
"""Exercise_Sheet_5.ipynb

# Natural Language Processing

## Exercise Sheet 5
"""

#imports for all exercises
import nltk

from nltk import FreqDist
from nltk.corpus import brown
from collections import defaultdict

nltk.download('brown')
nltk.download('universal_tagset')

"""### Exercise 1

Produce a sorted list of tags used in the Brown corpus, removing duplicates. Do the same for the universal part-of-speech tagset.
"""

brown_tags = sorted(list(set([tag for _, tag in brown.tagged_words()])))
universal_tags = sorted(list(set([tag for _, tag in brown.tagged_words(tagset='universal')])))

print("Brown Corpus Tags: ", brown_tags)
print("Universal Tagset Tags: ", universal_tags)

"""### Exercise 2

Write a program to process the Brown Corpus using the universal part-of-speech tagset to find out which nouns are more common in their plural form than in their singular form. Only consider regular plurals formed with the "-s" suffix. Print an alphabetically sorted list of the nouns together with the frequencies for the singular and plural forms, one per line.

"""

def find_common_plurals(corpus):
  # Get all tagged words from the Brown corpus with universal tagset
  universal_words = corpus.tagged_words(tagset='universal')

  # Create dictionaries to store frequencies of singular and plural nouns
  singular_nouns = defaultdict(int)
  plural_nouns   = defaultdict(int)

  # Iterate through the tagged words and count frequencies of singular and plural nouns
  for word, tag in universal_words:
    if tag == 'NOUN'and word.isalpha():
      word = word.lower()
      (plural_nouns if word.endswith('s') else singular_nouns)[word] += 1

  # Find nouns where the plural form is more common than the singular form
  common_plurals = {}
  for word, freq in plural_nouns.items():
    word_singular = word[:-1]

    # Check if the singular form exists and its frequency is less than the plural form's
    if word_singular in singular_nouns and freq > singular_nouns[word_singular]:
      common_plurals[word_singular] = (singular_nouns[word_singular], freq)

  return common_plurals


result = find_common_plurals(brown)

for noun in sorted(result.keys()):
    singular_freq, plural_freq = result[noun]
    print(f"{noun:<20} Singular frequency = {singular_freq:<10} Plural frequency = {plural_freq}")

"""### Exercise 3

Find out which word has the greatest number of distinct tags in the Brown corpus using the original tagset. Without using the `most_common` function, print a list of the tags together with the frequencies for the word, sorted by frequency from highest to lowest, one per line.


"""

# Count tag frequencies for each word
tag_fd = defaultdict(FreqDist)
[tag_fd[w.lower()].update([t]) for (w, t) in brown.tagged_words()]

# Find the word with the greatest number of distinct tags
max_word = max(tag_fd, key=lambda word: len(tag_fd[word]))
max_tags = tag_fd[max_word]

print(f"Word with the greatest number of distinct tags: '{max_word}'")
print(f"Number of distinct tags: {len(max_tags)}\n")

print(f"Tag\t Frequency")
print("------------------")
for tag, freq in sorted(max_tags.items(), key=lambda x: x[1], reverse=True):
    print(f"{tag:<8} {freq}")

"""### Exercise 4

Tabulate the frequencies of the universal tags that precede nouns in the Brown Corpus.
"""

# Get the sequence of (word, tag) pairs using the universal tagset
universal_words = brown.tagged_words(tagset='universal')

# Create bigrams of (word, tag) pairs
word_tag_pairs = nltk.bigrams(universal_words)

# Collect all tags that precede NOUNs
noun_preceders = [a[1] for (a, b) in word_tag_pairs if b[1] == 'NOUN']

# Tabulate frequencies
preceding_fd = FreqDist(noun_preceders)

print(f"Tag\t Frequency")
print("------------------")
for tag, freq in sorted(preceding_fd.items(), key=lambda x: x[1], reverse=True):
    print(f"{tag:<8} {freq}")

"""### Exercise 5

Write a function `ambiguous(tagged_text)` that returns the number of ambiguous word types as well as the number of all word types in a tagged text. A word type is ambiguous if it is tagged with at least two different tags. Use the function to print both values as well as the percentage of ambiguous word types for the Brown Corpus both for the original and the universal tagset.
"""

def ambiguous(tagged_text):
  word_to_tags = defaultdict(set)
  # Collect all unique tags for each word type
  for word, tag in tagged_text:
    word_to_tags[word.lower()].add(tag)

  total_word_types = len(word_to_tags)
  word_types_count = 0

  for word_type, tags_set in word_to_tags.items():
    if len(tags_set) >= 2:
      word_types_count += 1

  percentage = (word_types_count / total_word_types) * 100 if total_word_types > 0 else 0

  return total_word_types, word_types_count, percentage


# Analyze Brown Corpus with original tagset
original_tagged_words = brown.tagged_words()
total_original, ambiguous_original, percent_original = ambiguous(original_tagged_words)

print("Brown Corpus (Original Tagset):")
print(f"Number of all word types: {total_original}")
print(f"Number of ambiguous word types: {ambiguous_original}")
print(f"Percentage of ambiguous word types: {percent_original:.2f}%")
print("\n")

# Analyze Brown Corpus with universal tagset ---
universal_tagged_words = brown.tagged_words(tagset='universal')
total_universal, ambiguous_universal, percent_universal = ambiguous(universal_tagged_words)

print("Brown Corpus (Universal Tagset):")
print(f"Number of all word types: {total_universal}")
print(f"Number of ambiguous word types: {ambiguous_universal}")
print(f"Percentage of ambiguous word types: {percent_universal:.2f}%")

"""### Exercise 6

Write code to search the Brown Corpus to answer the following questions:

a) produce an alphabetically sorted list of the distinct words tagged as `MD`  
b) identify words that can be plural nouns or third person singular verbs  
c) print an alphabetically sorted list of distinct three-word prepositional phrases of the form `IN+AT+NN`, separated by semicolons

"""

# (a) Alphabetically sorted list of distinct words tagged as MD
md_words = sorted({w.lower() for (w, t) in brown.tagged_words() if t == 'MD'})
print("(a) Words tagged MD:")
print(md_words)
print()

# (b) Words that can be either plural nouns (NNS) or 3rd person singular verbs
from collections import defaultdict
word_tags = defaultdict(set)
for w, t in brown.tagged_words():
    word_tags[w.lower()].add(t)

nns_vbz = sorted([w for w, tags in word_tags.items() if 'NNS' in tags and 'VBZ' in tags])
print("(b) Words that are NNS or VBZ (both):")
print(nns_vbz)
print()

# (c) Distinct three-word prepositional phrases of the form IN + AT + NN
phrases = set()
for sent in brown.tagged_sents():
  for i in range(len(sent) - 2):
    (w1, t1), (w2, t2), (w3, t3) = sent[i], sent[i+1], sent[i+2]
    if t1 == 'IN' and t2 == 'AT' and t3 == 'NN':
      phrases.add(f"{w1.lower()} {w2.lower()} {w3.lower()}")

phrases_sorted = sorted(phrases)
print("(c) IN+AT+NN three-word prepositional phrases:")
print("; ".join(phrases_sorted))

"""### Exercise 7

Write a function `prec_adv(word, text)` that returns an alphabetically sorted list of distinct adverbs that precede `word` in `text`. Use this function to find out which adverbs precede the words "love", "like", and "prefer" in the Brown corpus.
"""

def prec_adv(word, text):
  preceding_adverbs = set()
  # Iterate through bigrams of (word, tag) pairs
  for (w1, t1), (w2, t2) in nltk.bigrams(text):
    # Check if the second word matches the target
    # and the first word is an adverb
    if w2.lower() == word.lower() and t1 == 'ADV':
      preceding_adverbs.add(w1.lower())
  return sorted(list(preceding_adverbs))

# Use Brown corpus with the universal tagset
brown_tagged_sents = brown.tagged_words(tagset='universal')

# Test for the given words
for target in ['love', 'like', 'prefer']:
  advs = prec_adv(target, brown_tagged_sents)
  print(f"Adverbs preceding '{target}': {advs}")