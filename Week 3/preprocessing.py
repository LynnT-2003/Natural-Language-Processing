import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

text = "Hello Mr.Bond. We've got a mission for you. Here're the details."
sentences = sent_tokenize(text)

print("WORDS:")
for sentence in sentences:
    words = word_tokenize(sentence)
    print(words)

all_words = word_tokenize(text)

print("BIGRAMS:")
bigrams = list(nltk.bigrams(all_words))
print(bigrams)

print("TRIGRAMS;")
trigrams = list(nltk.trigrams(all_words))
print(trigrams)

print("TAGS")
tags = nltk.pos_tag(all_words)
print(tags)

print("_________________________________________________________")

from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet

word_list = ['play', 'playing', 'played', 'is', 'am', 'be', 'are', 'were', 'mouse', 'mice']

print("Lemmatization")
lemmatizer = WordNetLemmatizer()
lemma_verbs = [lemmatizer.lemmatize(word, wordnet.VERB) for word in word_list]
print(lemma_verbs)
lemma_nouns = [lemmatizer.lemmatize(word, wordnet.NOUN) for word in word_list]
print(lemma_nouns)
