import streamlit as st
import os
import openai
import pandas as pd
from streamlit_chat import message
# from nlp_task.textsource_chatbot import csv_chatbot
from test import csv_chatbot
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.embeddings import CohereEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.document_loaders.csv_loader import CSVLoader
import os
from langchain.vectorstores import FAISS
import tempfile


user_api_key = os.environ.get("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = "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"



# load_dotenv()
openai.api_key = os.environ.get("OPENAI_API_KEY")

# Define the 'generate_response' function to send the user's message to the AI model 
# and append the response to the 'generated' list.
def generate_response(prompt):
    # The 'prompts' list is updated with the user's message before sending it to the AI model.
    st.session_state['prompts'].append({"role": "user", "content":prompt})
    # The 'openai.ChatCompletion.create' function is used to generate a response from the AI model.
    completion=openai.ChatCompletion.create(
        model="gpt-3.5-turbo", # The 'engine' parameter specifies the name of the OpenAI GPT-3.5 Turbo engine to use.
        temperature=0.7, # The 'temperature' parameter controls the randomness of the response.
        max_tokens=2000, # The 'max_tokens' parameter controls the maximum number of tokens in the response.
        top_p=0.95, # The 'top_p' parameter controls the diversity of the response.
        # The 'messages' parameter is set to the 'prompts' list to provide context for the AI model.
        messages = st.session_state['prompts']
    )
    # The response is retrieved from the 'completion.choices' list and appended to the 'generated' list.
    message=completion.choices[0].message["content"]
    return message


# The 'new_topic_click' function is defined to reset the conversation history and introduce the AI assistant.
def new_topic_click():
    st.session_state['prompts'] = [{"role": "system", "content": "You are an helpful AI assistant that could be used for company culture analytics and solutions.You are free to have open knowledge based conversations as well.You should be more engaging and interactive with the user. You can  collect or ask for feedback from employees on various aspects of company culture, such as communication, work-life balance, diversity and inclusion, and leadership. You could ask open-ended questions and use NLP techniques like sentiment analysis to analyze the responses and provide insights into areas of improvement.You can provide employees with learning and development opportunities that are aligned with the company's culture and values.You can help  to increase employee engagement by providing personalized recommendations based on an employee's interests and preferences"}]
    st.session_state['past'] = []
    st.session_state['generated'] = []
    st.session_state['user'] = ""
    
    
# The 'chat_click' function is defined to send the user's message to the AI model 
# and append the response to the conversation history.
def chat_click():
    if st.session_state['user']!= '':
        user_chat_input = st.session_state['user']
        output=generate_response(user_chat_input)
        st.session_state['past'].append(user_chat_input)
        st.session_state['generated'].append(output)
        st.session_state['prompts'].append({"role": "assistant", "content": output})
        st.session_state['user'] = ""


def global_chatbot():
     # Define the 'role' key as 'system' for the AI model's messages.
     st.info("Talk to our generalised AI Chatbot")
     if 'prompts' not in st.session_state:
          st.session_state['prompts'] = [{"role": "system", "content": "You are an helpful AI assistant that could be used for company culture analytics and solutions.You are free to have open knowledge based conversations as well.You should be more engaging and interactive with the user. You can  collect or ask for feedback from employees on various aspects of company culture, such as communication, work-life balance, diversity and inclusion, and leadership. You could ask open-ended questions and use NLP techniques like sentiment analysis to analyze the responses and provide insights into areas of improvement.You can provide employees with learning and development opportunities that are aligned with the company's culture and values.You can help  to increase employee engagement by providing personalized recommendations based on an employee's interests and preferences"}]
# The 'generated' list stores the AI model's responses to the user's messages.
     if 'generated_global' not in st.session_state:
          st.session_state['generated_global'] = []
# The 'past' list stores the user's previous messages.
     if 'past_global' not in st.session_state:
           st.session_state['past_global'] = []
     # generate_response()
     # new_topic_click()
     # chat_click()
     # The user's input is retrieved from the 'user' session state.
     user_input_global=st.text_input("You:", key="user")

# Streamlit to set the page layout and make the chat & new topic button.
     col1, col2, col3, col4, col5, col6 = st.columns([1,1,1,1,1,1])
     with col1:
      chat_button=st.button("Send", on_click=chat_click)
     with col2:
       new_topic_button=st.button("New Topic", on_click=new_topic_click)

# The 'message' function is defined to display the messages in the conversation history.
     if st.session_state['generated_global']:
      for i in range(len(st.session_state['generated_global'])-1, -1, -1):
              message(st.session_state['generated_global'][i], avatar_style='bottts', key=str(i))
              message(st.session_state['past_global'][i], is_user=True, avatar_style='thumbs', key=str(i) + '_user')







def ai_assistant():
    st.markdown(
        """
          <style>
          
          .chatbot-header{
               display: flex;
               flex-direction: column;
               justify-content: center;
               align-items: center;
               margin: 0px;
               }
               
               .chatbot-title{
                    font-size: 60px;
                    font-weight: bold;
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    color: #FF4B4B;
                    }
                    
                    
                    .block-container.css-z5fcl4.egzxvld4{
                         padding: 10px;
                    }
                    
                    .chatbot-subtitle{
                         font-size: 30px;
                         font-weight: 600;
                         border: 1.5px solid #ccc;
                         padding: 10px 20px;
                         border-radius: 10px;
                         box-shadow: 0px 0px 8px 0px #ccc;
                         margin-bottom: 20px;
                         }
          </style>
          
          <div class="chatbot-header">
               <div class="chatbot-title">
                       CultureFlow AI Chatbot
               </div>
               <div class="chatbot-subtitle">
                          Transforming and Improving Workplace Culture with AI-Powered Insights
               </div>
          </div>
                       
          
          """,
        unsafe_allow_html=True,
    )
    
    st.info("Our AI Chatbot can help you understand your company culture and improve it.It can use NLP techniques like sentiment analysis to analyze the responses and provide insights into areas of improvement. You can ask questions about your company culture or open-ended company culture related and get answers in real-time. You can also ask for suggestions on how to improve your company culture.")
    
    st.error("For understanding your own company please upload a dataset/CSV file of your company's employee feedbacks. You can also use sample dataset for demo purposes.")
    
    csv_chatbot()
    
   
    global_chatbot()
         