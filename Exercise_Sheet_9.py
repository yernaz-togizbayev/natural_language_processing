# -*- coding: utf-8 -*-

#imports for all exercises
import nltk
from nltk import grammar, parse

"""### Exercise 1

Take the following grammar:
"""

# Commented out IPython magic to ensure Python compatibility.
g = """
# %start S
S                    -> NP[AGR=?n] VP[AGR=?n]
NP[AGR=?n]           -> PropN[AGR=?n]
NP[AGR=?n]           -> Pro[AGR=?n]
VP[TENSE=?t, AGR=?n] -> Cop[TENSE=?t, AGR=?n] Adj

# Copula forms with person and number agreement
Cop[TENSE=pres, AGR=[NUM=sg, PER=1]] -> 'am'
Cop[TENSE=pres, AGR=[NUM=sg, PER=3]] -> 'is'
Cop[TENSE=pres, AGR=[NUM=pl, PER=1]] -> 'are'
Cop[TENSE=pres, AGR=[NUM=pl, PER=2]] -> 'are'
Cop[TENSE=pres, AGR=[NUM=pl, PER=3]] -> 'are'
Cop[TENSE=pres, AGR=[NUM=sg, PER=2]] -> 'are'

# Proper nouns
PropN[AGR=[NUM=sg, PER=3]] -> 'Kim'

# Pronouns with agreement features
Pro[AGR=[NUM=sg, PER=1]] -> 'I'
Pro[AGR=[NUM=sg, PER=2]] -> 'you'
Pro[AGR=[NUM=sg, PER=3]] -> 'she'
Pro[AGR=[NUM=sg, PER=3]] -> 'he'
Pro[AGR=[NUM=pl, PER=1]] -> 'we'
Pro[AGR=[NUM=pl, PER=2]] -> 'you'
Pro[AGR=[NUM=pl, PER=3]] -> 'they'

# Adjectives
Adj -> 'happy'
"""
gr = grammar.FeatureGrammar.fromstring(g)

def parse_sent(sent, gr):
    tokens = sent.split()
    parser = parse.FeatureEarleyChartParser(gr)
    trees = parser.parse(tokens)
    for tree in trees: print(tree)

"""as starting point to correctly parse word sequences like "I am happy" and "she is happy" but not " * you is happy" or " * they am happy"."""

sent1 = "I am happy"
sent2 = "she is happy"
sent3 = "you is happy"
sent4 = "they am happy"

def parse_sent(sent, gr):
    tokens = sent.split()
    parser = parse.FeatureEarleyChartParser(gr)
    trees = list(parser.parse(tokens))

    if trees:
        print(f"✓ '{sent}' - GRAMMATICAL")
        for tree in trees:
            print(tree)
    else:
        print(f"✗ '{sent}' - UNGRAMMATICAL (no parse found)")
    print()

# Valid sentences
parse_sent(sent1, gr)
parse_sent(sent2, gr)

# Invalid sentences
parse_sent(sent3, gr)
parse_sent(sent4, gr)

"""### Exercise 2

Develop a variant of the following grammar
"""

# Commented out IPython magic to ensure Python compatibility.
g = """
# %start S
# ###################
# Grammar Productions
# ###################

# S expansion productions
S -> NP[NUM=?n] VP[NUM=?n]

# NP expansion productions
# Count singular nouns REQUIRE a determiner
NP[NUM=sg, COUNT=count_sg] -> Det[NUM=sg] N[NUM=sg, COUNT=count_sg]

# Count plural nouns CAN appear bare (without determiner)
NP[NUM=pl, COUNT=count_pl] -> Det[NUM=pl] N[NUM=pl, COUNT=count_pl]
NP[NUM=pl, COUNT=count_pl] -> N[NUM=pl, COUNT=count_pl]

# Mass nouns CAN appear bare (with or without determiner)
NP[NUM=sg, COUNT=mass] -> Det[NUM=sg] N[NUM=sg, COUNT=mass]
NP[NUM=sg, COUNT=mass] -> N[NUM=sg, COUNT=mass]

# Proper nouns (always bare)
NP[NUM=sg] -> PropN[NUM=sg]

# VP expansion productions
VP[NUM=?n] -> IV[NUM=?n]
VP[NUM=?n] -> TV[NUM=?n] NP
VP[NUM=?n] -> Cop[NUM=?n] Adj

# ###################
# Lexical Productions
# ###################

# Determiners
Det[NUM=sg] -> 'this' | 'every' | 'the'
Det[NUM=pl] -> 'these' | 'all' | 'the'
Det -> 'some' | 'several'

# Proper Nouns
PropN[NUM=sg] -> 'Kim' | 'Jody'

# Count Nouns (singular)
N[NUM=sg, COUNT=count_sg] -> 'dog' | 'girl' | 'car' | 'child' | 'boy'

# Count Nouns (plural)
N[NUM=pl, COUNT=count_pl] -> 'dogs' | 'girls' | 'cars' | 'children' | 'boys'

# Mass Nouns (singular only)
N[NUM=sg, COUNT=mass] -> 'water' | 'milk' | 'rice' | 'information'

# Intransitive Verbs
IV[NUM=sg] -> 'disappears' | 'walks' | 'sings'
IV[NUM=pl] -> 'disappear' | 'walk' | 'sing'

# Transitive Verbs
TV[NUM=sg] -> 'sees' | 'likes'
TV[NUM=pl] -> 'see' | 'like'

# Copula
Cop[NUM=sg] -> 'is'
Cop[NUM=pl] -> 'are'

# Adjectives
Adj -> 'precious' | 'happy' | 'beautiful'
"""
gr = grammar.FeatureGrammar.fromstring(g)

def parse_sent(sent, gr):
    tokens = sent.split()
    parser = parse.FeatureEarleyChartParser(gr)
    trees = parser.parse(tokens)
    for tree in trees: print(tree)

"""that uses a feature `COUNT` to make the distinctions shown below:

(1a) the boy sings

(1b) * boy sings

(2a) the boys sing

(2b) boys sing

(3a) the water is precious

(3b) water is precious
"""

sent1 = "the boy sings"
sent2 = "boy sings"
sent3 = "the boys sing"
sent4 = "boys sing"
sent5 = "the water is precious"
sent6 = "water is precious"

def parse_sent(sent, gr):
    tokens = sent.split()
    parser = parse.FeatureEarleyChartParser(gr)
    trees = list(parser.parse(tokens))

    if trees:
        print(f"✓ '{sent}' - GRAMMATICAL")
        for tree in trees:
            print(tree)
    else:
        print(f"✗ '{sent}' - UNGRAMMATICAL (no parse found)")
    print()

parse_sent(sent1, gr)
parse_sent(sent2, gr)
parse_sent(sent3, gr)
parse_sent(sent4, gr)
parse_sent(sent5, gr)
parse_sent(sent6, gr)

"""### Exercise 3

Extend the German grammar
"""

# Commented out IPython magic to ensure Python compatibility.
g = """
# %start S

# Grammar Productions

# Standard sentence structure (SVO)
S -> NP[CASE=nom, AGR=?a] VP[AGR=?a]

# Verb-second structure (V2): ADV + Verb + Subject + Object
# Using slash category S/TV (S missing a TV)
S -> ADV TV[OBJCASE=?c, AGR=?a] S/TV[OBJCASE=?c, AGR=?a]

# S/TV represents a sentence missing the transitive verb
# It consists of subject (nominative) and object (with appropriate case)
S/TV[OBJCASE=?c, AGR=?a] -> NP[CASE=nom, AGR=?a] NP[CASE=?c]

# Standard VP rules
NP[CASE=?c, AGR=?a] -> PRO[CASE=?c, AGR=?a]
NP[CASE=?c, AGR=?a] -> Det[CASE=?c, AGR=?a] N[CASE=?c, AGR=?a]

VP[AGR=?a] -> IV[AGR=?a]
VP[AGR=?a] -> TV[OBJCASE=?c, AGR=?a] NP[CASE=?c]

# Lexical Productions

# Adverbs
ADV -> 'heute' | 'morgen' | 'gestern'

# Singular determiners
# masculine
Det[CASE=nom, AGR=[GND=masc,PER=3,NUM=sg]] -> 'der'
Det[CASE=dat, AGR=[GND=masc,PER=3,NUM=sg]] -> 'dem'
Det[CASE=acc, AGR=[GND=masc,PER=3,NUM=sg]] -> 'den'

# feminine
Det[CASE=nom, AGR=[GND=fem,PER=3,NUM=sg]] -> 'die'
Det[CASE=dat, AGR=[GND=fem,PER=3,NUM=sg]] -> 'der'
Det[CASE=acc, AGR=[GND=fem,PER=3,NUM=sg]] -> 'die'

# Plural determiners
Det[CASE=nom, AGR=[PER=3,NUM=pl]] -> 'die'
Det[CASE=dat, AGR=[PER=3,NUM=pl]] -> 'den'
Det[CASE=acc, AGR=[PER=3,NUM=pl]] -> 'die'

# Nouns
N[AGR=[GND=masc,PER=3,NUM=sg]] -> 'Hund'
N[CASE=nom, AGR=[GND=masc,PER=3,NUM=pl]] -> 'Hunde'
N[CASE=dat, AGR=[GND=masc,PER=3,NUM=pl]] -> 'Hunden'
N[CASE=acc, AGR=[GND=masc,PER=3,NUM=pl]] -> 'Hunde'

N[AGR=[GND=fem,PER=3,NUM=sg]] -> 'Katze'
N[AGR=[GND=fem,PER=3,NUM=pl]] -> 'Katzen'

# Pronouns
PRO[CASE=nom, AGR=[PER=1,NUM=sg]] -> 'ich'
PRO[CASE=acc, AGR=[PER=1,NUM=sg]] -> 'mich'
PRO[CASE=dat, AGR=[PER=1,NUM=sg]] -> 'mir'
PRO[CASE=nom, AGR=[PER=2,NUM=sg]] -> 'du'
PRO[CASE=nom, AGR=[PER=3,NUM=sg]] -> 'er' | 'sie' | 'es'
PRO[CASE=nom, AGR=[PER=1,NUM=pl]] -> 'wir'
PRO[CASE=acc, AGR=[PER=1,NUM=pl]] -> 'uns'
PRO[CASE=dat, AGR=[PER=1,NUM=pl]] -> 'uns'
PRO[CASE=nom, AGR=[PER=2,NUM=pl]] -> 'ihr'
PRO[CASE=nom, AGR=[PER=3,NUM=pl]] -> 'sie'

# Intransitive Verbs
IV[AGR=[NUM=sg,PER=1]] -> 'komme'
IV[AGR=[NUM=sg,PER=2]] -> 'kommst'
IV[AGR=[NUM=sg,PER=3]] -> 'kommt'
IV[AGR=[NUM=pl,PER=1]] -> 'kommen'
IV[AGR=[NUM=pl,PER=2]] -> 'kommt'
IV[AGR=[NUM=pl,PER=3]] -> 'kommen'

# Transitive Verbs (accusative object)
TV[OBJCASE=acc, AGR=[NUM=sg,PER=1]] -> 'sehe' | 'mag'
TV[OBJCASE=acc, AGR=[NUM=sg,PER=2]] -> 'siehst' | 'magst'
TV[OBJCASE=acc, AGR=[NUM=sg,PER=3]] -> 'sieht' | 'mag'

# Transitive Verbs (dative object)
TV[OBJCASE=dat, AGR=[NUM=sg,PER=1]] -> 'folge' | 'helfe'
TV[OBJCASE=dat, AGR=[NUM=sg,PER=2]] -> 'folgst' | 'hilfst'
TV[OBJCASE=dat, AGR=[NUM=sg,PER=3]] -> 'folgt' | 'hilft'

# Transitive Verbs (accusative object - plural)
TV[OBJCASE=acc, AGR=[NUM=pl,PER=1]] -> 'sehen' | 'moegen'
TV[OBJCASE=acc, AGR=[NUM=pl,PER=2]] -> 'seht' | 'moegt'
TV[OBJCASE=acc, AGR=[NUM=pl,PER=3]] -> 'sehen' | 'moegen'

# Transitive Verbs (dative object - plural)
TV[OBJCASE=dat, AGR=[NUM=pl,PER=1]] -> 'folgen' | 'helfen'
TV[OBJCASE=dat, AGR=[NUM=pl,PER=2]] -> 'folgt' | 'helft'
TV[OBJCASE=dat, AGR=[NUM=pl,PER=3]] -> 'folgen' | 'helfen'
"""
gr = grammar.FeatureGrammar.fromstring(g)

def parse_sent(sent, gr):
    tokens = sent.split()
    parser = parse.FeatureEarleyChartParser(gr)
    trees = parser.parse(tokens)
    for tree in trees: print(tree)

"""so that it can handle so-called verb-second structures like "heute sieht der Hund die Katze" by using a slash category `S/TV` for the missing transitive verb in "der Hund die Katze". Use the following test sentences:"""

sent1 = "heute sieht der Hund die Katze"
sent2 = "heute sehe der Hund die Katze"
sent3 = "heute sieht der Hund die Katzen"

def parse_sent(sent, gr):
    tokens = sent.split()
    parser = parse.FeatureEarleyChartParser(gr)
    trees = list(parser.parse(tokens))

    if trees:
        print(f"✓ '{sent}' - GRAMMATICAL")
        for tree in trees:
            print(tree)
    else:
        print(f"✗ '{sent}' - UNGRAMMATICAL (no parse found)")
    print()


parse_sent(sent1, gr)
parse_sent(sent2, gr)
parse_sent(sent3, gr)

"""### Exercise 4

Consider the patterns of grammaticality for the verbs "loaded", "filled", and "dumped" below. Write grammar productions to handle such data:

(1a) the farmer loaded the cart with sand

(1b) the farmer loaded sand into the cart

(2a) the farmer filled the cart with sand

(2b) * the farmer filled sand into the cart

(3a) * the farmer dumped the cart with sand

(3b) the farmer dumped sand into the cart
"""

# Commented out IPython magic to ensure Python compatibility.
g = """
# %start S

# Grammar Productions

# Sentence structure
S -> NP[NUM=?n] VP[NUM=?n]

# VP with different subcategorization frames
VP[NUM=?n] -> TV[SUBCAT=with] NP PP[PFORM=with]
VP[NUM=?n] -> TV[SUBCAT=into] NP PP[PFORM=into]

# Noun Phrase structure
NP[NUM=?n] -> Det[NUM=?n] N[NUM=?n]
NP[NUM=?n] -> N[NUM=?n]

# Prepositional Phrase structure
PP[PFORM=?p] -> P[PFORM=?p] NP

# Lexical Productions

# Determiners
Det[NUM=sg] -> 'the' | 'a'
Det[NUM=pl] -> 'the'

# Nouns
N[NUM=sg] -> 'farmer' | 'cart' | 'sand' | 'truck' | 'grain'
N[NUM=pl] -> 'farmers' | 'carts' | 'trucks'

# Prepositions
P[PFORM=with] -> 'with'
P[PFORM=into] -> 'into'

# Transitive Verbs with subcategorization features

# "loaded" - allows BOTH frames (locative alternation)
TV[SUBCAT=with] -> 'loaded'
TV[SUBCAT=into] -> 'loaded'

# "filled" - allows ONLY "with" frame (container-oriented only)
TV[SUBCAT=with] -> 'filled'

# "dumped" - allows ONLY "into" frame (contents-oriented only)
TV[SUBCAT=into] -> 'dumped'
"""
gr = grammar.FeatureGrammar.fromstring(g)

def parse_sent(sent, gr):
    tokens = sent.split()
    parser = parse.FeatureEarleyChartParser(gr)
    trees = list(parser.parse(tokens))

    if trees:
        print(f"✓ '{sent}' - GRAMMATICAL")
        for tree in trees:
            print(tree)
    else:
        print(f"✗ '{sent}' - UNGRAMMATICAL (no parse found)")
    print()

sent1 = "the farmer loaded the cart with sand"
sent2 = "the farmer loaded sand into the cart"
sent3 = "the farmer filled the cart with sand"
sent4 = "the farmer filled sand into the cart"
sent5 = "the farmer dumped the cart with sand"
sent6 = "the farmer dumped sand into the cart"

parse_sent(sent1, gr)
parse_sent(sent2, gr)
parse_sent(sent3, gr)
parse_sent(sent4, gr)
parse_sent(sent5, gr)
parse_sent(sent6, gr)

"""### Exercise 5

Consider the following feature structures:
"""

fs1 = nltk.FeatStruct("[A = ?x, B= [C = ?x]]")
fs2 = nltk.FeatStruct("[B = [D = d]]")
fs3 = nltk.FeatStruct("[B = [C = d]]")
fs4 = nltk.FeatStruct("[A = (1)[B = b], C->(1)]")
fs5 = nltk.FeatStruct("[A = (1)[D = ?x], C = [E -> (1), F = ?x] ]")
fs6 = nltk.FeatStruct("[A = [D = d]]")
fs7 = nltk.FeatStruct("[A = [D = d], C = [F = [D = d]]]")
fs8 = nltk.FeatStruct("[A = (1)[D = ?x, G = ?x], C = [B = ?x, E -> (1)] ]")
fs9 = nltk.FeatStruct("[A = [B = b], C = [E = [G = e]]]")
fs10 = nltk.FeatStruct("[A = (1)[B = b], C -> (1)]")

"""What is the result of the following unifications?

1. `fs1` and `fs2`,  
2. `fs1` and `fs3`,  
3. `fs4` and `fs5`,  
4. `fs5` and `fs6`,  
5. `fs5` and `fs7`,  
6. `fs8` and `fs9`,  
7. `fs8` and `fs10`.  
"""

# Helper function to show unification
def unify_and_display(fs_a, fs_b, num, name_a, name_b):
    print(f"\n{num}. Unifying {name_a} and {name_b}:")
    print(f"\n{name_a} = {fs_a}")
    print(f"{name_b} = {fs_b}")
    print("\nResult:")
    try:
        result = fs_a.unify(fs_b)
        if result is None:
            print("UNIFICATION FAILS ✗")
        else:
            print(f"{result}")
    except Exception as e:
        print(f"UNIFICATION FAILS ✗ (Error: {e})")
    print("-" * 80)

# Perform all unifications
unify_and_display(fs1, fs2, 1, "fs1", "fs2")
unify_and_display(fs1, fs3, 2, "fs1", "fs3")
unify_and_display(fs4, fs5, 3, "fs4", "fs5")
unify_and_display(fs5, fs6, 4, "fs5", "fs6")
unify_and_display(fs5, fs7, 5, "fs5", "fs7")
unify_and_display(fs8, fs9, 6, "fs8", "fs9")
unify_and_display(fs8, fs10, 7, "fs8", "fs10")