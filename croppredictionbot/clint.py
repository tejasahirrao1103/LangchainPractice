import requests
from datetime import date
def ollama_response(date,dateprice,ip,quetion):

    ##🔵api calling with post methode
    responses =requests.post("http://localhost:8080/bot/invoke",
    json={'input':{'date':date,'data':dateprice,'price':ip, 'question':quetion}})

    return(responses.json())
    #print(responses.json()['output'])




date = str(date.today())
dateprice = """
date:2024/04/15, avg price: 3465rs/qt
date:2024/04/16, avg price: 2984rs/qt
date:2024/04/17, avg price: 2053rs/qt
date:2024/04/18, avg price: 4131rs/qt
date:2024/04/19, avg price: 2876rs/qt
date:2024/04/20, avg price: 3189rs/qt
date:2024/04/21, avg price: 3447rs/qt
date:2024/04/22, avg price: 1903rs/qt
date:2024/04/23, avg price: 3793rs/qt
date:2024/04/24, avg price: 3541rs/qt
date:2024/04/25, avg price: 3738rs/qt
"""
ip= input("provide current price of the crop first: ")
quetion = input("ask quetion: ")





##🔵fucntion calling with pareameters
ollama_response(date,dateprice,ip,quetion)
##print(op)
