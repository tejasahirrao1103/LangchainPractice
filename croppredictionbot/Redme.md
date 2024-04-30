step 1. install all requirement form requrement.txt file

step 2. run botApi file

step 3. (optional but do visit )
        goto localhost:8080/bot/playground to test api with UI
        goto localhost:8080/docs to read swagger documentation
        
step 4. {Related Api calling}

        link ->> " http://localhost:8080/bot/invoke " this is your link for api calling
        use "POST" Method to call api

        API parameter ->>

         "input": 
         {
        "data": "string", 
        "date": "string",
        "price": "string",
        "question": "string"
        }


    Explination: 

        ##"data" is reffer to the previous market data like         
         date:2024/04/15, avg price: 3465rs/qt
         date:2024/04/16, avg price: 2984rs/qt
         date:2024/04/17, avg price: 2053rs/qt
         date:2024/04/18, avg price: 4131rs/qt

         note: make a string variable for data and pass  it while calling api 

        ##"date" is reffer to the current date of today
          
          note: fetch current date from your system and make a string variable for date and pass it while calling api 

        ##"price" is reffer to current market price of specific crop 

        note: take it as a user input or make variable with the dummy price and pass it while calling api 

        ##"question" is reffer to qury ask by the user 

        note: it is one of the important parameter take it as a input from use and pass it while calling to user 

    #note: ther is no need to full fill all parameter while calling api but {question} parameter must be present and valid qution we cant send it null to LLM

step 5. 
     you recive responce in form of JSON must convert it in string while printing Output

step 6. 
    you can cange promp for getting better answer form llm
        