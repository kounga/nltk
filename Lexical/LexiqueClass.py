import codecs
import nltk

class Lexique(object):

    __dictionnaire = None

    def __init__(self):
        self.dictionnaire = self.generer_dictionnaire("Lexical/original.txt")


    def generer_dictionnaire(self,text):
        with codecs.open(text, 'r', encoding='utf8') as f:
            rawText = f.read()
            return nltk.word_tokenize(rawText)


    def valide_lexicalement(self,textAvaliderLexicalement):
        Averifier = nltk.word_tokenize(textAvaliderLexicalement)
        motsValid = True

        for mots in Averifier:
            motsValid = False

            for motsLexi in self.dictionnaire:
                if (mots.lower() == motsLexi.lower()):
                    motsValid = True

            if (motsValid != True):
                print("Le mot «", mots, "» ne fait pas partie de notre lexique.")

    def toString(self):
        print("test")