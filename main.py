﻿import nltk
import codecs
from nltk import *
from Lexical import LexiqueClass

prepToVerbs = {
    "suspects": "is-suspect",
    "dans": "at-loc",
    "victime": "victim",
    "trouvé": "has-found",
    "objects": "object",
    "sur": "at-loc",
    "pas": "has-not"
}

quitteFrancais = "quitté"
salonFrancais = "salon"
alcoolFrancais = "alcool"
heuresFrancais = "heures"
pronomFrancais = "Il"
claudeFrancais = "Claude"
sangFrancais = "sang"
victimeFrancais = "victime"

enableDebug = True
allFacts = []

with codecs.open("grammaire.cfg", 'r', encoding='utf8') as f:
    grammaireText2 = f.read()

# Lecture de l'énoncé dans le fichier txt
with codecs.open("histoire.txt", 'r', encoding='utf8') as f:
    histoire = f.read()

phrases_de_histoire = nltk.sent_tokenize(histoire, 'french')

i = 0
for phrase in phrases_de_histoire:
    i += 1
    print(i, ")", phrase)

grammar = grammar.FeatureGrammar.fromstring(grammaireText2)
parser = nltk.ChartParser(grammar)

print("")
print("=====================================================================")
i = 0
for phrase_a_valider in phrases_de_histoire:
    try:
        splittedText = nltk.word_tokenize(phrase_a_valider)
        trees = parser.parse(splittedText)
    except:
        print("« ", phrase_a_valider, " » n'est pas syntaxiquement correct")
    i += 1

trees = None
splittedText = None

lexi = LexiqueClass.Lexique()
lexi.est_valide_lexicalement(histoire)

parser = parse.FeatureEarleyChartParser(grammar)

# =====================================================================
print("")
print("=====================================================================")
print("Phrase 1 : {phrase}".format(phrase=phrases_de_histoire[0]))
cleanedWords = []
facts = []
splittedText = nltk.word_tokenize(phrases_de_histoire[0])
trees = parser.parse(splittedText)

# Construct tree
for tree in trees:
    # uncomment to see the trees
    # nltk.draw.tree.draw_trees(tree)
    rawWords = str(tree.label()['SEM']).split(',')

try:
    if rawWords is None:
        print("rawWords is None!")
except NameError:
    print("Could not build tree using the grammar.")
else:
    # Debug
    if enableDebug:
        print(rawWords)

    # Clean up
    for word in rawWords:
        cleanWord = word.replace("(", "").replace(")", "").strip()
        cleanedWords.append(cleanWord)

    # Construct facts
    for word in cleanedWords:
        if word not in prepToVerbs:
            allFacts.append("({verb} {word})".format(verb=prepToVerbs[cleanedWords[0]], word=word))
            if enableDebug:
                print("({verb} {word})".format(verb=prepToVerbs[cleanedWords[0]], word=word))

# =====================================================================
print("")
print("=====================================================================")
print("Phrase 2 : {phrase}".format(phrase=phrases_de_histoire[1]))
cleanedWords = []
facts = []
splittedText = nltk.word_tokenize(phrases_de_histoire[1])
trees = parser.parse(splittedText)

# Construct tree
for tree in trees:
    # uncomment to see the trees
    # nltk.draw.tree.draw_trees(tree)
    rawWords = str(tree.label()['SEM']).split(',')

try:
    if rawWords is None:
        print("rawWords is None!")
except NameError:
    print("Could not build tree using the grammar.")
else:
    # Debug
    if enableDebug:
        print(rawWords)

    # Clean up
    for word in rawWords:
        cleanWord = word.replace("(", "").replace(")", "").strip()
        cleanedWords.append(cleanWord)

    nbItems = 0
    for i in cleanedWords:
        nbItems += 1

    # Construct facts
    fact = ""
    for i in range(0, nbItems):
        if cleanedWords[i].lower() == "corps":
            fact = cleanedWords[i].lower()
        elif cleanedWords[i].lower() == heuresFrancais:
            fact += " at " + cleanedWords[i - 1]
        elif cleanedWords[i].lower() == "dans":
            fact += " at-loc " + cleanedWords[i + 1]

    if enableDebug:
        print("({fact})".format(fact=fact))
    allFacts.append("({fact})".format(fact=fact))

# =====================================================================
print("")
print("=====================================================================")
print("Phrase 3 : {phrase}".format(phrase=phrases_de_histoire[2]))
cleanedWords = []
facts = []
splittedText = nltk.word_tokenize(phrases_de_histoire[2])
trees = parser.parse(splittedText)

# Construct tree
for tree in trees:
    # uncomment to see the trees
    # nltk.draw.tree.draw_trees(tree)
    rawWords = str(tree.label()['SEM']).split(',')

try:
    if rawWords is None:
        print("rawWords is None!")
except NameError:
    print("Could not build tree using the grammar.")
else:
    # Debug
    if enableDebug:
        print(rawWords)

    # Clean up
    for word in rawWords:
        cleanWord = word.replace("(", "").replace(")", "").strip()
        cleanedWords.append(cleanWord)

    fact = ""
    for word in cleanedWords:
        fact += word + " "

    if enableDebug:
        print("(description {fact})".format(fact=fact))
    allFacts.append("(description {fact})".format(fact=fact))

# =====================================================================
print("")
print("=====================================================================")
print("Phrase 4 : ", phrases_de_histoire[3])
cleanedWords = []
facts = []
splittedText = nltk.word_tokenize(phrases_de_histoire[3])
trees = parser.parse(splittedText)

for tree in trees:
    # uncomment to see the trees
    # nltk.draw.tree.draw_trees(tree)
    rawWords = str(tree.label()['SEM']).split(',')

try:
    if rawWords is None:
        print("rawWords is None!")
except NameError:
    print("Could not build tree using the grammar.")
else:
    # Debug
    if enableDebug:
        print(rawWords)

    i = 0
    for element in rawWords:
        rawWords[i] = element.replace("(", "").replace(")", "").replace(" ", "")
        i += 1

    fact = "("
    i = 0
    for word in rawWords:
        if word == claudeFrancais:
            fact += word
        elif word == quitteFrancais:
            fact += " exit "
        elif word == salonFrancais:
            fact += word
        elif word == heuresFrancais:
            fact += " at " + rawWords[i - 1]
        i += 1;
    fact += ")"

    if enableDebug:
        print(fact)

    allFacts.append(fact)

# =====================================================================
print("")
print("=====================================================================")
print("Phrase 5 : ", phrases_de_histoire[4])
cleanedWords = []
facts = []
splittedText = nltk.word_tokenize(phrases_de_histoire[4])
trees = parser.parse(splittedText)

for tree in trees:
    # uncomment to see the trees
    # nltk.draw.tree.draw_trees(tree)
    rawWords = str(tree.label()['SEM']).split(',')

try:
    if rawWords is None:
        print("rawWords is None!")
except NameError:
    print("Could not build tree using the grammar.")
else:
    # Debug
    if enableDebug:
        print(rawWords)

    i = 0
    for element in rawWords:
        rawWords[i] = element.replace("(", "").replace(")", "").replace(" ", "")
        i += 1

    fact = "("
    i = 0
    for word in rawWords:

        if word == pronomFrancais:
            fact += claudeFrancais
        elif word == "mangeait":
            fact += " ate "
        elif word == "sacdechips":
            fact += word
        i += 1;

    fact += ")"

    if enableDebug:
        print(fact)

    allFacts.append(fact)

# =====================================================================
print("")
print("=====================================================================")
print("Phrase 6 : {phrase}".format(phrase=phrases_de_histoire[5]))
cleanedWords = []
facts = []
splittedText = nltk.word_tokenize(phrases_de_histoire[5])
trees = parser.parse(splittedText)

# Construct tree
for tree in trees:
    # uncomment to see the trees
    # nltk.draw.tree.draw_trees(tree)
    rawWords = str(tree.label()['SEM']).split(',')

try:
    if rawWords is None:
        print("rawWords is None!")
except NameError:
    print("Could not build tree using the grammar.")
else:
    # Debug
    if enableDebug:
        print(rawWords)

    # Clean up
    for word in rawWords:
        cleanWord = word.replace("(", "").replace(")", "").strip()
        cleanedWords.append(cleanWord)

        nbItems = 0
    for i in cleanedWords:
        nbItems += 1

    # Construct facts
    fact = ""
    for i in range(0, nbItems):
        if cleanedWords[i].lower() == "trouvé":
            fact = prepToVerbs[cleanedWords[i]] + " " + cleanedWords[i - 1]
        elif cleanedWords[i].lower() == "heures":
            fact += " at " + cleanedWords[i - 1]
        elif not cleanedWords[i].isdigit():
            fact += " " + cleanedWords[i]

    if enableDebug:
        print("({fact})".format(fact=fact))
    allFacts.append("({fact})".format(fact=fact))

# =====================================================================
print("")
print("=====================================================================")
print("Phrase 7 : {phrase}".format(phrase=phrases_de_histoire[6]))
cleanedWords = []
facts = []
splittedText = nltk.word_tokenize(phrases_de_histoire[6])
trees = parser.parse(splittedText)

# Construct tree
for tree in trees:
    # uncomment to see the trees
    # nltk.draw.tree.draw_trees(tree)
    rawWords = str(tree.label()['SEM']).split(',')

try:
    if rawWords is None:
        print("rawWords is None!")
except NameError:
    print("Could not build tree using the grammar.")
else:
    # Debug
    if enableDebug:
        print(rawWords)

    # Clean up
    for word in rawWords:
        cleanWord = word.replace("(", "").replace(")", "").strip()
        cleanedWords.append(cleanWord)

        nbItems = 0
    for i in cleanedWords:
        nbItems += 1

    # Construct facts
    fact = ""
    curCount = 0
    for i in range(0, nbItems - 1):
        if cleanedWords[i] in prepToVerbs:
            if prepToVerbs[cleanedWords[i]] == "at-loc":
                fact += prepToVerbs[cleanedWords[i]] + " " + cleanedWords[i + 1]
            else:
                fact += prepToVerbs[cleanedWords[i]] + " "
            curCount += 1

    curCount += 1
    for i in range(curCount, nbItems - 1):
        if cleanedWords[i] not in prepToVerbs:
            if enableDebug:
                print("({partial_fact} {obj} {desc})".format(partial_fact=fact, obj=cleanedWords[i], desc=""))
            allFacts.append("({partial_fact} {obj} {desc})".format(partial_fact=fact, obj=cleanedWords[i], desc=""))

# =====================================================================
print("")
print("=====================================================================")
print("Phrase 8 : {phrase}".format(phrase=phrases_de_histoire[7]))
cleanedWords = []
facts = []
splittedText = nltk.word_tokenize(phrases_de_histoire[7])
trees = parser.parse(splittedText)

# Construct tree
for tree in trees:
    # uncomment to see the trees
    # nltk.draw.tree.draw_trees(tree)
    rawWords = str(tree.label()['SEM']).split(',')

try:
    if rawWords is None:
        print("rawWords is None!")
except NameError:
    print("Could not build tree using the grammar.")
else:
    # Debug
    if enableDebug:
        print(rawWords)

    # Clean up
    for word in rawWords:
        cleanWord = word.replace("(", "").replace(")", "").strip()
        cleanedWords.append(cleanWord)

        nbItems = 0
    for i in cleanedWords:
        nbItems += 1

    # Construct facts
    fact = ""
    curCount = 0

    fact = ""
    for word in cleanedWords:
        fact += word + " "

    if enableDebug:
        print("(description {fact})".format(fact=fact))
    allFacts.append("(description {fact})".format(fact=fact))

# =====================================================================
print("")
print("=====================================================================")
print("Phrase 9 : {phrase}".format(phrase=phrases_de_histoire[8]))
cleanedWords = []
facts = []
splittedText = nltk.word_tokenize(phrases_de_histoire[8])
trees = parser.parse(splittedText)

# Construct tree
for tree in trees:
    # uncomment to see the trees
    # nltk.draw.tree.draw_trees(tree)
    rawWords = str(tree.label()['SEM']).split(',')

try:
    if rawWords is None:
        print("rawWords is None!")
except NameError:
    print("Could not build tree using the grammar.")
else:
    # Debug
    if enableDebug:
        print(rawWords)

    # Clean up
    for word in rawWords:
        cleanWord = word.replace("(", "").replace(")", "").strip()
        cleanedWords.append(cleanWord)

    nbItems = 0
    for i in cleanedWords:
        nbItems += 1

    # Construct facts
    fact = ""
    curCount = 0
    for i in range(nbItems - 1, 0, -1):
        if cleanedWords[i] in prepToVerbs:
            fact = prepToVerbs[cleanedWords[i]] + " " + cleanedWords[i + 1]
            curCount += 1
        elif cleanedWords[i] == "bu":
            curCount += 1

    for i in range(nbItems - 1 - curCount, -1, -1):
        if enableDebug:
            print("({partial_fact} {person}".format(partial_fact=fact, person=cleanedWords[i]))
        allFacts.append("({partial_fact} {person}".format(partial_fact=fact, person=cleanedWords[i]))

print("")
print("=====================================================================")
print("Phrase 10 : ", phrases_de_histoire[9])
cleanedWords = []
facts = []
splittedText = nltk.word_tokenize(phrases_de_histoire[9])
trees = parser.parse(splittedText)

for tree in trees:
    # uncomment to see the trees
    # nltk.draw.tree.draw_trees(tree)
    rawWords = str(tree.label()['SEM']).split(',')

try:
    if rawWords is None:
        print("rawWords is None!")
except NameError:
    print("Could not build tree using the grammar.")
else:
    # Debug
    if enableDebug:
        print(rawWords)

    i = 0
    for element in rawWords:
        rawWords[i] = element.replace("(", "").replace(")", "").replace(" ", "")
        i += 1

    fact = "( etat  " + victimeFrancais + " "
    i = 0
    for word in rawWords:
        if word == sangFrancais:
            fact += word
        elif word == alcoolFrancais and rawWords[i - 1] == "pas":
            fact += "( not " + word + " "
        i += 1;
    fact += "))"

    if enableDebug:
        print(fact)

    allFacts.append(fact)

print("")
print("=====================================================================")
print("Phrase 11 : {phrase}".format(phrase=phrases_de_histoire[10]))
cleanedWords = []
facts = []
splittedText = nltk.word_tokenize(phrases_de_histoire[10])
trees = parser.parse(splittedText)

# Construct tree
for tree in trees:
    # uncomment to see the trees
    # nltk.draw.tree.draw_trees(tree)
    rawWords = str(tree.label()['SEM']).split(',')

try:
    if rawWords is None:
        print("rawWords is None!")
except NameError:
    print("Could not build tree using the grammar.")
else:
    # Debug
    if enableDebug:
        print(rawWords)

    # Clean up
    for word in rawWords:
        cleanWord = word.replace("(", "").replace(")", "").strip()
        cleanedWords.append(cleanWord)

    proprietaire = ""
    locateur = "John"
    quoi = ""
    fact = ""

    nbItems = 0
    for i in cleanedWords:
        nbItems += 1

    for i in range(0, nbItems - 1):
        if cleanedWords[i] != "mais":
            if cleanedWords[i] == "couteau de cuisine":
                quoi = cleanedWords[i]
            elif cleanedWords[i] == "Claude":
                proprietaire = cleanedWords[i]

    fact = "({action} {what} {who})".format(what=quoi, action=cleanedWords[i], who=proprietaire)
    allFacts.append(fact)
    fact = "({action} {what} {who})".format(what=quoi, action="en-possession", who=locateur)
    allFacts.append(fact)
    print(fact)

fichierFact = codecs.open("facts.txt", "w", "utf-8")
# Creation du fichier Facts.txt avec les faits Jess
for fact in allFacts:
    fact += "\n"
    fichierFact.writelines(fact)
fichierFact.close()
