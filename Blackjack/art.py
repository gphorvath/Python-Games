logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
'-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      '------'                           |__/           
"""

def concatenate_cards(*cards):
    concatenated_cards = ""
    for lines in zip(*[card.split("\n") for card in cards]):
        concatenated_cards += "  ".join(lines) + "\n"
    return concatenated_cards

def get_card(digit_and_suit):
    if len(digit_and_suit) == 3:
        digit = digit_and_suit[0] + digit_and_suit[1]
        suit = digit_and_suit[2]
    elif len(digit_and_suit) == 2:
        digit, suit = digit_and_suit
    else:
        return f"Invalid card: {digit_and_suit}"
    
    if suit == "♠":
        return spades(digit)
    elif suit == "♦":
        return diamonds(digit)
    elif suit == "♥":
        return hearts(digit)
    elif suit == "♣":
        return clubs(digit)
    else:
        return f"Invalid suit: {suit}"
    
def card_back_base():
    return """
.------.
|░░░░░░|
|░░░░░░|
|░░░░░░|
|░░░░░░|
'------'
"""

def card_back():
    return """
.------.
|░GAME░|
|░SHE░░|
|░░NAN░|
|░IGANS|
'------'
"""

def spades(digit):
    digit = str(digit)
    if(len(digit) == 1):
        return f""" 
.------.
|{digit}     |
|  /\  |
| (__) |
|  /\ {digit}|
'------'
"""
    elif(len(digit) == 2):
        return f""" 
.------.
|{digit}    |
|  /\  |
| (__) |
|  /\{digit}|
'------'
"""
    else:
        return f"Invalid digit: {digit}"

def diamonds(digit):
    digit = str(digit)
    if(len(digit) == 1):
        return f""" 
.------.
|{digit} /\  |
| /  \ |
| \  / |
|  \/ {digit}|
'------'
"""
    elif(len(digit) == 2):
        return f""" 
.------.
|{digit}/\  |
| /  \ |
| \  / |
|  \/{digit}|
'------'
"""
    else:
        return f"Invalid digit: {digit}"
    
def hearts(digit):
    digit = str(digit)
    if(len(digit) == 1):
        return f""" 
.------.
|{digit}_  _ |
|( \/ )|
| \  / |
|  \/ {digit}|
'------'
"""
    elif(len(digit) == 2):
        return f""" 
.------.
|{digit}  _ |
|( \/ )|
| \  / |
|  \/{digit}|
'------'
"""
    else:
        return f"Invalid digit: {digit}"

def clubs(digit):
    digit = str(digit)
    if(len(digit) == 1):
        return f""" 
.------.
|{digit} _   |
| (_)  |
|(_x_) |
|  Y  {digit}|
'------'
"""
    elif(len(digit) == 2):
        return f""" 
.------.
|{digit}_   |
| (_)  |
|(_x_) |
|  Y {digit}|
'------'
"""
    else:
        return f"Invalid digit: {digit}"
    
bust = """
 _               _   
| |             | |  
| |__  _   _ ___| |_ 
| '_ \| | | / __| __|
| |_) | |_| \__ \ |_ 
|_.__/ \__,_|___/\__|
"""

win = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡴⠚⠙⠲⢤⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠴⢊⣥⣤⣤⣤⣶⣦⣍⠓⠦⣄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣦⣈⠙⠻⢿⣿⡛⣻⣿⣿⣿⠂⠈⠙⢦⡄⠀
⠀⠀⠀⠀⠀⠀⢀⡀⠀⠠⣶⣿⣿⣿⣿⣿⣶⣤⣈⠙⠻⢿⡿⠟⣀⠴⢚⣻⠆⠀
⠀⠀⠀⠀⡠⠔⣩⣴⣿⣦⣄⠙⠻⢿⣿⣿⣿⣿⣿⣿⡶⠀⠀⢋⡡⠖⢉⡽⠂⠀
⠀⢠⣔⠋⠀⠀⣿⣿⣿⡟⠛⣿⣶⣤⡈⠛⠿⡿⠟⢁⣤⣾⠀⢉⡤⠚⣡⠝⠃⠀
⠀⠤⣎⡙⠲⣌⡛⠿⣿⣿⣿⣿⣿⡿⠟⣃⠤⠀⣾⣿⣿⣿⠀⣁⠔⠊⠀⠀⠀⠀
⠀⠐⢿⣉⠓⠦⣍⡒⠬⣁⠀⢀⣠⠔⣋⠵⠂⠀⣿⣿⣿⠟⠀⠁⠀⠀⠀⠀⠀⠀
⠀⠘⠳⣌⡙⠲⣄⡙⠲⢬⣉⣉⠴⠋⣡⠔⢋⠀⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠙⠲⢤⣉⠓⢦⣈⣡⠖⢋⡠⠖⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠓⠦⣌⡤⠖⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""

lose = """
_____.___.              .____                        
\__  |   | ____  __ __  |    |    ____  ______ ____  
 /   |   |/  _ \|  |  \ |    |   /  _ \/  ___// __ \ 
 \____   (  <_> )  |  / |    |__(  <_> )___ \\  ___/ 
 / ______|\____/|____/  |_______ \____/____  >\___  >
 \/                             \/         \/     \/ 
"""
