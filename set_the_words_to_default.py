import spacy
#python -m spacy download de_core_news_sm
#pip install spacy


def singularize(word, pos):
    # Einfache Logik, um einige häufige Fälle von Pluralformen zu Singularformen zu konvertieren
    if pos == "NOUN":
        if word.endswith('en'):
            return word[:-2]
        elif word.endswith('er'):
            return word[:-2]
        elif word.endswith('e'):
            return word[:-1]
    return word

def lemmatize_and_singularize(words):
    nlp = spacy.load("de_core_news_sm")

    processed_words = []
    for word in words:
        doc = nlp(word)
        lemma = doc[0].lemma_
        pos = doc[0].pos_
        singular = singularize(lemma, pos)
        processed_words.append(singular)

    return processed_words


def lemmatize_sogularize_words(words):
    
    return(lemmatize_and_singularize(words))