import MeCab

mecab = MeCab.Tagger('-Ochasen')

def tokenize(text):
    node = mecab.parseToNode(text)
    while node:
        word = node.surface
        hinshi = node.feature.split(",")[0]
        if hinshi == '名詞':
            yield word.lower()
        node = node.next

def get_words(contents):
    ret = []
    for content in contents:
        ret.append(get_words_main(content))
    return ret

def get_words_main(content):
    return [token for token in tokenize(content)]
