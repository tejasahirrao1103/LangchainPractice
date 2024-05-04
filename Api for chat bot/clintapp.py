import requests

def ollama_response(ip):
    responses =requests.post("http://localhost:8080/essay/invoke",
    json={'input':{'topic':ip},})

    #return(responses.json())
    print(responses.json()['output'])

ip = input("enter topic: ")
ollama_response(ip)
#print(op)
