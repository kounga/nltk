import codecs
from Lexical import LexiqueClass


#Lecture de l'énoncé dans le fichier txt
with codecs.open("enonce.txt", 'r', encoding='utf8') as f:
    enonce = f.read()

#Instance de la classe Lexique
lexi = LexiqueClass.Lexique()

#Valide que chaque mots de l'énoncer fait partie de notre lexique
#(J'ai remplacé dans le text de MAD John par James_Bond pour demontrer l'erreur)
lexi.valide_lexicalement(enonce)






