import string
import re


def clean_text(sentences):
    """Cleans the sentences so it's easier for processing later on.

    Parameters
    ----------
    sentences : [list]
        [a list of sentences.]

    Returns
    -------
    [list]
        [returns a list of processed sentences.]
    """

    for sentence in sentences:
        sentence = sentence.replace("crore", "money")
        sentence = sentence.replace("lakh", "money")
        sentence = re.sub(r"\b\w{1,2}\b", "", sentence)
        sentence = sentence.replace("\d+", "number")
        sentence = sentence.translate(str.maketrans("", "", string.punctuation))

    return sentences
