import time
import os

from . import text
from . import analytics
from . import vector
from . import dictionary
from . import svm

print("start")

print("analytics texts")
startTime = time.time()

s_list, labels = text.get_sentence_and_labels_for_training()
words = analytics.get_words(s_list)

spentTime = round(time.time() - startTime, 2)
print("analytics end:{0}".format(spentTime) + "[s]")

print("creating dictionary")
startTime = time.time()

dct = dictionary.get_dictionary(words, True)

spentTime = round(time.time() - startTime, 2)
print("creating dictionary end:{0}".format(spentTime) + "[s]")

print("converting dictionary to vector")
startTime = time.time()

vectors = vector.dic2vec(dct, words)

spentTime = round(time.time() - startTime, 2)
print("converting dictionary to vector end:{0}".format(spentTime) + "[s]")

print("training by svm")
startTime = time.time()

clf = svm.train(vectors, labels)

spentTime = round(time.time() - startTime, 2)
print("training by svm end:{0}".format(spentTime) + "[s]")

print("testing targets")
startTime = time.time()

test_list = text.get_sentence("./target/")
test_words = analytics.get_words(test_list)
test_all = vector.dic2vec(dct, test_words)

result = clf.predict(test_all)
print("result: {0}".format(result))

spentTime = round(time.time() - startTime, 2)
print("testing targets end:{0}".format(spentTime) + "[s]")
