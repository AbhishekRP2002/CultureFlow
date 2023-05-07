import streamlit as st
import openai
import os
import spacy
import gensim
import gensim.corpora as corpora
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import spacy_streamlit


nlp = spacy.load("en_core_web_sm")


# load_dotenv()
openai.api_key = os.environ.get("OPENAI_API_KEY")



completion = openai.ChatCompletion()


def textsource_classification_analysis(text):
    response = completion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful AI assistant which will help in Topic Modelling , Context Identification , Contextual Topic Identification .  Context identification, keyword extraction, and topic modeling can provide a data-driven approach to understanding company culture and guiding improvement efforts.Perform a detailed analysis and provide the response in a tabular format.Also display atleast  top 7 themes of the text source in a organized format.Arrange in descending order of the most related themes to the least related themes.",
            },
            {"role": "user", "content": text},
        ],
        temperature=0.5,
    )

    answer = response.choices[0].message["content"]

    return answer




def topic_modeling(text):
    words = gensim.utils.simple_preprocess(text)
    data_words = [words]
    id2word = corpora.Dictionary(data_words)
    corpus = [id2word.doc2bow(text) for text in data_words]
    lda_model = gensim.models.ldamodel.LdaModel(corpus=corpus, id2word=id2word, num_topics=1, random_state=100, update_every=1, chunksize=100, passes=10, alpha='auto', per_word_topics=True)
    return lda_model.print_topics()

def named_entity_recognition(text):
    doc = nlp(text)
    spacy_streamlit.visualize_ner(doc, labels=nlp.get_pipe('ner').labels)
    return [(ent.text, ent.label_) for ent in doc.ents]
    

def keyword_extraction(text):
    doc = nlp(text)
    return [token.text for token in doc if token.is_stop == False and token.is_punct == False]

def generate_wordcloud(text):
    wordcloud = WordCloud(width=800, height=800, background_color='white', stopwords=None, min_font_size=10).generate(text)
    plt.figure(figsize=(8, 8), facecolor=None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad=0)
    # fig , ax = plt.subplots()
    st.pyplot()

# st.title("Text Analysis App")

# input_text = st.text_area("Enter your text here")

# if st.button("Analyze"):
#     st.header("Topic Modeling")
#     topics = topic_modeling(input_text)
#     for topic in topics:
#         st.write(topic)

#     st.header("Named Entity Recognition")
#     entities = named_entity_recognition(input_text)
#     for entity in entities:
#         st.write(entity)

#     st.header("Keyword Extraction")
#     keywords = keyword_extraction(input_text)
#     st.write(keywords)

#     st.header("Word Cloud")
#     generate_wordcloud(input_text)


def context_analysis():
    st.info("This is a context analysis model for given text source")
    
    with st.form(key = "context_analysis_form"):
        input_text = st.text_area("Enter the text data here")
        submit_button = st.form_submit_button(label = "Analyze")
        # clear_button = st.form_submit_button(label = "Clear")
        if submit_button:
            st.subheader("Topic Modelling")
            topics = topic_modeling(input_text)
            for topic in topics:
                st.write(topic)

            st.subheader("Named Entity Recognition")
            entities = named_entity_recognition(input_text)
            for entity in entities:
                st.write(entity)

            st.header("Keyword Extraction")
            keywords = keyword_extraction(input_text)
            st.write(keywords)

            st.subheader("Word Cloud")
            generate_wordcloud(input_text)

    
            
    