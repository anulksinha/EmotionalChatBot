import gensim
import re
import numpy as np

word2vec_path = './GoogleNews-vectors-negative300.bin'
unknown_vectors = {}

def initialize():
    return gensim.models.KeyedVectors.load_word2vec_format(word2vec_path, binary=True)

# input: trained model, one sentence (string)
# output: a list of word2vec vectors for that sentence
def vectorize(model, sentence):
    if model is None:
        print "Please initialize the model before vectorizing a sentence!"
        return []

    sentence = re.sub(r"([\w/'+$\s-]+|[^\w/'+$\s-])\s*", r" \1", sentence)
    words = str.split(sentence.strip(), " ")
    vectorized_sentence = []

    for word in words:
        if word in model:
            vectorized_sentence.append(model[word])
        elif word in unknown_vectors:
            vectorized_sentence.append(unknown_vectors[word])
        else:
            # Yoon Kim's unknown word handling, 2014
            # https://github.com/yoonkim/CNN_sentence/blob/master/process_data.py#L88
            unknown_vectors[word] = np.random.uniform(-0.25,0.25,300)
            vectorized_sentence.append(unknown_vectors[word])   

    return vectorized_sentence

#model = initialize()
#print vectorize(model, "Hello, this is a test!")
