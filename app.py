from langchain.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
)
from langchain_community.chat_message_histories import StreamlitChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema.output_parser import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from streamlit_mic_recorder import speech_to_text
from streamlit_TTS import text_to_speech
from gtts.lang import tts_langs
import streamlit as st
from gtts import gTTS
from dotenv import load_dotenv
import os

load_dotenv()

st.markdown("""
    <style>
    .title {
        font-family: 'Helvetica Neue', sans-serif;
        color: #c9c9c9;
        font-size: 2.5em;
        font-weight: bold;
        text-align: center;
        padding: 20px 0;
        background: -webkit-linear-gradient(#f8cdda, #ff0000);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .subtitle {
        font-family: 'Helvetica Neue', sans-serif;
        color: #4B4B4B;
        font-size: 1.5em;
        text-align: center;
        margin-top: -10px;
        margin-bottom: 30px;
    }
    </style>
""", unsafe_allow_html=True)

# Display the styled title
st.markdown('<div class="title">Urdu Voice Query</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Speech-to-Text and Text-to-Speech Assistant in Urdu</div>', unsafe_allow_html=True)
# Display description
st.markdown("""
    <style>
    .description {
        font-family: 'Helvetica Neue', sans-serif;
        color: #f5740b;
        font-size: 1em;
        text-align: center;
        margin-bottom: 20px;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)
st.markdown('<div class="description">Record your voice in Urdu and receive a spoken response in Urdu.</div>', unsafe_allow_html=True)

api_key = "https://aistudio.google.com/app/apikey"
# st_audiorec()
    
    
    
    
prompt = ChatPromptTemplate(
    messages=[
        SystemMessagePromptTemplate.from_template(
            "You are a helpful AI assistant.Please always respond user query in Pure Urdu language."
        ),
        MessagesPlaceholder(variable_name="chat_history"),
        HumanMessagePromptTemplate.from_template("{question}"),     
    ]
)

msgs = StreamlitChatMessageHistory(key="langchain_messages")

model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash", google_api_key=os.getenv("google_api_key")
)

chain = prompt | model | StrOutputParser()

chain_with_history = RunnableWithMessageHistory(
    chain,
    lambda session_id: msgs,
    input_messages_key="question",
    history_messages_key="chat_history",
)


langs = tts_langs().keys()


with st.spinner("Converting Speech To Text..."):
    text = speech_to_text(
        language="ur", use_container_width=True, just_once=True, key="STT"
    )

if text:
    st.chat_message("human").write(text)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""

        config = {"configurable": {"session_id": "any"}}
        response = chain_with_history.stream({"question": text}, config)

        for res in response:
            full_response += res or ""
            message_placeholder.markdown(full_response + "|")
            message_placeholder.markdown(full_response)

    with st.spinner("Converting Text To Speech.."):
        tts = gTTS(text=full_response, lang='ur')
        tts.save("output.mp3")
        st.audio("output.mp3")

else:
    st.error("Could not recognize speech.Please speak again.")
