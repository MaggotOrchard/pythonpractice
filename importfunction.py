import ollama

import os

def ask(query):

    os.system('clear')
    while True:    
        response = ollama.chat(model='llama2', messages=[
            {

                'content': query
            },
        ])
        print(response['message']['content'])
        