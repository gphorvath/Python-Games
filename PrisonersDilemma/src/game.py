import os
from typing import Literal
from win_condition import WinCondition
from ollama_wrapper import OllamaWrapper
from art import (
    logo,
)

def get_system_prompt(win_condition: WinCondition, stage: Literal[0, 1, 2, 3] = 0):
    prompt =  "You are a character in a video game."
    prompt += " You committed a crime and the player is a detective that must ask you questions to solve it."
    prompt += " Stay in character, don't break the fourth wall."
    prompt += " Be concise and limit your response length to one sentence."
    match stage:
        case 0:
            return f""" {prompt} """
        case 1:
            prompt += f" Your name is {win_condition.name}."
        case 2:
            prompt += f"You stole {win_condition.item}."
        case 3:
            prompt += f"You hid it in the {win_condition.location}."
    return f""" {prompt} """
    
def configure_suspect(win_condition: WinCondition, stage: Literal[0, 1, 2, 3] = 0):
    system_prompt = get_system_prompt(win_condition, stage=stage)
    llm = OllamaWrapper()
    llm.set_system_prompt(system_prompt)
    return llm

def game_loop():
    os.system('clear')
    print(logo)
        
    win_condition = WinCondition()
    
    stage = 0
    suspect = configure_suspect(win_condition=win_condition, stage=stage)
    
    print(suspect.chat_response("""
        Greet the player, but don't introduce yourself.
        Make sure to provide sure to tell them the following hints:
        "Type 'exit' or 'quit' to leave the game. 
        Type 'help' for help." """))
    
    stage += 1
    suspect = configure_suspect(win_condition=win_condition, stage=stage)
    
    while True:
        prompt = input("> ")
        print("\n")
        response = ""
        
        
        if(prompt.lower() == "exit" or prompt.lower() == "quit"):
            response += suspect.chat_response("Make a snarky comment about quitting the game.")
            return print(response + "\n")
        elif(prompt.lower() == "help"):
            response += suspect.chat_response("""
                Make a response that includes the following information: 
                "Question me to solve the crime" """)
        else:
            response += suspect.chat_response(prompt)
            
        print(response + "\n")
            
        if stage == 1:
            if win_condition.name in response:
                stage += 1
                suspect = configure_suspect(win_condition=win_condition, stage=stage)
        elif stage == 2:
            if win_condition.item in response:
                stage += 1
                suspect = configure_suspect(win_condition=win_condition, stage=stage)
        elif stage == 3:
            if win_condition.location in response:
                stage += 1
                suspect = configure_suspect(win_condition=win_condition, stage=stage)
                
        if stage == 4:
            print("You have solved the crime! Congratulations!")
            print(f"The suspect's name is {win_condition.name}, they stole {win_condition.item} and hid it in the {win_condition.location}.")
            if(input("Would you like to play again? (Type 'yes' or 'no'): ").lower() == "yes"):
                return game_loop()
            else:
                return print("Thanks for playing!")
            
if __name__ == "__main__":    
    game_loop()