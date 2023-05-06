import streamlit as st
from streamlit_chat import message
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.embeddings import CohereEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.document_loaders.csv_loader import CSVLoader
import os
from langchain.vectorstores import FAISS
import tempfile


user_api_key = os.environ.get("OPENAI_API_KEY")
# os.environ["OPENAI_API_KEY"] = "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"

def csv_chatbot():
   
    uploaded_file = st.sidebar.file_uploader("upload", type="csv")

    if uploaded_file :
      st.info("Talk to your data with our AI chatbot")
      with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(uploaded_file.getvalue())
        tmp_file_path = tmp_file.name

      loader = CSVLoader(file_path=tmp_file_path, encoding="utf-8")
      data = loader.load()

      embeddings = OpenAIEmbeddings()
 
      vectors = FAISS.from_documents(data, embeddings)

      chain = ConversationalRetrievalChain.from_llm(llm = ChatOpenAI(temperature=0.0,model_name='gpt-3.5-turbo', openai_api_key=user_api_key),
                                                                      retriever=vectors.as_retriever())

      def conversational_chat(query):
        
        result = chain({"question": query, "chat_history": st.session_state['history']})
        st.session_state['history'].append((query, result["answer"]))
        
        return result["answer"]
    
      if 'history' not in st.session_state:
        st.session_state['history'] = []

      if 'generated' not in st.session_state:
        st.session_state['generated'] = ["Hello ! Ask me anything about " + uploaded_file.name + " 🤗"]

      if 'past' not in st.session_state:
        st.session_state['past'] = ["Hey ! 👋"]
        
    #container for the chat history
      response_container = st.container()
    #container for the user's text input
      container = st.container()

      with container:
        with st.form(key='my_form', clear_on_submit=True):
            
            user_input = st.text_input("Query:", placeholder="Talk about your csv data here (:", key='input_user')
            submit_button = st.form_submit_button(label='Send')
            
        if submit_button and user_input:
            output = conversational_chat(user_input)
            
            st.session_state['past'].append(user_input)
            st.session_state['generated'].append(output)

      if st.session_state['generated']:
        with response_container:
            for i in range(len(st.session_state['generated'])):
                message(st.session_state["past"][i], is_user=True, key=str(i) + '_user1', avatar_style="big-smile")
                message(st.session_state["generated"][i], key=str(i)+'_user2', avatar_style="thumbs")


# if __name__ == "__main__":
#     csv_chatbot()