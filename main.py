import nltk
import codecs
from nltk import *
from Lexical import LexiqueClass

verbs = {
    "suspects" : "is-suspect",
    "dans" : "at-loc",
    "victime" : "victim"
    }

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
tokens2 = "La victime a été retrouvé dans le salon à 21 heures."
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
tokens11 = "La victime n'a pas d’alcool dans son sang."
tokens12 = "Claude est le propriétaire du couteau de cuisine, mais il l'a prêté à John."
#Texte complet de MAD
#tokens3 = enonce.split()

parser = parse.FeatureEarleyChartParser(grammar)

# =====================================================================
# Phrase 1 : "Les suspects sont Claude, Jeannette, Ivan, Karl et John."
print("")
print("=====================================================================")
print("Phrase 1 : Les suspects sont Claude, Jeannette, Ivan, Karl et John.")
cleanedWords=[]
facts=[]
splittedText = nltk.word_tokenize(tokens1)
trees = parser.parse(splittedText)

# Construct tree
for tree in trees:
    # uncomment to see the trees
    # nltk.draw.tree.draw_trees(tree)
    rawWords = str(tree.label()['SEM']).split(',')

# Debug
print(rawWords)

# Clean up
for word in rawWords:
     cleanWord = word.replace("(","").replace(")","").strip()
     cleanedWords.append(cleanWord)

# Construct facts
for word in cleanedWords:
    if word not in verbs:
        print("({verb} {word})".format(verb=verbs[cleanedWords[0]], word=word))


# =====================================================================
# Phrase 2 : La victime a été retrouvé dans le salon à 21 heures
print("")
print("=====================================================================")
print("Phrase 2 : La victime a été retrouvé dans le salon à 21 heures")
cleanedWords=[]
facts=[]
splittedText = nltk.word_tokenize(tokens2)
trees = parser.parse(splittedText)

# Construct tree
for tree in trees:
    # uncomment to see the trees
    # nltk.draw.tree.draw_trees(tree)
    rawWords = str(tree.label()['SEM']).split(',')

# Debug
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

    if cleanedWords[i].lower() == "victime":
        fact = "victim"
    elif cleanedWords[i].lower() == "heures":
        fact += " at " + cleanedWords[i-1]
    elif cleanedWords[i].lower() == "dans":
        fact += " at-loc " + cleanedWords[i+1]
        
print("({fact})".format(fact=fact))

# =====================================================================
# Phrase 3 : Le corps est chaud.
print("")
print("=====================================================================")
print("Phrase 3 : Le corps est chaud.")
cleanedWords=[]
facts=[]
splittedText = nltk.word_tokenize(tokens3)
trees = parser.parse(splittedText)

# Construct tree
for tree in trees:
    # uncomment to see the trees
    # nltk.draw.tree.draw_trees(tree)
    rawWords = str(tree.label()['SEM']).split(',')

# Debug
print(rawWords)

# Clean up
for word in rawWords:
     cleanWord = word.replace("(","").replace(")","").strip()
     cleanedWords.append(cleanWord)

fact=""
for word in cleanedWords:
    fact+=word + " "
    
print("(is {fact})".format(fact=fact))
