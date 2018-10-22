from janome.tokenizer import Tokenizer

t = Tokenizer()

s = '今日は良いお天気ですね！'

print(type(t.tokenize(s)))
# <class 'list'>

print(type(t.tokenize(s)[0]))
# <class 'janome.tokenizer.Token'>

for token in t.tokenize(s):
    print(token)