import streamlit as st
import openai
import os


# load_dotenv()
openai.api_key = os.environ.get("OPENAI_API_KEY")



completion = openai.ChatCompletion()


def textsource_recommendation_analysis(text):
    response = completion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful AI assistant which will help to provide actionable recommendations for the growth and improvement of company culture based on a given text source using Natural Language Processing.First perform sentiment analysis and identify areas where the company culture is positively or negatively perceived.Second Extract topics and themes: Identify the most common topics and themes in the text source.This will help you identify areas where the company culture is strong and areas where improvements are needed.Identify key phrases: Use entity recognition techniques to identify key phrases in the text source that are relevant to company culture. This might include phrases like 'teamwork', 'communication', 'diversity', and 'work-life balance'.Analyze patterns and trends: Use NLP techniques to analyze patterns and trends in the text source. This might include identifying common phrases, frequently used words, or frequently occurring topics.Make recommendations: Based on the analysis, provide actionable recommendations for improving the company culture. For example, if the sentiment analysis indicates that employees are generally unhappy, you might recommend implementing a more robust employee feedback program. If the topic modeling indicates that communication is a common theme, you might recommend improving communication channels and encouraging more open communication among employees.Provide in depth analysis and  actionable recommendations to the user in bullet points",
            },
            {"role": "user", "content": text},
        ],
        temperature=0.5,
    )

    answer = response.choices[0].message["content"]

    return answer


def recommend():
    st.info("This is a recommendation model based on given text source")