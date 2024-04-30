from langchain_community.llms import Ollama 
from langchain_core.prompts import ChatPromptTemplate

from fastapi import FastAPI
from langserve import add_routes
import uvicorn , os

from dotenv import load_dotenv
load_dotenv()

app = FastAPI(
    title="lanchain api server",
    version="1",
    description="simple api"
)

llm = Ollama(model="llama2")

prompt1= ChatPromptTemplate.from_template("write a essay on {topic} in 100 word")


add_routes(
    app,
    prompt1|llm,
    path= "/essay"
)

if __name__=="__main__":
    uvicorn.run(app,host="localhost",port="8080")