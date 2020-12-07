import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True

class Card:
    
    def __init__(self, suit, rank):
        self.suit=suit
        self.rank=rank
        self.value=values[rank]
    
    def __str__(self):
        return f"{self.suit} of {self.rank}"

class Deck:
    
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                created_card=Card(suit,rank)
                self.deck.append(created_card)
    
    def __str__(self):
        deck_list=''
        for card in self.deck:
            deck_list+= '\n ' + card.__str__()
        return f"Deck has {len(self.deck)} cards." + deck_list

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        card_taken=self.deck.pop()
        return card_taken

class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        
        self.cards.append(card)
        self.value+=card.value
    
    def adjust_for_ace(self):
        aces='wrong'
        acceptable=[1,11]
        while aces not in acceptable:
            try: 
                aces=int(input("What shoud the value of Ace be? 1 or 11?"))
            except:
                print("Please choose only 1 or 11.")
            else:
                
                if aces not in acceptable:
                    print("Please choose only 1 or 11.")
                if aces in acceptable:
                    
                    print(f"Value of ace is {aces}")
                    break
        self.aces=aces
    
    def __str__(self):
        hand_list=' '
        for i in self.cards:
            hand_list += "\n " + i.__str__() 
        return hand_list 

class Chips:
    
    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        self.total+=self.bet
        
    
    def lose_bet(self):
        self.total-=self.bet

def take_bet(Chips):
    
    while True:
        try:
            bet=int(input("How much do you wanna bet?")) 
        except:
            print("Please bet with value of money.")
        else:
            if bet <= Chips.total:
                Chips.bet=bet
                return f"Alright. You bet ${Chips.bet} for this round."
                
               
            
            else:
                print (f"Sorry, you don't have enough money to bet that much. Currentyly, you have ${Chips.total}. Try betting a lower amount.")


def hit(deck,hand):
    if hand.value >= 21:
        return "Sorry, you cannot hit as your values in Hand already reaches 21."
    else:
        hand.add_card(deck.deal())
         
def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop
    
    hitme='wrong'
    acceptable=['Y','N','y','n']
    while hit not in acceptable:
        try:
            hitme=input("Do you want to hit from deck(Y or N)? If not, you will stand.")
            hitme=hitme.upper()
        except:
            print("Please choose Y or N.")
        else:
            if hitme=='Y':
                
                hit(deck,hand)
                
            else:
                playing=False
        break

def show_some(player,dealer):
    print("___________________________")
    print("Dealer's Hand:\n")
    for i,o in enumerate(dealer.cards):
        if i ==0:
            print(" <Hidden Card>")
        else:
            print(f" {o}")
    #print(f" Total values: {dealer.value}")
    print("\n")
    print("Player's Hand:")
    print(player)
    print(f" Total values: {player.value}")
    print("___________________________")
    
def show_all(player,dealer):
    print("___________________________")
    print("Dealer's Hand:")
    print(dealer)
    print(f" Total values: {dealer.value}")
    print("\n")
    print("Player's Hand:")
    print(player)
    print(f" Total values: {player.value}")
    print("___________________________")
    
def player_busts(Chips):
    print("Player busts! Dealer wins!")
    Chips.lose_bet()

def player_wins(Chips):
    print("Player's sum in hand is nearer to 21. Congratulations! Player wins!")
    Chips.win_bet()

def dealer_busts(Chips):
    print("Dealer busts! Congratulations, player wins!")
    Chips.win_bet()
    
def dealer_wins(Chips):
    print("Dealer's sum in hand is nearer to 21. Whoops! Dealer wins!")
    Chips.lose_bet()
    
def push():
    print("Ties!")

def blackjack():
    
    playing=True
    # Set up the Player's chips
    pchips=Chips()
    
    while True:
        # Print an opening statement
        print("Welcome to BLACKJACK! Let's play!")

        # Create & shuffle the deck, deal two cards to each player
        deck=Deck()
        deck.shuffle()
        dealer=Hand()
        player=Hand()

        for i in range(2):
            dealer.add_card(deck.deal())
            player.add_card(deck.deal())
        print (f"You have ${pchips.total}.")
        # Prompt the Player for their bet
        take_bet(pchips)

        

        while playing:  
            # Show cards (but keep one dealer card hidden)
            show_some(player,dealer)
            # Prompt for Player to Hit or Stand
            hit_or_stand(deck,player)

            # Show cards (but keep one dealer card hidden)
            #show_some(dealer,player) 

            # If player's hand exceeds 21, run player_busts() and break out of loop
            if player.value > 21:
                show_some(player,dealer)
                player_busts(pchips)
                busted=True
            else:
                busted=False
                
            if busted==False:
            # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
                
                r=random.randint(0,1)
                if r==1:
                    hit(deck, dealer)
                else:
                    pass

                # Show all cards
                show_all(player,dealer)

                # Run different winning scenarios
                if player.value > 21:
                    player_busts(pchips)
                elif dealer.value > 21:
                    dealer_busts(pchips)
                elif dealer.value > player.value:
                    dealer_wins(pchips)
                elif player.value > dealer.value:
                    player_wins(pchips)
                else:
                    push()

        # Inform Player of their chips total 
            print(f"You have ${pchips.total}.")

        # Ask to play again
            again='wrong'
            acceptable=['Y','N','y','n']

            while again not in acceptable:
                try: 
                    again=input("Wanna play another hand (Y or N)").upper()
                    
                except:
                    print("Y to play again, N to quit.")
            
            if again=='Y':
                print("Okay! Next round!")
                playing=True
                # Create & shuffle the deck, deal two cards to each player
                deck=Deck()
                deck.shuffle()
                dealer=Hand()
                player=Hand()

                for i in range(2):
                    dealer.add_card(deck.deal())
                    player.add_card(deck.deal())

                # Prompt the Player for their bet
                take_bet(pchips)
                
            else:
                print("See you again!")
                playing=False
                break       
        break

if __name__ == '__main__':
	blackjack() #test Play!

