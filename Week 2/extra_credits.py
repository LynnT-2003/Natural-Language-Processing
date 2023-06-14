import re

sentence = "hello 213 CSX4210 BG1403"

def preprocess_sentence(sentence):
    course_codes = re.findall(r"[A-Z a-z]{2,3}\d{4}", sentence)
    return course_codes

course_codes = preprocess_sentence(sentence)
print(course_codes) 