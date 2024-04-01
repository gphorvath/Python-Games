# Prisoner's Dilemma

``` bash
__________        .__                                /\        
\______   \_______|__| __________   ____   __________)/ ______ 
 |     ___/\_  __ \  |/  ___/  _ \ /    \_/ __ \_  __ \/  ___/ 
 |    |     |  | \/  |\___ (  <_> )   |  \  ___/|  | \/\___ \  
 |____|     |__|  |__/____  >____/|___|  /\___  >__|  /____  > 
                          \/           \/     \/           \/  
       ________  .__.__                                        
       \______ \ |__|  |   ____   _____   _____ _____          
        |    |  \|  |  | _/ __ \ /     \ /     \\__  \         
        |    `   \  |  |_\  ___/|  Y Y  \  Y Y  \/ __ \_       
       /_______  /__|____/\___  >__|_|  /__|_|  (____  /       
               \/             \/      \/      \/     \/        
```

## Description

A game where the main character (powered by a Large Language Model) is a suspect in an investigation. Your goal is to discover three clues to solve the crime.

## Instructions

This one requires a little more setup.

``` bash
python -m venv .venv
pip install requirements.txt
make setup-ollama
python game.py
```

## Considerations

The responses of the character are often lacking context and vary dramatically in revealing the clues. There are a lot of ways to improve upon this game.
