# -*- coding: utf-8 -*-

import nltk
import codecs
from nltk.corpus import stopwords
from nltk import *

with codecs.open("exemple_et_code.cfg", 'r', encoding='utf8') as f:
    grammaireText=f.read()
with codecs.open("MonProgramSimple.cfg", 'r', encoding='utf8') as f:
    grammaireText2=f.read()

grammar = grammar.FeatureGrammar.fromstring(grammaireText2)
parser = nltk.ChartParser(grammar)
tokens0 = "Les et Les"
tokens = "Le Jean tua Marie."
tokens1 = "Les suspects sont Claude, Jeannette, Ivan, Karl et John."
tokens2 = "La victime a été retrouvé dans le salon à 21 heures."
tokens3 = "Les suspects sont: Claude, Jeannette, Ivan, Karl et John. La victime a été retrouvé dans le salon à 21 heure.. Le corp est encore chaud. Claude a quitté le salon vers 19 heure. Il mangeait un sac de chips. C’est Karl qui a trouvé le corp à 23 heure. Les objets trouvés sur la scène du crime sont: un couteau de cuisine, un sac de chips et un verre d’alcool vide. Le couteau est taché de sang. Jeannette Ivan et Karl n’ont pas bu. Claude et jeannette ont vu un homme dans le salon en compagnie de la victime vers 21 heure. La victime n’a pas d’alcool dans son sang. Claude est le propriétaire du couteau, mais il l’a prêté à John.".split()
splittedText = nltk.word_tokenize(tokens1)

parser = parse.FeatureEarleyChartParser(grammar)
trees = parser.parse(splittedText)
for tree in trees:
    nltk.draw.tree.draw_trees(tree)
    print(tree.label()['SEM'])
