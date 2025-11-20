# %% [markdown]
# # Natural Language Processing
# 
# ## Exercise Sheet 6

# %%
#imports for all exercises
import nltk
import random
import pickle

from nltk.corpus import names
from nltk.corpus import brown
from nltk.corpus import senseval
from nltk.corpus import ppattach
from nltk.classify import apply_features
from nltk.classify import NaiveBayesClassifier
from nltk.tag import UnigramTagger, BigramTagger, TrigramTagger

nltk.download('names')
nltk.download('brown')
nltk.download('senseval')
nltk.download('ppattach')
nltk.download('universal_tagset')

# %% [markdown]
# ### Exercise 1
# 
# Write a name gender classifier using the Names Corpus, the `apply_features` function, shuffling, and a test set of 500 instances. Use the following features:
# 
# a) first letter;  
# b) last letter;  
# c) last two letters;  
# d) length;  
# e) for each letter one feature, which is true if the name contains the letter.
# 
# Use the `NaiveBayesClassifier`, calculate the accuracy, and display the 10 most informative features.
# 

# %%
def gender_features(name):
  name = name.lower()

  features = {}
  features["first_letter"] = name[0]            # (a)
  features["last_letter"] = name[-1]            # (b)
  features["last_two_letters"] = name[-2:]      # (c)
  features["length"] = len(name)                # (d)
  for letter in 'abcdefghijklmnopqrstuvwxyz':   # (e)
    features["has({})".format(letter)] = (letter in name)

  return features

labeled_names = ([(name, 'male') for name in names.words('male.txt')] +
                 [(name, 'female') for name in names.words('female.txt')])
random.shuffle(labeled_names)

train_set = apply_features(gender_features, labeled_names[500:])
test_set = apply_features(gender_features, labeled_names[:500])

classifier = nltk.NaiveBayesClassifier.train(train_set)

print(nltk.classify.accuracy(classifier, test_set))
classifier.show_most_informative_features(10)

# %% [markdown]
# ### Exercise 2
# 
# The Senseval 2 Corpus contains data intended to train word-sense disambiguation classifiers. Using this dataset, build a `NaiveBayesClassifier` that predicts the correct sense tag for a given instance for the word "hard":

# %%
def features(inst):
  p = inst.position
  features = {}

  preceding_word = inst.context[p - 1][0].lower() if (p > 0) else "<START>"
  following_word = inst.context[p + 1][0].lower() if (p + 1 < len(inst.context)) else "<END>"

  features["prev_word"] = preceding_word
  features["next_word"] = following_word

  return features


# %%
instances = senseval.instances('hard.pos')
labeled_instances = [(inst, inst.senses) for inst in instances]
size = int(len(labeled_instances) * 0.1)

# %% [markdown]
# Use the preceding and following word as features. They can be calculated by retrieving the position of the word "hard" as `p=inst.position` and then accessing `inst.context[p-1]` and `inst.context[p+1]`.
# 
# Run 10 iterations by reshuffling the instances and printing the individual accuracies. Finally, print the average accuracy.

# %%
accuracies = []

for i in range(10):
    random.shuffle(labeled_instances)
    train_set = apply_features(features, labeled_instances[size:])
    test_set = apply_features(features, labeled_instances[:size])
    classifier = NaiveBayesClassifier.train(train_set)
    accuracy = nltk.classify.accuracy(classifier, test_set)
    accuracies.append(accuracy)
    print(f"Iteration {i+1}: \taccuracy = {accuracy:.4f}")

average_accuracy = sum(accuracies) / len(accuracies)
print(f"\nAverage accuracy over {len(accuracies)} iterations: {average_accuracy:.4f}")

# %% [markdown]
# ### Exercise 3
# 
# The synonyms "strong" and "powerful" pattern differently. Use the tagged Brown corpus with the universal tagset to first list the nouns which follow "strong" vs. "powerful". Write for this a function `next_noun(word, tagged_text)` which returns the list of nouns that follow `word` in the `tagged_text`. Build then a `NaiveBayesClassifier` that predicts when each word should be used by using the function `apply_features` and the following noun as single feature.
# 
# Run 10 iterations by reshuffling the instances and printing the individual accuracies. Finally, print the average accuracy.
# 

# %%
def next_noun(word, tagged_text):
  nouns = []
  for sent in tagged_text:
    for i in range(len(sent) - 1):
      (w1, t1), (w2, t2) = sent[i], sent[i+1]
      if w1.lower() == word and t2 == 'NOUN':
        nouns.append(w2.lower())
  return nouns

tagged_corpus = brown.tagged_sents(tagset='universal')

nouns_following_strong   = next_noun('strong', tagged_corpus)
nouns_following_powerful = next_noun('powerful', tagged_corpus)

print("Nouns following 'strong':")
print(sorted(set(nouns_following_strong)))

print("\nNouns following 'powerful':")
print(sorted(set(nouns_following_powerful)))
print()

labeled_instances = ([(noun, 'strong') for noun in nouns_following_strong] +
                    [(noun, 'powerful') for noun in nouns_following_powerful])

def features(noun):
  return {'next_noun': noun}


accuracies = []

for i in range(10):
  random.shuffle(labeled_instances)
  size = int(len(labeled_instances) * 0.1)
  train_set = apply_features(features, labeled_instances[size:])
  test_set = apply_features(features, labeled_instances[:size])
  classifier = NaiveBayesClassifier.train(train_set)
  accuracy = nltk.classify.accuracy(classifier, test_set)
  accuracies.append(accuracy)
  print(f"Iteration {i+1}: \taccuracy = {accuracy:.4f}")

average_accuracy = sum(accuracies) / len(accuracies)
print(f"\nAverage accuracy over {len(accuracies)} iterations: {average_accuracy:.4f}")


# %% [markdown]
# ### Exercise 4
# 
# Based on the Movie Reviews document classifier discussed in this chapter, build a new `NaiveBayesClassifier`. Tag first the Movie Reviews Corpus using the combined tagger from the previous chapter stored in `t2.pkl`. Filter the tagged words to contain only words for the tags `['JJ', 'JJR', 'JJS', 'RB', 'NN', 'NNS', 'VB', 'VBN', 'VBG', 'VBZ', 'VBD', 'QL']` as well as only alphabetic tokens with at least three characters. Convert the words to lowercase. Use the most common 5000 words as `word_features` in the function `document_features`.
# 
# Run 10 iterations by reshuffling the instances and printing the accuracy and 5 most informative features for each iteration. Finally, print the average accuracy.
#     

# %% [markdown]
# ### Exercise 5
# 
# The PP Attachment Corpus is a corpus describing prepositional phrase attachment decisions. Each instance in the training corpus is encoded as a `PPAttachment` object:
# 
#     from nltk.corpus import ppattach
#     ppattach.attachments('training')
#     
#         [PPAttachment(sent='0', verb='join', noun1='board',
#             prep='as', noun2='director', attachment='V'),
#         PPAttachment(sent='1', verb='is', noun1='chairman',
#             prep='of', noun2='N.V.', attachment='N'),
#         ...]
# 
#     inst = ppattach.attachments('training')[1]
#     (inst.noun1, inst.prep, inst.noun2)
#     
#         ('chairman', 'of', 'N.V.')
# 
# In the same way, `ppattach.attachments('test')` accesses the test instances. Select only the instances where `inst.attachment` is `'N'`:

# %%
from nltk.corpus import ppattach
nattach = [inst for inst in ppattach.attachments('training')
               if inst.attachment == 'N']

# %% [markdown]
# Using this sub-corpus, build a `NaiveBayesClassifier` that attempts to predict which preposition is used to connect a given pair of nouns. For example, given the pair of nouns "team" and "researchers", the classifier should predict the preposition "of".
# 
# Write for this purpose a function `prepare_featuresets(subcorpus)`, where `subcorpus` is either the string "training" or "test" to return the training set or the test set.
# 
# Print the achieved accuracy as well as the result of `classifier.classify({ 'noun1': 'team', 'noun2': 'researchers' })`.

# %%
def prepare_featuresets(subcorpus):
  filtered = (inst for inst in ppattach.attachments(subcorpus) if inst.attachment == 'N')
  return [({'noun1': inst.noun1.lower(), 'noun2': inst.noun2.lower()}, inst.prep) for inst in filtered]

training_set = prepare_featuresets('training')
test_set     = prepare_featuresets('test')

classifier = NaiveBayesClassifier.train(training_set)

accuracy = nltk.classify.accuracy(classifier, test_set)
print(f'Test Accuracy: {accuracy:.4f}')

pred = classifier.classify({'noun1': 'team', 'noun2': 'researchers'})
print(f"Predicted preposition for ('team', 'researchers'): {pred}")


