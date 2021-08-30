from src.clean import clean_text
from src.extract import extract_entity_words
from src.analyze_sentiment import analysis
import spacy
import textblob
import streamlit as st


if __name__ == "__main__":
    # sentence = ['the hotel was very nice',
    # 'the cake was pretty.']
    st.title("Aspect Based Sentiment Analysis")
    st.subheader(
        "This model will extract the main entities \
        from your sentence and the words that describe it."
    )
    st.subheader("It will also compute the sentiment of that entity.")
    sentence = [
        st.text_input(
            "Enter a text to \
        compute sentiment.",
            "The pizza was very good.",
        )
    ]
    clean_sent = clean_text(sentence)

    extracted_dict = extract_entity_words(clean_sent)
    st.write("These are the extracted entities.")
    st.dataframe(extracted_dict)
    df_analysis = analysis(extracted_dict)
    st.write("These are the sentiment scores.")
    st.dataframe(df_analysis)
    st.write(
        "The number close to positive 1 in polarity means that\
         its a positive sentence and vice-versa."
    )
    st.write(
        "Subjectivity means personal opinion whereas its \
        opposite objective means more factual."
    )
