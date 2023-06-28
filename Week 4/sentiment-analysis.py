from nltk.corpus import movie_reviews
from collections import Counter
from sklearn.model_selection import train_test_split

print(len(movie_reviews.fileids()))
print(movie_reviews.categories())
print(movie_reviews.words()[:100])
print(movie_reviews.fileids()[:10])

documents = [(list(movie_reviews.words(fileid)), category) 
            for category in movie_reviews.categories() 
            for fileid in movie_reviews.fileids(category)]

# print(documents[0])
print(len(documents))

distribution = Counter([label for (words, label) in documents])
print(distribution)

train, test = train_test_split(documents, test_size=0.1,)
