import streamlit as st
import openai
import os
from dotenv import load_dotenv


load_dotenv()
openai.api_key = os.environ.get("OPENAI_API_KEY")



completion = openai.ChatCompletion()


def textsource_summarize_analysis(text):
    response = completion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful AI assistant which will help the user to perform text summarization on their text data provided. Help company leaders quickly identify common themes and issues that need to be addressed in order to improve company culture.",
            },
            {"role": "user", "content": text},
        ],
        temperature=0.5,
    )

    answer = response.choices[0].message["content"]

    return answer



def summarize_text(prompt , token_length):
    augmented_prompt = f"Summarize this text in an abstractive manner preserving the semantic meaning and frame the summarized text as per the token length: {prompt}"
    try:
        st.session_state["summary"] = openai.Completion.create(
            model="text-davinci-003",
            prompt=augmented_prompt,
            temperature=0.5,
            max_tokens=token_length,
        )["choices"][0]["text"]
    except:
        st.write('There was an error =(')
        
       
def summarize():
  
        if "summary" not in st.session_state:
            st.session_state["summary"] = ""
  
        
        st.header("Summarize your Text/Feedback:")
  
        input_text = st.text_area(label="Enter your text:", value="", height=250 , key="input_text")
        token_len = st.slider('Select Response Length', 50, 1000, step=10, value=250)
        col1 , col2 = st.columns(2)
        with col1:
            button = st.button(
        "Summarize",
            on_click=summarize_text,
        kwargs={"prompt": input_text ,
                "token_length": token_len
                },
  )     
        with col2:
             clear_button = st.button("Clear Response")
             if clear_button:
              input_text = ""
              st.session_state["summary"] = ""
        with st.spinner(text="Generating Summary., k.."):
            if button and input_text:
                 st.text_area(label="Summarized text:", value=st.session_state["summary"], height=250)
                 st.success("Summary Generated Successfully!")


