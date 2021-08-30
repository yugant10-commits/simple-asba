import spacy

nlp = spacy.load("en_core_web_sm")


def extract_entity_words(sentences):
    """[Extracts the entity words and\
         their surrouding description words.]

    Parameters
    ----------
    sentences : [list]
        [takes in a list of sentences.]

    Returns
    -------
    [list]
        [a list with two columns namely, aspect and description.]
    """
    aspects = []
    for sentence in sentences:
        doc = nlp(sentence)
        descriptive_term = ""
        target = ""
        for token in doc:
            if token.dep_ == "nsubj" and token.pos_ == "NOUN":
                target = token.text
            if token.pos_ == "ADJ":
                prepend = ""
                for child in token.children:
                    if child.pos_ != "ADV":
                        continue
                    prepend += child.text + " "
                descriptive_term = prepend + token.text
                aspects.append({"aspect": target, "description": descriptive_term})
    return aspects
