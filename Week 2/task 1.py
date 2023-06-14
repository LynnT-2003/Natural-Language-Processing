# 6411271 - LYNN THIT NYI NYI

import re

sentence = "I have so much fun. Yahoo! u6411271@au.edu lNyinyi22@gmail.com #computerscience #IT https://oshinokoo.com/manga/oshi-no-ko-chapter-71/ https://oshinokoo.com/manga/oshi-no-ko-chapter-72/"

def preproccsss_sentence(sentence):
    sentence = re.sub(r"http\S+|www\S+|https\S+", "", sentence)
    sentence = re.sub(r"\S+@\S+", "", sentence)
    sentence = re.sub(r"#\w+", "", sentence)
    sentence = re.sub(r"[.!]", "", sentence)
    words = sentence.split()
    return words

words = preproccsss_sentence(sentence)
print(words)