import streamlit as st
import openai
import os
import pandas as pd
import streamlit.components.v1 as html
import streamlit.components.v1 as components
from textblob import TextBlob
import altair as alt
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from dotenv import load_dotenv

# Load the .env file
load_dotenv()
openai.api_key = os.environ.get("OPENAI_API_KEY")

completion = openai.ChatCompletion()


def textsource_sentiment_analysis(text):
    response = completion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful AI assistant which will help the user to perform sentiment analysis on their text data provided.Analyse the sentiment and provide the result to the user. Display the reult in multiple formats. and show the words that are most positive and negative.Try to display the positive and negative words in a tabular format.",
            },
            {"role": "user", "content": text},
        ],
        temperature=0.5,
    )

    answer = response.choices[0].message["content"]

    return answer




# Utility Functions
def convert_to_df(sentiment):
	sentiment_dict = {'polarity':sentiment.polarity,'subjectivity':sentiment.subjectivity}
	sentiment_df = pd.DataFrame(sentiment_dict.items(),columns=['metric','value'])
	return sentiment_df

def analyze_token_sentiment(docx):
	analyzer = SentimentIntensityAnalyzer()
	pos_list = []
	neg_list = []
	neu_list = []
	for i in docx.split():
		res = analyzer.polarity_scores(i)['compound']
		if res > 0.1:
			pos_list.append(i)
			pos_list.append(res)

		elif res <= -0.1:
			neg_list.append(i)
			neg_list.append(res)
		else:
			neu_list.append(i)

	result = {'positives':pos_list,'negatives':neg_list,'neutral':neu_list}
	return result 





def sentiment_analysis():
    with st.form(key = "sentiment_analysis_form"):
        input_text = st.text_area("Enter your text here")
        submit_button = st.form_submit_button(label = "Analyze Sentiment")
        
        col1, col2 = st.columns(2)
        if submit_button:
            with col1:
                st.info("Sentiment Analysis Results")
                sentiment = TextBlob(input_text).sentiment
                st.write(convert_to_df(sentiment))
                
                
                if sentiment.polarity > 0:
                    st.markdown("Sentiment : Positive")
                elif sentiment.polarity == 0:
                    st.markdown("Sentiment : Neutral")
                else:
                    st.markdown("Sentiment : Negative")
                    
                # Visualization
                result_df = convert_to_df(sentiment)
                c = alt.Chart(result_df).mark_bar().encode(
                    x='metric',
                    y='value',
                    color='metric')
                st.altair_chart(c,use_container_width=True)
                
            with col2:
                st.info("Token Sentiment Analysis")
                token_sentiment = analyze_token_sentiment(input_text)
                st.write(token_sentiment)
                    
                