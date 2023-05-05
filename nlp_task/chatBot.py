import streamlit as st
import os
import openai



# load_dotenv()
openai.api_key = os.environ.get("OPENAI_API_KEY")

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
    
    uploaded_file = st.file_uploader(
            "Upload your company data", type=["pdf", "txt", "csv", "xlsx"]
        )