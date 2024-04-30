from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os

from dotenv import load_dotenv
load_dotenv()


os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("langchain_key")



promtp= ChatPromptTemplate(
    [
        ("system", "write a 2 line poem on topic given by the user"),
        ("user","Topic:{topic}")
    ]
)


llm = Ollama(model="llama2")
outputparser = StrOutputParser()
chain = promtp|llm|outputparser

while True:
    ip= input("enter topic: ")
    print(chain.invoke({"topic":ip}))
    print("\n")
