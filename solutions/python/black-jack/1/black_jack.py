
def value_of_card(card):
    if card == "A":
        return 1
    elif card in ["K","Q","J"]:
        return 10
    else:
        return int(card)

def higher_card(card_one, card_two):    
    if value_of_card(card_one) > value_of_card(card_two):
         return card_one
    elif value_of_card(card_one) < value_of_card(card_two):
        return card_two
    else:
        return card_one, card_two
    return higher_card
    
def value_of_ace(card_one, card_two):
    total = value_of_card(card_one) + value_of_card(card_two)
    if card_one == 'A' or card_two == "A":
        return 1
    if total + 11 <= 21:
        return 11
    else:
        return 1

def is_blackjack(card_one, card_two):
    
    if (card_one) == "A" and (card_two) in ["K","Q","J","10"]: 
        return True
    elif (card_two) == "A" and (card_one) in ["K","Q","J","10"]:
        return True
    elif value_of_card(card_one) + value_of_card(card_two) == 21:
        return True
    if value_of_card(card_one)==10 and value_of_card(card_two)=="A":
        return True
    else:
        return False

def can_split_pairs(card_one, card_two):
    if value_of_card(card_one) == value_of_card(card_two):
        return True
    else:
        return False

def can_double_down(card_one, card_two):
    total=value_of_card(card_one) + value_of_card(card_two)
    if total == 9:
        return True
    if total == 10:
        return True
    if total == 11:
        return True 
    else:
        return False
