import nltk
import codecs
from nltk import *
from Lexical import LexiqueClass

verbs = {
    "suspects" : "is-suspect",
    "dans" : "at-loc",
    "victime" : "victim",
    "trouvé" : "has-found",
    "objects" : "object",
    "sur" : "at-loc",
    "pas" : "has-not"
    }

enableDebug=True
allFacts=[]

with codecs.open("grammaire.cfg", 'r', encoding='utf8') as f:
    grammaireText2=f.read()

#Lecture de l'énoncé dans le fichier txt
with codecs.open("enonce.txt", 'r', encoding='utf8') as f:
    enonce = f.read()

# Instance de la classe Lexique
lexi = LexiqueClass.Lexique()
lexi.est_valide_lexicalement(enonce)

grammar = grammar.FeatureGrammar.fromstring(grammaireText2)
parser = nltk.ChartParser(grammar)

tokens0 = "Les et Les"
tokens = "Le Jean tua Marie."
tokens1 = "Les suspects sont Claude, Jeannette, Ivan, Karl et John."
tokens2 = "Le cadavre a été retrouvée dans le salon à 21 heures."
tokens3 = "Le corps est chaud."
tokens4 = "Claude a quitté le salon vers 19 heures."
tokens5 = "Il mangeait un sac de chips."
tokens6 = "C'est Karl qui a trouvé le corps à 23 heures."
tokens7 = "Les objets trouvés sur la scène du crime sont un couteau de cuisine, un sac de chips et un verre d'alcool vide."
#tokens8 = "Le couteau est taché de sang."
#tokens8 = "Le couteau de cuisine est ensanglanté"
tokens8 = "Le couteau de cuisine est ensanglanté."
tokens9 = "Jeannette, Ivan et Karl n'ont pas bu."
#tokens10 = "Claude et jeannette ont vu un homme dans le salon en compagnie de la victime vers 21 heure."
tokens11 = "La victime n'a pas d'alcool dans son sang."
tokens12 = "Le couteau de cuisine appartient à Claude, mais il l'a prêté à John."
#Texte complet de MAD
#tokens3 = enonce.split()

parser = parse.FeatureEarleyChartParser(grammar)

# =====================================================================
# Phrase 1 : "Les suspects sont Claude, Jeannette, Ivan, Karl et John."
print("")
print("=====================================================================")
print("Phrase 1 : {phrase}".format(phrase=tokens1))
cleanedWords=[]
facts=[]
splittedText = nltk.word_tokenize(tokens12)
trees = parser.parse(splittedText)

# Construct tree
for tree in trees:
    # uncomment to see the trees
    nltk.draw.tree.draw_trees(tree)
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
         cleanWord = word.replace("(","").replace(")","").strip()
         cleanedWords.append(cleanWord)

    # Construct facts
    for word in cleanedWords:
        if word not in verbs:
            allFacts.append("({verb} {word})".format(verb=verbs[cleanedWords[0]], word=word))
            if enableDebug:
                print("({verb} {word})".format(verb=verbs[cleanedWords[0]], word=word))


# =====================================================================
# Phrase 2 : La victime a été retrouvé dans le salon à 21 heures
print("")
print("=====================================================================")
print("Phrase 2 : {phrase}".format(phrase=tokens2))
cleanedWords=[]
facts=[]
splittedText = nltk.word_tokenize(tokens2)
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
         cleanWord = word.replace("(","").replace(")","").strip()
         cleanedWords.append(cleanWord)

    nbItems = 0
    for i in cleanedWords:
        nbItems+=1

    # Construct facts
    fact=""
    for i in range(0, nbItems):
        if cleanedWords[i].lower() == "corps":
            fact = "corps"
        elif cleanedWords[i].lower() == "heures":
            fact += " at " + cleanedWords[i-1]
        elif cleanedWords[i].lower() == "dans":
            fact += " at-loc " + cleanedWords[i+1]

    if enableDebug:
        print("({fact})".format(fact=fact))
    allFacts.append("({fact})".format(fact=fact))

# =====================================================================
# Phrase 3 : Le corps est chaud.
print("")
print("=====================================================================")
print("Phrase 3 : {phrase}".format(phrase=tokens3))
cleanedWords=[]
facts=[]
splittedText = nltk.word_tokenize(tokens3)
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
         cleanWord = word.replace("(","").replace(")","").strip()
         cleanedWords.append(cleanWord)

    fact=""
    for word in cleanedWords:
        fact+=word + " "

    if enableDebug:
        print("(description {fact})".format(fact=fact))
    allFacts.append("(description {fact})".format(fact=fact))

# =====================================================================
# Phrase 4 : Claude a quitté le salon vers 19 heures.
print("")
print("=====================================================================")
print("Phrase 4 : Claude a quitté le salon vers 19 heures.")
cleanedWords=[]
facts=[]
splittedText = nltk.word_tokenize(tokens4)
trees = parser.parse(splittedText)

for tree in trees:
    # uncomment to see the trees
    # nltk.draw.tree.draw_trees(tree)
    rawWords = str(tree.label()['SEM']).split(',')

# Debug
print(rawWords)


i=0
for element in rawWords:
    rawWords[i]=element.replace("(","").replace(")","").replace(" ","")
    i+=1

fact="( "
i=0
for word in rawWords:
    if word == "Claude":
        fact += "Claude"
    elif word == "quitté":
        fact += " exit "
    elif  word == "salon":
        fact += "salon"
    elif  word == "heures":
        fact += " at " + rawWords[i-1]
    i+=1;
fact+=" )"
print(fact)


# =====================================================================
# Phrase 5 : Il mangeait un sac de chips.
print("")
print("=====================================================================")
print("Phrase 5 : Il mangeait un sac de chips.")
cleanedWords=[]
facts=[]
splittedText = nltk.word_tokenize(tokens5)
trees = parser.parse(splittedText)

for tree in trees:
    # uncomment to see the trees
    # nltk.draw.tree.draw_trees(tree)
    rawWords = str(tree.label()['SEM']).split(',')

# Debug
print(rawWords)


i=0
for element in rawWords:
    rawWords[i]=element.replace("(","").replace(")","").replace(" ","")
    i+=1

fact="( "
i=0
for word in rawWords:

    if word == "Il":
        fact += "Claude"
    elif word == "mangeait":
        fact += " ate "
    elif  word == "sacdechips":
        fact += "chips at 19"

    i+=1;

fact+=" )"
print(fact)


# =====================================================================
# Phrase 6 : C'est Karl qui a trouvé le corps à 23 heures.
print("")
print("=====================================================================")
print("Phrase 6 : {phrase}".format(phrase=tokens6))
cleanedWords=[]
facts=[]
splittedText = nltk.word_tokenize(tokens6)
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
         cleanWord = word.replace("(","").replace(")","").strip()
         cleanedWords.append(cleanWord)

         nbItems = 0
    for i in cleanedWords:
        nbItems+=1

    # Construct facts
    fact=""
    for i in range(0, nbItems):
        if cleanedWords[i].lower() == "trouvé":
            fact = verbs[cleanedWords[i]] + " " + cleanedWords[i-1]
        elif cleanedWords[i].lower() == "heures":
            fact += " at " + cleanedWords[i-1]
        elif not cleanedWords[i].isdigit():
            fact += " " + cleanedWords[i]

    if enableDebug:
        print("({fact})".format(fact=fact))
    allFacts.append("({fact})".format(fact=fact))

# =====================================================================
# Phrase 7 : Les objets trouvés sur la scène du crime sont un couteau de cuisine, un sac de chips et un verre d'alcool vide.
print("")
print("=====================================================================")
print("Phrase 7 : {phrase}".format(phrase=tokens7))
cleanedWords=[]
facts=[]
splittedText = nltk.word_tokenize(tokens7)
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
         cleanWord = word.replace("(","").replace(")","").strip()
         cleanedWords.append(cleanWord)

         nbItems = 0
    for i in cleanedWords:
        nbItems+=1

    # Construct facts
    fact=""
    curCount = 0
    for i in range(0, nbItems - 1):
        if cleanedWords[i] in verbs:
            if verbs[cleanedWords[i]]=="at-loc":
                fact+=verbs[cleanedWords[i]] + " " + cleanedWords[i + 1]
            else:
                fact+=verbs[cleanedWords[i]] + " "
            curCount+=1

    curCount+=1
    for i in range(curCount, nbItems - 1):
        if cleanedWords[i] not in verbs:
            if enableDebug:
                print("({partial_fact} {obj} {desc})".format(partial_fact=fact, obj=cleanedWords[i], desc=""))
            allFacts.append("({partial_fact} {obj} {desc})".format(partial_fact=fact, obj=cleanedWords[i], desc=""))

# =====================================================================
# Phrase 8 : Le couteau de cuisine est ensanglanté.
print("")
print("=====================================================================")
print("Phrase 8 : {phrase}".format(phrase=tokens8))
cleanedWords=[]
facts=[]
splittedText = nltk.word_tokenize(tokens8)
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
         cleanWord = word.replace("(","").replace(")","").strip()
         cleanedWords.append(cleanWord)

         nbItems = 0
    for i in cleanedWords:
        nbItems+=1

    # Construct facts
    fact=""
    curCount = 0

    fact=""
    for word in cleanedWords:
        fact+=word + " "

    if enableDebug:
        print("(description {fact})".format(fact=fact))
    allFacts.append("(description {fact})".format(fact=fact))

# =====================================================================
# Phrase 9 : Jeannette, Ivan et Karl n'ont pas bu.
print("")
print("=====================================================================")
print("Phrase 9 : {phrase}".format(phrase=tokens9))
cleanedWords=[]
facts=[]
splittedText = nltk.word_tokenize(tokens9)
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
         cleanWord = word.replace("(","").replace(")","").strip()
         cleanedWords.append(cleanWord)


    nbItems = 0
    for i in cleanedWords:
        nbItems+=1

    # Construct facts
    fact=""
    curCount = 0
    for i in range(nbItems - 1, 0, -1):
        if cleanedWords[i] in verbs:
            fact=verbs[cleanedWords[i]] + " " + cleanedWords[i+1]
            curCount+=1
        elif cleanedWords[i] == "bu":
            curCount+=1

    for i in range(nbItems - 1 - curCount, -1, -1):
        if enableDebug:
            print("({partial_fact} {person}".format(partial_fact=fact, person=cleanedWords[i]))
        allFacts.append("({partial_fact} {person}".format(partial_fact=fact, person=cleanedWords[i]))

# =====================================================
# Print all facts
# =====================================================
print("")
print("=====================================================")
print("Facts : ")
for fact in allFacts:
    print(fact)
print("=====================================================")
