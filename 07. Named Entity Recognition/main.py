﻿import nltk
from nltk.corpus import state_union
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tokenize import PunktSentenceTokenizer

train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")

custom_sentence_tokenizer = PunktSentenceTokenizer(train_text)
tokenized_words = custom_sentence_tokenizer.tokenize(sample_text)


def process_content():
    try:
        for w in tokenized_words:
            words = nltk.word_tokenize(w)
            tagged = nltk.pos_tag(words)

            named_entity = nltk.ne_chunk(tagged)
            named_entity.draw()

    except Exception as e:
        print(str(e))


process_content()
