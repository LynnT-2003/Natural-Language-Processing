import re

sentence = "I have so much fun. Yahoo! lnyinyi22@gmail.com #computerscience https://oshinokoo.com/manga/oshi-no-ko-chapter-71/"

def preproccsss_sentence(sentence):
    sentence = re.sub(r"http\S+|www\S+|https\S+", "", sentence)
    sentence = re.sub(r"\S+@\S+", "", sentence)
    sentence = re.sub(r"#\w+", "", sentence)
    sentence = re.sub(r"[.!]", "", sentence)
    words = sentence.split()
    return words

words = preproccsss_sentence(sentence)

print(words)