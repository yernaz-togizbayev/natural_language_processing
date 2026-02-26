# -*- coding: utf-8 -*-

#imports for all exercises
import nltk

from nltk.sem import Expression

"""### Exercise 1

Translate the following sentences into propositional logic and verify that they can be processed with `Expression.fromstring()`.

1. If Angus sings, it is not the case that Bertie sulks.
2. Cyril runs and barks.
3. It will snow if it doesn't rain.
4. It's not the case that Irene will be happy if Olive or Tofu comes.
5. Pat didn't cough or sneeze.
6. If you don't come if I call, I won't come if you call.

"""

# Create a reader for logical expressions
read_expr = Expression.fromstring

# Define the sentences and their translations
sentences = [
    {
        'num': 1,
        'english': "If Angus sings, it is not the case that Bertie sulks.",
        'logic': "As -> -Bs"
    },
    {
        'num': 2,
        'english': "Cyril runs and barks.",
        'logic': "Cr & Cb"
    },
    {
        'num': 3,
        'english': "It will snow if it doesn't rain.",
        'logic': "-R -> S"
    },
    {
        'num': 4,
        'english': "It's not the case that Irene will be happy if Olive or Tofu comes.",
        'logic': "-((Oc | Tc) -> Ih)"
    },
    {
        'num': 5,
        'english': "Pat didn't cough or sneeze.",
        'logic': "-(Pc | Ps)"
    },
    {
        'num': 6,
        'english': "If you don't come if I call, I won't come if you call.",
        'logic': "-(call(i) -> come(you)) -> (call(you) -> -come(i))"
    }
]

# Process each sentence
for sent in sentences:
    print(f"\n{sent['num']}. {sent['english']}")
    print(f"   Logic: {sent['logic']}")

    try:
        expr = read_expr(sent['logic'])
        print(f"   ✓ Successfully parsed")
        print(f"   Parsed expression: {expr}")
    except Exception as e:
        print(f"   ✗ Failed to parse: {e}")

    print("-" * 80)

"""### Exercise 2

Translate the following sentences into predicate-argument formula of first order logic and verify that they can be processed with `Expression.fromstring()`.

1. Angus likes Cyril and Irene hates Cyril.
2. Tofu is taller than Bertie.
3. Bruce loves himself and Pat does too.
4. Cyril saw Bertie, but Angus didn't.
5. Cyril is a fourlegged friend.
6. Tofu and Olive are near each other.
"""

# Create a reader for logical expressions
read_expr = Expression.fromstring

# Define the sentences and their translations
sentences = [
    {
        'num': 1,
        'english': "Angus likes Cyril and Irene hates Cyril.",
        'logic': "like(angus, cyril) & hate(irene, cyril)"
    },
    {
        'num': 2,
        'english': "Tofu is taller than Bertie.",
        'logic': "taller(tofu, bertie)"
    },
    {
        'num': 3,
        'english': "Bruce loves himself and Pat does too.",
        'logic': "love(bruce, bruce) & love(pat, pat)"
    },
    {
        'num': 4,
        'english': "Cyril saw Bertie, but Angus didn't.",
        'logic': "see(cyril, bertie) & -see(angus, bertie)"
    },
    {
        'num': 5,
        'english': "Cyril is a fourlegged friend.",
        'logic': "fourlegged(cyril) & friend(cyril)"
    },
    {
        'num': 6,
        'english': "Tofu and Olive are near each other.",
        'logic': "near(tofu, olive) & near(olive, tofu)"
    }
]

# Process each sentence
for sent in sentences:
    print(f"\n{sent['num']}. {sent['english']}")
    print(f"   FOL: {sent['logic']}")

    try:
        expr = read_expr(sent['logic'])
        print(f"   ✓ Successfully parsed")
        print(f"   Expression: {expr}")
    except Exception as e:
        print(f"   ✗ Failed to parse: {e}")

    print("-" * 80)

"""### Exercise 3

Translate the following sentences into quantified formulas of first order logic and verify that they can be processed with `Expression.fromstring()`.

1. Angus likes someone and someone likes Julia.
2. Angus loves a dog who loves him.
3. Nobody smiles at Pat.
4. Somebody coughs and sneezes.
5. Nobody coughed or sneezed.
6. Bruce loves somebody other than Bruce.
7. Nobody other than Matthew loves somebody Pat.
8. Cyril likes everyone except for Irene.
9. Exactly one person is asleep.
"""

# Create a reader for logical expressions
read_expr = Expression.fromstring

# Define the sentences and their translations
sentences = [
    {
        'num': 1,
        'english': "Angus likes someone and someone likes Julia.",
        'logic': "exists x.like(angus, x) & exists y.like(y, julia)"
    },
    {
        'num': 2,
        'english': "Angus loves a dog who loves him.",
        'logic': "exists x.(dog(x) & love(angus, x) & love(x, angus))"
    },
    {
        'num': 3,
        'english': "Nobody smiles at Pat.",
        'logic': "-exists x.smile_at(x, pat)"
    },
    {
        'num': 4,
        'english': "Somebody coughs and sneezes.",
        'logic': "exists x.(cough(x) & sneeze(x))"
    },
    {
        'num': 5,
        'english': "Nobody coughed or sneezed.",
        'logic': "-exists x.(cough(x) | sneeze(x))"
    },
    {
        'num': 6,
        'english': "Bruce loves somebody other than Bruce.",
        'logic': "exists x.(x != bruce & love(bruce, x))"
    },
    {
        'num': 7,
        'english': "Nobody other than Matthew loves somebody Pat.",
        'logic': "all x.((x != matthew) -> -love(x, pat))"
    },
    {
        'num': 8,
        'english': "Cyril likes everyone except for Irene.",
        'logic': "all x.((x != irene) -> like(cyril, x))"
    },
    {
        'num': 9,
        'english': "Exactly one person is asleep.",
        'logic': "exists x.(asleep(x) & all y.(asleep(y) -> (y = x)))"
    }
]

# Process each sentence
for sent in sentences:
    print(f"\n{sent['num']}. {sent['english']}")
    print(f"   FOL: {sent['logic']}")

    try:
        expr = read_expr(sent['logic'])
        print(f"   ✓ Successfully parsed")
        print(f"   Expression: {expr}")
    except Exception as e:
        print(f"   ✗ Failed to parse: {e}")

    print("-" * 80)

"""### Exercise 4

Translate the following verb phrases using $\lambda$-abstracts quantified formulas of first order logic and verify that they can be processed with `Expression.fromstring()`.

1. feed Cyril and give a capuccino to Angus
2. be given 'War and Peace' by Pat
3. be loved by everyone
4. be loved or detested by everyone
5. be loved by everyone and detested by no-one
"""

# Create a reader for logical expressions
read_expr = Expression.fromstring

# Define the verb phrases and their λ-abstract translations
verb_phrases = [
    {
        'num': 1,
        'english': "feed Cyril and give a cappuccino to Angus",
        'logic': "\\x.(feed(x, cyril) & give(x, cappuccino, angus))"
    },
    {
        'num': 2,
        'english': "be given 'War and Peace' by Pat",
        'logic': "\\x.give(pat, war_and_peace, x)"
    },
    {
        'num': 3,
        'english': "be loved by everyone",
        'logic': "\\x.all y.love(y, x)"
    },
    {
        'num': 4,
        'english': "be loved or detested by everyone",
        'logic': "\\x.all y.(love(y, x) | detest(y, x))"
    },
    {
        'num': 5,
        'english': "be loved by everyone and detested by no-one",
        'logic': "\\x.(all y.love(y, x) & -exists z.detest(z, x))"
    }
]

# Process each verb phrase
for vp in verb_phrases:
    print(f"\n{vp['num']}. '{vp['english']}'")
    print(f"   λ-abstract: {vp['logic']}")

    try:
        expr = read_expr(vp['logic'])
        print(f"   ✓ Successfully parsed")
        print(f"   Expression: {expr}")
        print(f"   Type: {type(expr).__name__}")
    except Exception as e:
        print(f"   ✗ Failed to parse: {e}")

    print("-" * 80)

"""### Exercise 5

Consider the following statements:

    read_expr = nltk.sem.Expression.fromstring
    e2 = read_expr('pat')
    e3 = nltk.sem.ApplicationExpression(e1, e2)
    print(e3.simplify())
        exists y.love(pat, y)

Clearly something is missing here, namely a declaration of the value of `e1`. In order for `ApplicationExpression(e1, e2)` to be $\beta$-convertible to `exists y.love(pat, y)`, `e1` must be a $\lambda$-abstract which can take `pat` as an argument. Your task is to construct such an abstract, bind it to `e1`, and satisfy yourself that the statements above are all satisfied (up to alphabetic variance).

Now carry on doing this same task for the further cases of `e3.simplify()` shown below.

    print(e3.simplify())
        exists y.(love(pat,y) | love(y,pat))

    print(e3.simplify())
        walk(pat)
"""

read_expr = nltk.sem.Expression.fromstring

# Case 1: exists y.love(pat, y)
print("\n" + "=" * 80)
print("CASE 1: Target output = exists y.love(pat, y)")
print("=" * 80)

e1 = read_expr('\\x.exists y.love(x, y)')
e2 = read_expr('pat')
e3 = nltk.sem.ApplicationExpression(e1, e2)

print(f"e1 = {e1}")
print(f"e2 = {e2}")
print(f"e3 = ApplicationExpression(e1, e2) = {e3}")
print(f"e3.simplify() = {e3.simplify()}\n")



# Case 2: exists y.(love(pat,y) | love(y,pat))
print("\n" + "=" * 80)
print("CASE 2: Target output = exists y.(love(pat,y) | love(y,pat))")
print("=" * 80)

e1 = read_expr('\\x.exists y.(love(x,y) | love(y,x))')
e2 = read_expr('pat')
e3 = nltk.sem.ApplicationExpression(e1, e2)

print(f"e1 = {e1}")
print(f"e2 = {e2}")
print(f"e3 = ApplicationExpression(e1, e2) = {e3}")
print(f"e3.simplify() = {e3.simplify()}\n")



# Case 3: walk(pat)
print("\n" + "=" * 80)
print("CASE 3: Target output = walk(pat)")
print("=" * 80)

e1 = read_expr('\\x.walk(x)')
e2 = read_expr('pat')
e3 = nltk.sem.ApplicationExpression(e1, e2)

print(f"e1 = {e1}")
print(f"e2 = {e2}")
print(f"e3 = ApplicationExpression(e1, e2) = {e3}")
print(f"e3.simplify() = {e3.simplify()}")

"""### Exercise 6

As in the preceding exercise, find a $\lambda$-abstract `e1` that yields results equivalent to those shown below.

    e2 = read_expr('chase')
    e3 = nltk.sem.ApplicationExpression(e1, e2)
    print(e3.simplify())
        \x.all y.(dog(y) -> chase(x,pat))

    e2 = read_expr('chase')
    e3 = nltk.sem.ApplicationExpression(e1, e2)
    print(e3.simplify())
        \x.exists y.(dog(y) & chase(pat,x))

    e2 = read_expr('give')
    e3 = nltk.sem.ApplicationExpression(e1, e2)
    print(e3.simplify())
        \x0 x1.exists y.(present(y) & give(x1,y,x0))
"""

read_expr = nltk.sem.Expression.fromstring

# Case 1: \x.all y.(dog(y) -> chase(x,pat))
print("\n" + "=" * 80)
print("CASE 1: Target output = \\x.all y.(dog(y) -> chase(x,pat))")
print("=" * 80)

e1 = read_expr('\\P.\\x.all y.(dog(y) -> P(x,pat))')
e2 = read_expr('chase')
e3 = nltk.sem.ApplicationExpression(e1, e2)

print(f"e1 = {e1}")
print(f"e2 = {e2}")
print(f"e3 = ApplicationExpression(e1, e2) = {e3}")
print(f"e3.simplify() = {e3.simplify()}\n")



# Case 2: \x.exists y.(dog(y) & chase(pat,x))
print("\n" + "=" * 80)
print("CASE 2: Target output = \\x.exists y.(dog(y) & chase(pat,x))")
print("=" * 80)

e1 = read_expr('\\P.\\x.exists y.(dog(y) & P(pat,x))')
e2 = read_expr('chase')
e3 = nltk.sem.ApplicationExpression(e1, e2)

print(f"e1 = {e1}")
print(f"e2 = {e2}")
print(f"e3 = ApplicationExpression(e1, e2) = {e3}")
print(f"e3.simplify() = {e3.simplify()}\n")




# Case 3: \x0 x1.exists y.(present(y) & give(x1,y,x0))
print("\n" + "=" * 80)
print("CASE 3: Target output = \\x0 x1.exists y.(present(y) & give(x1,y,x0))")
print("=" * 80)

e1 = read_expr('\\P.\\x0 x1.exists y.(present(y) & P(x1,y,x0))')
e2 = read_expr('give')
e3 = nltk.sem.ApplicationExpression(e1, e2)

print(f"e1 = {e1}")
print(f"e2 = {e2}")
print(f"e3 = ApplicationExpression(e1, e2) = {e3}")
print(f"e3.simplify() = {e3.simplify()}")

"""### Exercise 7

As in the preceding exercise, find a $\lambda$-abstract `e1` that yields results equivalent to those shown below.

    e2 = read_expr('bark')
    e3 = nltk.sem.ApplicationExpression(e1, e2)
    print(e3.simplify())
        exists y.(dog(x) & bark(x))

    e2 = read_expr('bark')
    e3 = nltk.sem.ApplicationExpression(e1, e2)
    print(e3.simplify())
        bark(fido)

    e2 = read_expr('\\P. all x. (dog(x) -> P(x))')
    e3 = nltk.sem.ApplicationExpression(e1, e2)
    print(e3.simplify())
        all x.(dog(x) -> bark(x))
"""

read_expr = nltk.sem.Expression.fromstring

# Case 1: exists x.(dog(x) & bark(x))
print("\n" + "=" * 80)
print("CASE 1: Target output = exists x.(dog(x) & bark(x))")
print("=" * 80)
print("Note: Exercise shows 'exists y.(dog(x) & bark(x))' - likely a typo")
print("Interpreting as 'exists x.(dog(x) & bark(x))' for consistency")

e1 = read_expr('\\P.exists x.(dog(x) & P(x))')
e2 = read_expr('bark')
e3 = nltk.sem.ApplicationExpression(e1, e2)

print(f"\ne1 = {e1}")
print(f"e2 = {e2}")
print(f"e3 = ApplicationExpression(e1, e2) = {e3}")
print(f"e3.simplify() = {e3.simplify()}\n")



# Case 2: bark(fido)
print("\n" + "=" * 80)
print("CASE 2: Target output = bark(fido)")
print("=" * 80)

e1 = read_expr('\\P.P(fido)')
e2 = read_expr('bark')
e3 = nltk.sem.ApplicationExpression(e1, e2)

print(f"e1 = {e1}")
print(f"e2 = {e2}")
print(f"e3 = ApplicationExpression(e1, e2) = {e3}")
print(f"e3.simplify() = {e3.simplify()}\n")



# Case 3: all x.(dog(x) -> bark(x))
print("\n" + "=" * 80)
print("CASE 3: Target output = all x.(dog(x) -> bark(x))")
print("=" * 80)

e1 = read_expr('\\Q.Q(bark)')
e2 = read_expr('\\P.all x.(dog(x) -> P(x))')
e3 = nltk.sem.ApplicationExpression(e1, e2)

print(f"e1 = {e1}")
print(f"e2 = {e2}")
print(f"e3 = ApplicationExpression(e1, e2) = {e3}")
print(f"e3.simplify() = {e3.simplify()}")