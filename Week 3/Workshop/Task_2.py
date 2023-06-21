import nltk

from nltk.corpus import reuters
words = reuters.words()[:1000]

bigram_model = {}
prev_word = None

for word in words:
    if prev_word is not None:
        bigram = (prev_word, word)
        if bigram in bigram_model:
            bigram_model[bigram] += 1
        else:
            bigram_model[bigram] = 1
    prev_word = word


# print(f"count of words: {bigram_model}")

for bigram in bigram_model:
    prev_word = bigram[0]
    # print(f"Bigram: {bigram_model[bigram]}")
    # print(f"Previous word count: {prev_word}")
    bigram_model[bigram] /= words.count(prev_word)


import random

for i in range(10):
  print("###################################")
  print("NEWLY GENERATED SENTENCE")
  generated_sequence = []
  current_word = random.choice(words)
  # Select 20 words randomly based on their probabilities
  for _ in range(20):
      generated_sequence.append(current_word)
      possible_next_words = []

      for word, next_word in bigram_model:
          if word == current_word:
              possible_next_words.append(next_word)

      if possible_next_words:
          current_word = random.choice(possible_next_words)
      else:
          current_word = random.choice(words)
  # Join the words to form a sentence
  generated_sentence = ' '.join(generated_sequence)

  print(generated_sentence)
