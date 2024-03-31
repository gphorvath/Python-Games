import os
from ollama_wrapper import OllamaWrapper

def game_setup():
    llm = OllamaWrapper()
    llm.set_system_prompt('Your name is Fred. You are a grumpy old man.')
    return llm

def game_loop():
    os.system('clear')
    # print("Welcome to Prisoner's Dilemma!")
    
    fred = game_setup()
    
    quit = False
    
    while not quit:
        prompt = input("Ask Fred a question: ")
        
        if(prompt.lower() == "exit" or prompt.lower() == "quit"):
            response = fred.chat_response("Make a snarky comment about quitting the game.")
            quit = True
        else:
            response = fred.chat_response(prompt)
        
        print(response)
    
    
    if(input("Would you like to play again? (yes/no): ").lower() == "yes"):
        game_loop()
        
game_loop()