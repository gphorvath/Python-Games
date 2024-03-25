import random
import os
from art import (
    logo,
    get_card,
    concatenate_cards,
    card_back,
    bust,
    win,
    lose,
)

def new_deck():
    return [
        "2♠", "3♠", "4♠", "5♠", "6♠", "7♠", "8♠", "9♠", "10♠", "J♠", "Q♠", "K♠", "A♠",
        "2♦", "3♦", "4♦", "5♦", "6♦", "7♦", "8♦", "9♦", "10♦", "J♦", "Q♦", "K♦", "A♦",
        "2♥", "3♥", "4♥", "5♥", "6♥", "7♥", "8♥", "9♥", "10♥", "J♥", "Q♥", "K♥", "A♥",
        "2♣", "3♣", "4♣", "5♣", "6♣", "7♣", "8♣", "9♣", "10♣", "J♣", "Q♣", "K♣", "A♣"
    ]

def shuffle_deck(deck):
    random.shuffle(deck)

def deal_card(deck):
    return deck.pop()

def hand_value(cards):
    total = 0
    ace = False
    for card in cards:
        if card[0] in "JQK":
            total += 10
        elif card[0] == "A":
            ace = True
        else:
            total += int(card[:-1])
    if ace:
        if total + 11 <= 21:
            total += 11
        else:
            total += 1
    return total


def print_game_state(player_hand, dealer_hand):
    os.system("clear")
    print(logo)
    
    if(len(dealer_hand) == 1):
        print(f"Dealer Showing: {hand_value(dealer_hand)}")
        print(concatenate_cards(get_card(dealer_hand[0]), card_back()))
    else:
        print(f"Dealer: {hand_value(dealer_hand)}")
        print(concatenate_cards(*[get_card(card) for card in dealer_hand]))
    print(f"Player: {hand_value(player_hand)}")
    print(concatenate_cards(*[get_card(card) for card in player_hand]))
    


def game_loop():
    deck = new_deck()
    shuffle_deck(deck)
    dealer_hand = []
    player_hand = []
    
    # Starting hands
    dealer_hand.append(deal_card(deck))
    player_hand.append(deal_card(deck))
    player_hand.append(deal_card(deck))
    print_game_state(player_hand=player_hand, dealer_hand=dealer_hand)
    
    while hand_value(player_hand) < 21:
        action = input("Do you want to hit or stand? ").lower()
        if action == "hit":
            player_hand.append(deal_card(deck))
            print_game_state(player_hand=player_hand, dealer_hand=dealer_hand)
        elif action == "stand":
            break
        else:
            print("Invalid action, please type 'hit' or 'stand'.")
            
    if hand_value(player_hand) > 21:
        print_game_state(player_hand=player_hand, dealer_hand=dealer_hand)
        print(bust)
    else:
        while hand_value(dealer_hand) < 17:
            dealer_hand.append(deal_card(deck))
            print_game_state(player_hand=player_hand, dealer_hand=dealer_hand)            
        if hand_value(dealer_hand) > 21:
            print_game_state(player_hand=player_hand, dealer_hand=dealer_hand)
            print(win)
            print("Dealer busts! You win!")
        elif hand_value(dealer_hand) > hand_value(player_hand):
            print_game_state(player_hand=player_hand, dealer_hand=dealer_hand)
            print(lose)
            print("Dealer wins!")
        elif hand_value(dealer_hand) < hand_value(player_hand):
            print_game_state(player_hand=player_hand, dealer_hand=dealer_hand)
            print(win)
            print("You win!")
        else:
            print_game_state(player_hand=player_hand, dealer_hand=dealer_hand)
            print("It's a tie!")
    
    if(input("Do you want to play again? (yes or no): ").lower() == "yes"):
        game_loop()
    else:
        print("Thanks for playing!")
        return
    
    
game_loop()

