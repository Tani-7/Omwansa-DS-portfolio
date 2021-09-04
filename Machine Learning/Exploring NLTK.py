import nltk
from nltk.tokenize import word_tokenize
from nltk.help import upenn_tagset
import spacy
nlp = spacy.load('en_core_web_sm')

sent = '''I am reading a book.
            It is Python Machine Learning by Example,
            Third Edition.'''
            
sent1 = '''The book written by Hayden Liu in 2018 was sold
at $30 in America'''

tokens2 = nlp(sent)
#print([token.text for token in tokens2])

#tokens = word_tokenize(sent)
#print(nltk.pos_tag(tokens))


#nltk.help.upenn_tagset('PRP')
#nltk.help.upenn_tagset('VBP')

#print([(token.text, token.pos_) for token in tokens2])
tokens3 = nlp(sent1)
print([(token_ent.text, token_ent.label)for token_ent in tokens3.ents])
