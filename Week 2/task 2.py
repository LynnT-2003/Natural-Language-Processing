# 6411271 - LYNN THIT NYI NYI

import re

sentence = "I have so much fun. Yahoo! u6411271@au.edu lNyinyi22@gmail.com #computerscience #IT https://oshinokoo.com/manga/oshi-no-ko-chapter-71/ https://oshinokoo.com/manga/oshi-no-ko-chapter-72/"

def preproccsss_sentence(sentence):
    emails = []
    urls = []
    hashtags = []
    # extract URLS
    urls.extend(re.findall(r"http\S+|www\S+|https\S+", sentence))
    sentence = re.sub(r"http\S+|www\S+|https\S+", "", sentence)
    #extract email addresses from
    emails.extend(re.findall(r"\S+@\S+", sentence))
    sentence = re.sub(r"\S+@\S+", "", sentence)
    #extract hashtags
    hashtags.extend(re.findall(r"#\w+", sentence))
    sentence = re.sub(r"#\w+", "", sentence)
    #remove punctuations
    sentence = re.sub(r"[.!]", "", sentence)
    #finalize
    words = sentence.split()
    return [words, emails, urls, hashtags, ]

words, emails, urls, hashtags,  = preproccsss_sentence(sentence)
print(words, emails, urls, hashtags)

with open("emails.txt", "w") as file:
    for each in emails:
      file.write(each + "\n")

with open("urls.txt", "w") as file:
    for each in urls:
      file.write(each + "\n")

with open("hashtags.txt", "w") as file:
    for each in hashtags:
      file.write(each + "\n")