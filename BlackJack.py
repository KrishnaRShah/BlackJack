import random
from PIL import Image                                                                                


Deck = [2,3,4,5,6,7,8,9,10,11,12,13,14]*8

def deal(Deck):
    Hand = []
    for i in range(2):
        random.shuffle(Deck)
        Card = Deck.pop()
        if Card == 11:Card = "J"
        if Card == 12:Card = "Q"
        if Card == 13:Card = "K"
        if Card == 14:Card = "A"
        Hand.append(Card)
    return Hand
        
def total(HandTotal):
    Total = 0
    TotalCards = len(HandTotal)
    for i in range(TotalCards):
        Value = HandTotal[i]
        if Value == 1 or Value == 2 or  Value == 3 or Value == 4 or  Value == 5 or  Value == 6 or  Value == 7 or  Value == 8 or  Value == 9 or  Value == 10:
            Total+= Value
        if Value == "J" or Value == "Q" or Value == "K":
	        Total+= 10
        elif Value == "A":
	        Total+= 11
    return Total

def Hit(PlayerHand):
    random.shuffle(Deck)
    Card = Deck.pop()
    if Card == 11:Card = "J"
    if Card == 12:Card = "Q"
    if Card == 13:Card = "K"
    if Card == 14:Card = "A"
    PlayerHand.append(Card)
    return PlayerHand

def Split(PlayerHand):
    Hand1 = []
    Hand2 = []

    Hand1.append(PlayerHand[0])
    Hand2.append(PlayerHand[1])

    PlayerHand = Hand1
    PlayerHand = Hit(PlayerHand)
    Hand1 = PlayerHand

    PlayerHand = Hand2
    PlayerHand = Hit(PlayerHand)
    Hand2 = PlayerHand

    return Hand1, Hand2

def SplitHit(Hand1,Hand2):
    PlayerHand = Hand1
    while total(PlayerHand) < 21:
        Choice = input("Would You Like to Hit(H) or Stand(S) for your first Hand: ")
        print("")
        Choice = Choice.upper()

        if Choice == "H":

            PlayerHand = Hit(PlayerHand)
            print("Your first Hand is now: ", PlayerHand, "Your new Total is: ", total(PlayerHand))
            print("")

            PlayerTotal = total(PlayerHand)

            if total(PlayerHand) == 21:
                #print("Blackjack! You won this hand!")
                break

            if total(PlayerHand) > 21:
                #print("Bust!, Dealer Wins this hand")
                print("")
                break
        if Choice == "S":
            Hand1 = PlayerHand
            break
    Hand1Total = total(PlayerHand)
    Hand1 = PlayerHand

    PlayerHand = Hand2
    while total(PlayerHand) < 21:
        Choice = input("Would You Like to Hit(H) or Stand(S) for your second Hand: ")
        print("")
        Choice = Choice.upper()

        if Choice == "H":

            PlayerHand = Hit(PlayerHand)
            print("Your second Hand is now: ", PlayerHand, "Your new Total is: ", total(PlayerHand))

            PlayerTotal = total(PlayerHand)

            if total(PlayerHand) == 21:
                #print("Blackjack! You won this hand!")
                break

            if total(PlayerHand) > 21:
                #print("Bust!, Dealer Wins this hand")
                break
        if Choice == "S":
            Hand2 = PlayerHand
            break
    Hand2Total = total(PlayerHand)
    Hand2 = PlayerHand
    return Hand1, Hand2, Hand1Total, Hand2Total

def RegularHit(PlayerHand):

    while total(PlayerHand) < 21:

        Choice = input("Would You Like to Hit(H) or Stand(S): ")
        print("")
        Choice = Choice.upper()

        if Choice == "H":

            PlayerHand = Hit(PlayerHand)
            print("Your Hand is now: ", PlayerHand, "Your new Total is: ", total(PlayerHand))

            PlayerTotal = total(PlayerHand)

            if total(PlayerHand) == 21:
               # print("BlackJack!, You are the winner!")
                print("")
                
            if total(PlayerHand) > 21:
                #print("Bust!, Dealer Wins")
                print("")
               
        if Choice == "S":
            return PlayerHand
    return PlayerHand

def DealerHit(DealerHand):

    print("The Dealer's hand is :", DealerHand, "for a total of:", total(DealerHand))
    
    if total(DealerHand) == 21:
        print("Blackjack! Dealer Wins")

    while total(DealerHand) < 17:

        DealerHand = Hit(DealerHand)

        if total(DealerHand) > 21:
            print("The Dealer's Hand is now:", DealerHand, "for a total of", total(DealerHand))
            #print("Bust!, The Dealer Went too High, Player WINS!")
            break
            
        if total(DealerHand) == 21:
            print("The Dealer's Hand is now:", DealerHand, "for a total of", total(DealerHand))
            #print("Blackjack! Dealer Wins")
            
        DealerTotal = total(DealerHand)

    DealerTotal = total(DealerHand)
    return DealerHand, DealerTotal

def ProbTable():

    Choice = input("Would You Like to view the strategy table?(Y/N) ")
    print("")
    Choice = Choice.upper()

    if Choice == 'Y':
        img = Image.open("BlackJackProb.png")
        img.show()

    if Choice == 'N':
        return
    return   

def BlackJack():

    ProbTable()

    running = True
    while running:

        PlayerHand = deal(Deck)
        DealerHand = deal(Deck)

        HandTotal = PlayerHand
        PlayerTotal = total(HandTotal) 
        HandTotal = DealerHand
        DealerTotal = total(HandTotal)
        
        SingleHand = True

        print("Your hand is :", PlayerHand, "for a total of:",PlayerTotal)
        print("The dealer's hand is: [",DealerHand[0],", ? ]")
        print("")

        if PlayerTotal == 21:
            print("Blackjack! Player Wins")
            

        if PlayerHand[0] == PlayerHand[1]:
            SplitChoice = input("Would you like to split(Y/N?")
            print("")
            SplitChoice = SplitChoice.upper()

            if SplitChoice == 'Y':
                Hand1, Hand2 = Split(PlayerHand)
                print("Your first Hand is:", Hand1)
                print("Your second Hand is:", Hand2)
                print("")

                Hand1,Hand2,Hand1Total,Hand2Total = SplitHit(Hand1,Hand2)
                
                print("Your first Hand is:", Hand1, "for a total of:", Hand1Total)
                print("Your second Hand is:", Hand2, "for a total of:", Hand2Total)
                print("")
                
                SingleHand = False

            if SplitChoice == 'N':
                SingleHand = True
                print("")
        
        OriginalDealerTotal = total(DealerHand)

        if PlayerTotal < 21 and SingleHand == True:
            PlayerHand = RegularHit(PlayerHand)

        DealerHand,DealerTotal = DealerHit(DealerHand)

        if DealerTotal < 21 and OriginalDealerTotal != total(DealerHand):
            print("The Dealer's Hand is now:", DealerHand, "for a total of", total(DealerHand))
        print("")

        while SingleHand == True:

            if total(PlayerHand) > 21:
                print("The Dealer is the winner!")
                break
            
            if total(DealerHand) > 21:
                print("You are the winner!")
                break

            if total(DealerHand) <= 21 and total(PlayerHand) <= 21:
                if total(PlayerHand) == total(DealerHand):
                    print("Bet's Returned")
                    break   
                if total(PlayerHand) > total(DealerHand):
                    print("You are the winner!")
                    break
                if total(DealerHand) > total(PlayerHand):
                    print("The Dealer wins!")
                    break

        while SingleHand == False:

            if Hand1Total > 21:
                print("The Dealer Win's the first hand!")
        
            if total(DealerHand) > 21 and Hand1Total <= 21:
                print("You are the winner of the first hand!")
                
            if total(DealerHand) <= 21 and (Hand1Total <= 21 or Hand2Total <= 21):
                if total(DealerHand) > Hand1Total:
                    print("The Dealer is the winner of the first hand!")
                if total(DealerHand) < Hand1Total and Hand1Total <= 21:
                    print("You are the winner of the first hand!")
                if total(DealerHand) == Hand1Total:
                    print("Bet's Returned for First Hand")
                if total(DealerHand) > Hand2Total:
                    print("The Dealer is the winner of the second hand!")
                if total(DealerHand) < Hand2Total and Hand2Total <= 21:
                    print("You are the winner of the second hand!")
                if total(DealerHand) == Hand2Total:
                    print("Bet's Returned for Second Hand")

            if Hand2Total > 21:
                print("The Dealer Win's the second hand!")
            
            if total(DealerHand) > 21 and Hand2Total <= 21:
                print("You are the winner of the second hand!")
                
            print("")
            SingleHand = True
    
        GameChoice = input("Would you like to play again?(Y/N?")
        print("")
        GameChoice = GameChoice.upper()

        if GameChoice == 'Y':
            running = True
            
        if GameChoice == 'N':
            running = False


if __name__ == "__main__":
    BlackJack()

