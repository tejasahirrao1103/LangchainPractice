from langchain_community.llms import Ollama 
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings

from langchain_core.runnables import RunnablePassthrough

pdfloader = PyPDFLoader("D:\\LangchainPractice\\rag\\reserchpaper.pdf")
pdf = pdfloader.load()


textsplitter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap=100)
docs= textsplitter.split_documents(pdf)


vectoredb = Chroma.from_documents(documents=docs,embedding=OllamaEmbeddings(model="nomic-embed-text",temperature= 0.6,show_progress=True))
#retriver = vectoredb.as_retriever(search_type="mmr", search_kwargs={'k': 6, 'lambda_mult': 0.25})
retriver = vectoredb.as_retriever()

promt = PromptTemplate.from_template("""
You are an assistant for question-answering tasks. Use the following pieces of retrieved context to 
answer the question. If you don't know the answer, just say that you don't know. Use three sentences 
maximum and keep the answer concise.
Question: {question} 
Context: {context}
""")

llm = Ollama(model="llama3",temperature = 0.6)

parser = StrOutputParser()

chain= (
    {"context": retriver, "question":RunnablePassthrough()}
    |promt
    |llm
    |parser
)

op=chain.invoke("email address of person name that are start tej")
print(op)