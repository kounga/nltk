import nltk
import codecs
from nltk import *
from Lexical import LexiqueClass

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
#Texte complet de MAD
tokens3 = enonce.split()
splittedText = nltk.word_tokenize(tokens1)

parser = parse.FeatureEarleyChartParser(grammar)
trees = parser.parse(splittedText)
for tree in trees:
    nltk.draw.tree.draw_trees(tree)
    print(tree.label()['SEM'])
