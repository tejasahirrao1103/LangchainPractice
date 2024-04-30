from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
from dotenv import load_dotenv
import os
load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("openai_key")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"]= os.getenv("langchain_key")

## prompt Template

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","you are a helpful assistant. plese response to the user queires"),
        ("user","Question:{question}")
    ]
)

## streamlit framework

st.title('Langchain Demo With OPENAI API')
input_text=st.text_input("Search the topic u want")

## openAI LLM
llm = ChatOpenAI(model="gpt-3.5-turbo")

##output parser
output_parser= StrOutputParser()


##chain
chain=prompt|llm|output_parser


if input_text:
    st.write(chain.invoke({'question':input_text}))