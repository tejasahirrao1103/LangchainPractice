from langchain_community.llms import Ollama 
from langchain_core.prompts import ChatPromptTemplate

from fastapi import FastAPI
from langserve import add_routes
import uvicorn , os

from datetime import date

#from dotenv import load_dotenv
#load_dotenv()

#os.environ["LANGCHAIN_TRACING_V2"] = "true"
#os.environ["LANGCHAIN_API_KEY"]= os.getenv("langchain_key")

app = FastAPI(
    title="lanchain api server",
    version="1",
    description="simple api"
)

llm = Ollama(model="llama3")

prompt1=ChatPromptTemplate.from_messages(
    [
        ("system",
        """Imagine you are a knowledgeable assistant specializing in crop information. 
         Your expertise assists farmers with buying, selling there crop, decision-making where and when to sell crop, predict 
         futre date and price to sell ther crop for max profit and give general qutions answer based on you khowledge for general quetion there is 
         no need to analyse old data everytime if qution is out of scope dont give answer . 
         Your suggestions are based on real-time market {price}, 
         which are provided by the farmers themselves. Additionally, 
         you have access to data on the average prices from the past 7 days data: {data} also  
         you have insights related to the Indian agricultural season getting from current date {date},. 
         If ever you lack specific information, don't hesitate to consult the farmer 
         for further details."  """),
    
        ("user","Question:{question}")
    ]
    
)



add_routes(
    app,
    prompt1|llm,
    path= "/bot"
)

if __name__=="__main__":
    uvicorn.run(app,host="localhost",port="8080")