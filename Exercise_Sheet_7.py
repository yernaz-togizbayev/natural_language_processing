# %% [markdown]
# # Natural Language Processing
# 
# ## Exercise Sheet 7

# %%
#imports for all exercises
import nltk

# %% [markdown]
# ### Exercise 1
# 
# Extend the chunk grammar

# %%
grammar = "NP: {<DT>?<JJ>*<NN>}"

# %% [markdown]
# to also match noun phrases containing plural head nouns. Test your grammar with the following sentences:

# %%
sentence1 = [("many", "JJ"), ("dogs", "NNS"), ("barked", "VBD"), ("at", "IN"), ("the", "DT"), ("cat", "NN")]
sentence2 = [("two", "CD"), ("dogs", "NNS"), ("barked", "VBD"), ("at", "IN"), ("the", "DT"), ("cat", "NN")]
sentence3 = [("both", "DT"), ("new", "JJ"), ("dogs", "NNS"), ("barked", "VBD"),("at", "IN"),  ("the", "DT"), 
             ("cat", "NN")]

# %%
# List of sentences
sentences = [sentence1, sentence2, sentence3]

# %%
grammar = "NP: {<DT|CD>?<JJ>*<NN|NNS>}"

cp = nltk.RegexpParser(grammar)

results = [cp.parse(s) for s in sentences]

for i, sent in enumerate(results, start=1):
    print(f"\nChunked Sentence {i}:")
    print(sent.pprint(margin=60))
    sent.pretty_print(unicodelines=True, nodedist=15)

# %% [markdown]
# ### Exercise 2
# 
# Extend the grammar from Exercise 1 to also cover noun phrases that contain gerunds. Test your grammar with the following sentences and the sentences from Exercise 1:

# %%
sentence4 = [("many", "JJ"), ("dogs", "NNS"), ("barked", "VBD"), ("at", "IN"), 
             ("the", "DT"), ("meowing", "VBG"), ("cat", "NN")]
sentence5 = [("the", "DT"), ("man", "NN"), ("wants", "VBZ"), ("to", "TO"), ("become", "VB"), 
             ("assistant", "NN"), ("managing", "VBG"), ("director", "NN")] 

# %%
# append sentences 4 & 5 to results list
sentences.append(sentence4)
sentences.append(sentence5)

# %%
grammar = "NP: {<DT|CD>?<JJ|VBG|NN>*<NN|NNS>}"

cp = nltk.RegexpParser(grammar)

results = [cp.parse(s) for s in sentences]

for i, sent in enumerate(results, start=1):
    print(f"\nChunked Sentence {i}:")
    print(sent.pprint(margin=60))
    sent.pretty_print(unicodelines=True, nodedist=15)

# %% [markdown]
# ### Exercise 3
# 
# Extend the grammar from Exercise 2 to also  handle coordinated noun phrases. Test your grammar with the following sentences and the sentences from Exercise 1 and 2:

# %%
sentence6 = [("the", "DT"), ("man", "NN"), ("wants", "VBZ"), ("to", "TO"), ("leave", "VB"),  ("in", "IN"), 
             ("July", "NNP"), ("or", "CC"), ("August", "NNP")]
sentence7 = [("Donald", "NNP"), ("fired", "VBD"), ("all", "PDT"), ("your", "PRP$"), ("managers", "NNS"), 
             ("and", "CC"), ("supervisors", "NNS")]
sentence8 = [("company", "NN"), ("personnel", "NN"), ("policy", "NN"), ("has", "VBZ"), ("always", "RB"), 
             ("been", "VBN"), ("the", "DT"), ("law", "NN"), ("that", "WDT"), ("rules", "VBZ"), 
             ("company", "NN"),  ("courts", "NN"), ("and", "CC"), ("adjudicators", "NNS")]

# %%
# append sentences 6, 7 & 8 to results list
sentences.append(sentence6)
sentences.append(sentence7)
sentences.append(sentence8)

# %%
grammar = r"""
          NP: {<DT|CD|PDT|PRP\$>*<JJ|VBG|NN>*<NN|NNS|NNP>}
          NP: {<NP>(<CC><NP>)+}
          """

cp = nltk.RegexpParser(grammar)

results = [cp.parse(sent) for sent in sentences]

for i, sent in enumerate(results, start=1):
    print(f"\nChunked Sentence {i}:")
    print(sent.pprint(margin=60))
    sent.pretty_print(unicodelines=True, nodedist=5)
    print('---' * 10)
results[5].draw()  # Draw parse tree for sentence 6

# %% [markdown]
# ### Exercise 4
# 
# Extend the chunk grammar from Exercise 1 to a multi-stage chunk grammar for a cascaded chunker that produces the following output for the three test sentences:
# 
#     (S
#       (NP many/JJ dogs/NNS)
#       (VP barked/VBD (PP at/IN (NP the/DT cat/NN))))
#     (S
#       (NP two/CD dogs/NNS)
#       (VP barked/VBD (PP at/IN (NP the/DT cat/NN))))
#     (S
#       (NP both/DT new/JJ dogs/NNS)
#       (VP barked/VBD (PP at/IN (NP the/DT cat/NN))))

# %%


# %% [markdown]
# ### Exercise 5
# 
# Extend the multi-stage chunk grammar from Exercise 4 to also cover the test sentences from Exercise 2:
# 
#     (S
#       (NP many/JJ dogs/NNS)
#       (VP barked/VBD (PP at/IN (NP the/DT meowing/VBG cat/NN))))
#     (S
#       (NP the/DT man/NN)
#       (VP
#         wants/VBZ
#         (INFCL
#           to/TO
#           (VP become/VB (NP assistant/NN managing/VBG director/NN))))) 
# 

# %%


# %% [markdown]
# ### Exercise 6
# 
# Extend the multi-stage chunk grammar from Exercise 5 to also cover the test sentences from Exercise 3:
# 
#     (S
#       (NP the/DT man/NN)
#       (VP
#         wants/VBZ
#         (INFCL
#           to/TO
#           (VP leave/VB (PP in/IN (NP July/NNP or/CC August/NNP))))))
#     (S
#       (NP Donald/NNP)
#       (VP
#         fired/VBD
#         (NP all/PDT your/PRP$ managers/NNS and/CC supervisors/NNS)))
#     (S
#       (NP company/NN personnel/NN policy/NN)
#       (VP
#         has/VBZ
#         always/RB
#         been/VBN
#         (NPRC
#           (NP the/DT law/NN)
#           (RELCL
#             that/WDT
#             (VP
#               rules/VBZ
#               (NP company/NN courts/NN and/CC adjudicators/NNS))))))

# %%


# %% [markdown]
# ### Exercise 7
# 
# Select the VP chunks from the "train" portion of the CoNLL 2000 Chunking Data Corpus. Create a list of all the tag sequences that occur with each instance of this chunk type. Use a `FreqDist` to display the 100 most common tag sequences.  

# %%



