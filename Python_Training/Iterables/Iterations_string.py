class Sentence:
    def __init__(self,sentence):
        self.sentence = sentence
        self.index = 0
        self.words = self.sentence.split()

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self.words):
            raise StopIteration
        index = self.index
        self.index +=1
        return self.words[index]
    
def sentence(sentence):
    for words in sentence.split():
        yield words
    return words
    
    
my_sentence = sentence("This is a Sentence")
for num in my_sentence:
    print(num)
