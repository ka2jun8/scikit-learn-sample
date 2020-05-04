from gensim import matutils

def vec2dense(vec, num_terms):
    return list(matutils.corpus2dense([vec], num_terms = num_terms).T[0])

def dic2vec(dictionary, words):
    ret = []
    for i in range(len(words)):
        bow = dictionary.doc2bow(words[i])
        dic_length = len(dictionary)
        dense = vec2dense(bow, dic_length)
        ret.append(dense)
    return ret
