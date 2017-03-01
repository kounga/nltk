import codecs
import nltk

class Lexique(object):

    __dictionnaire = None

    def __init__(self):
        self.dictionnaire = self.generer_dictionnaire("Lexical/banque_mots.txt")


    def generer_dictionnaire(self,text):
        with codecs.open(text, 'r', encoding='utf8') as f:
            rawText = f.read()
            return nltk.word_tokenize(rawText)


    def est_valide_lexicalement(self, text_avalider_lexicalement):
        text_valide = True
        a_verifier = nltk.word_tokenize(text_avalider_lexicalement)
        motsValid = True

        for mots in a_verifier:
            motsValid = False

            for motsLexi in self.dictionnaire:
                if (mots.lower() == motsLexi.lower()):
                    motsValid = True

            if (motsValid != True):
                print("Le mot «", mots, "» ne fait pas partie de notre lexique.")
                text_valide = False

        return text_valide
    def toString(self):
        print("test")