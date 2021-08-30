from textblob import TextBlob
import pandas as pd


def analysis(aspects):
    """[Computes the sentiment score of the sentences.]

    Parameters
    ----------
    aspects : [list]
        [a list that has two columns.]

    Returns
    -------
    [pd.dataframe]
        [Returns a dataframe with the scores computed.]
    """
    for aspect in aspects:
        aspect["sentiment"] = TextBlob(aspect["description"]).sentiment

    new_df = pd.DataFrame(aspects)
    new_df["Polarity"] = [b.polarity for b in new_df["sentiment"]]
    new_df["Subjectivity"] = [b.subjectivity for b in new_df["sentiment"]]
    new_df.drop("sentiment", axis="columns", inplace=True)
    return new_df
