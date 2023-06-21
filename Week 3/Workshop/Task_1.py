import nltk

from nltk.corpus import reuters
words = reuters.words()[:1000]

unigram_model = {}
total_words = len(words)

for word in words:
    if word in unigram_model:
        unigram_model[word] += 1
    else:
        unigram_model[word] = 1

# print(f"count of words: {unigram_model}")
# print(f"total number words: {total_words}")

for word in unigram_model:
    unigram_model[word] /= total_words

print(unigram_model)

import random


for i in range(10):
  print("###################################")
  print("NEWLY GENERATED SENTENCE")

  generated_sequence = []
  for i in range(20):
      # Randomly choose a word from the available words
      random_word = random.choice(list(unigram_model.keys()))
      generated_sequence.append(random_word)

  generated_sentence = ' '.join(generated_sequence)
  print(generated_sentence)
