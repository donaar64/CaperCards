import os
from colorama import Fore
from colorama import Back
from colorama import Style

global playedCards
global Score
global risk
global Reward
playedCards=[]
class CrewCard:
    def __init__(self,name, number, ability):
        self.name = name
        self.number = number
        self.ability=ability
       


    def __str__(self):
     return f"\n{self.name}\nValue: {self.number}\nAbility:{self.ability}\n"
    def __repr__(self):
     return f"\n{self.name}\nValue: {self.number}\nAbility:{self.ability}\n"
class Spade(CrewCard):
    pass
class Heart(CrewCard):
    pass
class Club(CrewCard):
    def __init__(self,name, number, ability):
        self.name = name
        self.number = number
        self.ability=ability
        self.activated = False 
    def __str__(self):
     if self.activated == True:
      return f"\n{self.name}\nValue: {self.number}\nAbility:{self.ability}\n"+Back.RED+"Replaced Risk\n" +Back.RESET
     else: 
        return f"\n{self.name}\nValue: {self.number}\nAbility:{self.ability}\n"
    def __repr__(self):
     if self.activated == True:
      return f"\n{self.name}\nValue: {self.number}\nAbility:{self.ability}\n"+Back.RED+"Replaced Risk\n" +Back.RESET 
     else: 
        return f"\n{self.name}\nValue: {self.number}\nAbility:{self.ability}\n"



class Diamond(CrewCard):
       def __init__(self,name, number, ability,altValue,):
        self.name = name
        self.number = number
        self.ability=ability
        self.altValue= altValue
        self.OGNumber = number
        self.OGAlt = altValue

       
        
       def Rotate(self):
            backup= self.number
            self.number= self.altValue
            self.altValue= backup

       
       def UnRotate(self):
            self.number=self.OGNumber
            self.altValue = self.OGAlt
           
FCG= Club(Fore.YELLOW+"FCG"+chr(9831)+Fore.RESET,2, "Rotate a diamond", )
FCG2= Club(Fore.YELLOW+"FCG"+chr(9831)+Fore.RESET, 2,"Rotate a diamond",)
FCG3= Club(Fore.YELLOW+"FCG"+chr(9831)+Fore.RESET,2, "Rotate a diamond",)
Orym=Heart(Style.DIM+Fore.GREEN+"Orym"+chr(9825)+Fore.RESET+ Style.NORMAL,3,"+1 for each other heart in play")
Orym2=Heart(Style.DIM+Fore.GREEN+"Orym"+chr(9825)+Fore.RESET+Style.NORMAL,3,"+1 for each other heart in play")
Orym3=Heart(Style.DIM+Fore.GREEN+"Orym"+chr(9825)+Fore.RESET+Style.NORMAL,3,"+1 for each other heart in play")
Fearne=Spade(Style.DIM+Fore.YELLOW+"Fearne"+chr(9828)+Fore.RESET+Style.NORMAL,4,"Peek at the reward")
Fearne2=Spade(Style.DIM+Fore.YELLOW+"Fearne"+chr(9828)+Fore.RESET+Style.NORMAL,4,"Peek at the reward")
Fearne3=Spade(Style.DIM+Fore.YELLOW+"Fearne"+chr(9828)+Fore.RESET+Style.NORMAL,4,"Peek at the reward")
Dorian= Heart(Fore.CYAN+"Dorian"+chr(9825)+Fore.RESET,5,"-1 for each spade in play")
Dorian2= Heart(Fore.CYAN+"Dorian"+chr(9825)+Fore.RESET,5,"-1 for each spade in play")
Dorian3= Heart(Fore.CYAN+"Dorian"+chr(9825)+Fore.RESET,5,"-1 for each spade in play")
Chetney= Diamond(Style.DIM+Fore.CYAN+"Chetney"+chr(9826)+Fore.RESET+Style.NORMAL,6,"Can be played as a 6 or a 9",9)
Chetney2= Diamond(Style.DIM+Fore.CYAN+"Chetney"+chr(9826)+Fore.RESET+Style.NORMAL,6,"Can be played as a 6 or a 9",9)
Chetney3= Diamond(Style.DIM+Fore.CYAN+"Chetney"+chr(9826)+Fore.RESET+Style.NORMAL,6,"Can be played as a 6 or a 9",9)
Ashton=Spade(Fore.BLACK+"Ashton"+chr(9828)+Fore.RESET,7,"Must discard another ODD crew from play")
Ashton2=Spade(Fore.BLACK+"Ashton"+chr(9828)+Fore.RESET,7,"Must discard another ODD crew from play")
Ashton3=Spade(Fore.BLACK+"Ashton"+chr(9828)+Fore.RESET,7,"Must discard another ODD crew from play")
Imogen= Club(Fore.MAGENTA+"Imogen"+chr(9831)+Fore.RESET,8,"May replace risk instead of joing crew",)
Imogen3= Club(Fore.MAGENTA+"Imogen"+chr(9831)+Fore.RESET,8,"May replace risk instead of joing crew",)
Imogen2= Club(Fore.MAGENTA+"Imogen"+chr(9831)+Fore.RESET,8,"May replace risk instead of joing crew",)
Laudna = Diamond(Fore.RED+"Laudna"+chr(9826)+Fore.RESET,10,"Must be played as 10",1)
Laudna2 = Diamond(Fore.RED+"Laudna"+chr(9826)+Fore.RESET,10,"Must be played as 10",1)
Laudna3 = Diamond(Fore.RED+"Laudna"+chr(9826)+Fore.RESET,10,"Must be played as 10",1)
Crew_deck=[FCG, Orym, Fearne,Dorian,Chetney,Ashton, Imogen,Laudna,FCG2, Orym2, Fearne2,Dorian2,Chetney2,Ashton2, Imogen2,Laudna2,FCG3, Orym3, Fearne3,Dorian3,Chetney3,Ashton3, Imogen3,Laudna3]


class RewardCard:
    def __init__(self,name, risk, complication):
        self.name = name
        self.risk = risk
        self.complication= complication



    def __str__(self):
        return f"\n{self.name}\nRisk: {self.risk}\nComplication:{self.complication}\n"

    def __repr__(self):
        return f"\n{self.name}\nRisk: {self.risk}\nComplication:{self.complication}\n"
GB=RewardCard(Fore.BLACK+"Gloomscale Breastplate"+Fore.RESET,5,"-4 if no spades are in play")
WL=RewardCard(Fore.GREEN+"Weave Lens"+Fore.RESET,8,"The crew loses ties")
SM=RewardCard(Fore.RED+"Sashimi Marionette"+Fore.RESET,5, "-2 to score per diamond in play")
CHE = RewardCard(Fore.CYAN+"Circle of the Hidden Eye"+Fore.RESET,6,"Discard all duplicate crew before scoring")
JVC = RewardCard(Fore.BLUE+"Journal of Vespin Chloras"+Fore.RESET,7,"+2 to crew score per club in play")
GS = RewardCard(Fore.MAGENTA+"Gnarlrock Shard"+Fore.RESET,7,"Rotate all diamonds in play before scoring")
MB = RewardCard(Style.DIM+Fore.GREEN+"Message Bloom"+Fore.RESET+Style.NORMAL,7, "+1 to crew score per even card if a heart is in play")
HM = RewardCard(Style.DIM+Fore.CYAN+"Hishari Mask"+Fore.RESET+Style.NORMAL, 5, "Discard all crew with lowest number before scoring")
CC = RewardCard(Fore.YELLOW+"Changebringer Coin"+Fore.RESET,6,"+1 to crew score per odd crew in play")
RewardDeck=[GB,WL,SM,CHE,JVC,GS,MB,HM,CC]
def Clear():
    os.system('cls' if os.name == 'nt' else 'clear')
def Draw_cards(deck, picks, list):  
    import random
    Draws=0
    for x in range(picks):
        max_index = len(deck) - 1
        random_number = (random.randint(0, max_index))
        list.append(deck[random_number])
        del deck[random_number]
        Draws=Draws+1

        if len(deck) <= 0 or Draws >= picks:
            break
def play(card):
    global Score
    global risk
    global Reward
    global PutDown
    global DiscardedCards
    if card == Imogen or card == Imogen2 or card == Imogen3:
        for x in playedCards:
            try: 
                if x.activated == True:
                 print(Fore.MAGENTA+"Imogen is already activated"+Fore.RESET)
                 playedCards.append(card)
                 input("Press Enter to Continue")
                 return()
            except: AttributeError
        Answer=input(Fore.MAGENTA+'Do you want this to replace the risk'+Fore.RESET+'(y or n)')
        if Answer == "yes"or Answer=="y" or Answer == "Y":
         risk = 8
         card.activated = True
    elif card == Ashton or card == Ashton2 or card==Ashton3:
         print(Fore.BLACK+"Choices"+Fore.RESET)
         choices = 0
         for x in playedCards:
            if (x.number % 2) != 0:
                print(playedCards.index(x),x.name)
                choices += 1
         if choices == 0:
              print("None")
              playedCards.append(card)
              input("Press Enter to Continue")
              return
         Answer=eval(input('Which card do you want to discard(enter number):'))
         if playedCards[Answer] in playedCards:
            DiscardedCards.append(playedCards[Answer])
            PutDown.remove(playedCards[Answer])
            playedCards.remove(playedCards[Answer])      
    elif card == Chetney or card == Chetney3 or card == Chetney2:
        Answer= eval(input(Style.DIM+Fore.CYAN+'What do you want Chetneys value to be?\n'+Style.NORMAL+Fore.RESET))
        if Answer == 6:
            pass
        if Answer == 9:
              card.Rotate()
    elif card == FCG or card == FCG2 or card == FCG3:
        print(Fore.YELLOW+"Choices"+Fore.RESET)
        choices = 0
        for x in playedCards:
             if type(x) == Diamond:
                print(playedCards.index(x),x.name)
                choices += 1
        if choices == 0:
             print("None")
             playedCards.append(card)
             input("Press Enter to Continue")
             return
        Answer=eval(input('Who do you want to rotate(enter number):'))
        if playedCards[Answer] in playedCards and type(playedCards[Answer]) == Diamond:
                playedCards[Answer].Rotate()
    elif card == Fearne or card == Fearne2 or card == Fearne3:
        print(Style.DIM+Fore.YELLOW+"\nReward"+Style.NORMAL +Fore.RESET,Reward[0])
        input("Press Enter to Continue")
    playedCards.append(card)

       
def CheckCards(Deck,card,checkedDeck,Suit):
        global instances
        global CardInstances
        instances = 0
        CardInstances = 0
        for x in Deck:
         if x.name == card.name: 
            for z in checkedDeck:
                if type(z) == Suit:
                    instances +=1
            CardInstances +=1
def DiscardDupes(Card,Deck):
    global DiscardedCards
    instances = 0
    for x in Deck:
        if Card.name == x.name :
            instances += 1
    if instances >= 2:
         for x in reversed(Deck):
             if Card.name == x.name :
                 print(x.name,("was discarded"))
                 DiscardedCards.append(x)
                 Deck.remove(x)
                 
             
def ScoreCards():
    global Score
    global playedCards
    global risk
    global Target
    global Reward
    global DiscardedCards
    Clear()
    Score = 0

    if len(riskDeck)>0 :
     for i in riskDeck: 
        if i == HM: # these are all of the complications that happen before scoring
            CardNumbers = []
            for x in playedCards:
             CardNumbers.append(x.number)
            LowestNumber = min(CardNumbers)
            for x in reversed(playedCards):
             if x.number == LowestNumber:
                print(x.name,"was discarded")
                DiscardedCards.append(x)
                playedCards.remove(x)
                
        elif i == GS:
            for x in playedCards:
                if type(x) == Diamond:
                    x.Rotate()
                    print(x.name,"was rotated")
        elif i == CHE:
            allNames = [Imogen,Chetney, FCG, Orym, Dorian, Laudna, Fearne,Ashton]
            for x in allNames:
                DiscardDupes(x,playedCards)

    CheckCards(playedCards,Orym,playedCards,Heart)
    if CardInstances >0:
     Score += (instances-CardInstances)
    CheckCards(playedCards,Dorian, playedCards,Spade)
    if CardInstances >0:
     Score-=(instances)
    if len(riskDeck)>0:
     CheckCards(riskDeck,JVC,playedCards,Club)
     if CardInstances >0:
      Score += 2*(instances)
     CheckCards(riskDeck,SM,playedCards,Diamond)
     if CardInstances >0:
      Score -= 2*(instances)
     CheckCards(riskDeck,GB,playedCards,Spade)
     if CardInstances >0:
         if instances == 0:
            Score -= 4
     CheckCards(riskDeck,MB,playedCards,Heart)
     if CardInstances >0:# this sees if there are any hearts and then adds one point for every even crew if there is a heart
         if instances >0 :
           ListPosition = 0
           for x in range(len(playedCards)):
            if (playedCards[ListPosition].number % 2) == 0:
                Score += 1
            ListPosition += 1 
     CheckCards(riskDeck,CC,playedCards,Heart)  
     if CardInstances > 0:
         for x in playedCards:
            if (x.number % 2) != 0:
                Score += 1
     CheckCards(riskDeck,WL,playedCards,Heart) #tallies up the score but you lose if there was a tie, determines if you won or lost, and then displays appropriate message
     if CardInstances >0 :
        Target = risk + Reward[0].risk
        for x in playedCards: 
            if x.name == Imogen.name and x.activated == True: 
                pass
            else:
                Score += x.number
        if Score <= Target or Score>21:
              print(Back.LIGHTBLACK_EX+"\nGame Over"+Back.RESET)
              print("\nYour Score was",Score)
              if Score < Target:
               print("\nYour reward was the",Reward[0].name, "and the score to beat was",Target)
              if Score > 21:
                  print("\nYou made too much noise.Your Reward was the",Reward[0].name,"and the score to beat was",Target,"\n")
              if len(riskDeck)>0:
                print ("\nYour Final Loot was:")
                for x in riskDeck:
                    print (x)
              print(Back.GREEN+"\nCards Played in this round"+Back.RESET)
              for x in playedCards:
                    print(x)
              if len(DiscardedCards)>0:
                print (Back.LIGHTBLACK_EX+"\nCards Discarded this Round:"+Back.RESET)
                for x in DiscardedCards:
                    print (x)      
              print ("You won", len(riskDeck), "Rounds")
              exit()
        elif Score == Target and Score <= 21:
                if len(riskDeck)== 4:
                 print(Back.BLUE+"\nYou won the game"+Back.RESET)
                 print("\nYour Score was", Score)
                 print("\nThe score to beat was",Target)
                 if len(riskDeck)>0:
                  print ("\nYour Final Loot was:",Reward[0])
                  for x in riskDeck:
                    print (x)
                 print(Back.GREEN+"\nCards Played in this round"+Back.RESET)
                 for x in playedCards:
                    print(x)
                 if len(DiscardedCards)>0:
                  print (Back.LIGHTBLACK_EX+"\nCards Discarded this Round:"+Back.RESET)
                  for x in DiscardedCards:
                    print (x)   
                 print("Thank You for Playing")
                 exit()
                else:
                    print(Back.BLUE+"You won the round"+Back.RESET)
                    print("\nYour Score was",Score)
                    print("\nYour reward was the", Reward[0].name, "and the score to beat was",Target)
                    if len(riskDeck)>0:
                     print(Back.RED+"Your Complications were:\n"+Back.RESET)
                     for x in riskDeck:
                        print (x.complication)
                    print(Back.GREEN+"\nCards Played in this round:"+Back.RESET)
                    for x in playedCards:
                     print(x)
                    if len(DiscardedCards)>0:
                     print (Back.LIGHTBLACK_EX+"\nCards Discarded this Round:"+Back.RESET)
                     for x in DiscardedCards:
                      print (x)
                    print("You have",4-len(riskDeck),"rounds left to go")
                    input("Press Enter to Continue")
                    return()
    Target = risk + Reward[0].risk
    for x in playedCards: #tallies up the score, determines if you won or lost, and then displays appropriate message
            if x.name == Imogen.name and x.activated == True: 
                pass
            else:
                Score += x.number
    if Score < Target or Score>21:
              print(Back.LIGHTBLACK_EX+"\nGame Over"+Back.RESET)
              print("\nYour Score was",Score)
              if Score < Target:
               print("\nYour reward was the",Reward[0].name, "and the score to beat was",Target)
              if Score > 21:
                  print("\nYou made too much noise.Your Reward was the",Reward[0].name,"and the score to beat was",Target,"\n")
              print ("\nYour Final Loot was:")
              if len(riskDeck)>0:
                for x in riskDeck:
                    print (x)
              print(Back.GREEN+"\nCards Played in this round"+Back.RESET)
              for x in playedCards:
                     print(x)
              if len(DiscardedCards)>0:
                     print (Back.LIGHTBLACK_EX+"\nCards Discarded this Round:"+Back.RESET)
                     for x in DiscardedCards:
                      print (x)
              print ("You won", len(riskDeck), "Rounds")
              exit()
    elif Score >= Target and Score <= 21:
                if len(riskDeck)== 4:
                 print(Back.BLUE+"\nYou won the game"+Back.RESET)
                 print("\nYour Score was", Score)
                 print("\nThe score to beat was",Target)
                 if len(riskDeck)>0:
                  print ("\nYour Final Loot was:",Reward[0])
                 if len(riskDeck)>0:
                  for x in riskDeck:
                    print (x)
                 print(Back.GREEN+"\nCards Played in this round"+Back.RESET)
                 for x in playedCards:
                     print(x)
                 if len(DiscardedCards)>0:
                     print (Back.LIGHTBLACK_EX+"\nCards Discarded this Round:"+Back.RESET)
                     for x in DiscardedCards:
                      print (x)
                 print("Thank You for Playing")
                 exit()
                else:
                    print(Back.BLUE+"You won the round"+Back.RESET)
                    print("\nYour Score was",Score)
                    print("\nYour reward was the", Reward[0].name, "and the score to beat was",Target)
                    if len(riskDeck)>0:
                     print(Back.RED+"\nYour Complications were:\n"+Back.RESET)
                     for x in riskDeck:
                        print (x.complication)
                    print(Back.GREEN+"\nCards Played in this round"+Back.RESET)
                    for x in playedCards:
                     print(x)
                    if len(DiscardedCards)>0:
                     print (Back.LIGHTBLACK_EX+"\nCards Discarded this Round:"+Back.RESET)
                     for x in DiscardedCards:
                      print (x)
                    print("You have",4-len(riskDeck),"rounds left to go")
                    input("Press Enter to Continue")
                    return()

def playRound():
  global PutDown
  global RDC
  global CDC
  global Hand
  global Reward
  global riskDeck
  global playedCards
  global risk
  global truerisk
  global DiscardedCards
  Clear()
  playedCards = []
  PutDown = []
  risk = truerisk
  DiscardedCards= []

  y=0
  Draw_cards(RDC,1,Reward)
  Draw_cards(CDC,2,Hand)
  for x in range(2):
    Draw_cards(CDC,1,PutDown)
    input(Back.GREEN+"\nPlay card from Deck"+Back.RESET +"\nPress enter to continue")
    Clear()   
    print(Back.GREEN+"Played Cards:"+Back.RESET)
    for x in PutDown:
         print (x)
    if len(riskDeck)>0:
        print(Back.RED+"Your Complications are:"+Back.RESET)
        for x in riskDeck:
          print (x.complication,"\n")          
    print(Back.GREEN+"Hand:\n"+Back.RESET)
    for z in Hand:
        print(Hand.index(z),z) 
    print(Back.BLUE+"\n"+"Play Effect:"+Back.RESET+"\n"+PutDown[y-len(DiscardedCards)].ability)            
    play(PutDown[y-len(DiscardedCards)])
    Clear()     
    print(Back.GREEN+"Played Cards"+Back.RESET)
    for x in playedCards:
         print (x)
    if len(riskDeck)>0:
        print(Back.RED+"Your Complications are:"+Back.RESET)
        for x in riskDeck:
          print(x.complication,"\n")     
    print(Back.GREEN+"\nHand"+Back.RESET)
    for z in Hand:
        print(Hand.index(z),z) 

    PlayedCard = eval(input("Who will you play(enter number)"))
    print(Back.BLUE+"\n"+"Play Effect:"+Back.RESET+"\n"+Hand[PlayedCard].ability)  
    play(Hand[PlayedCard])
    PutDown.append(Hand[PlayedCard])
    Hand.remove(Hand[PlayedCard])
    Clear()
    y=2
  ScoreCards()
  riskDeck.append(Reward[0]) 
  Reward = []    
              

            



 
            
                       
    
risk = 0
while risk != 11 and risk != 12:
 Clear()
 risk = eval(input(Fore.RED+"Do you want the risk to be 11 or 12? \nIf you do not know how to play type instructions"+Fore.RESET) )
 if risk == "instructions":
    print("""This is the single player version of the game so the rules for multiple players will not be mentioned
            The Game is played over 5 rounds.Each round you are building a crew to attempt a heist. If the total value of the Crew Cards you play ties or exceed the difficult of the heist- without going over 21- the heist is successful!
            The difficulty of each heist is the Risk plus the hidden Reward card. Since the Reward isn't revealed until the end you won't know exactly how difficult the heist will be.
            If you can successfully complete 4 heists in a row, you win. However if you fail even once, the game is over
            Playing a round
            You will be dealt a hand of 4 cards. The top card of the deck is played and it is treated as if you played it yourself. After that you play a card and then you play a card from the deck and then you play a final card. If you can you MUST use a cards ability
            After the 4 Crew have been played the score will be calculated and you will win or lose. You win if you tie or exceed the difficulty. The difficulty is the current risk plus the hidden reward card. You lose if you do not exceed the difficulty or if you go over 21
            After you complete heist""")
truerisk = risk
RDC = RewardDeck[:]
CDC = Crew_deck[:]
riskDeck=[]
Hand=[]
PutDown=[]
playedCards=[]
Reward = []
Draw_cards(CDC,2,Hand)
for x in range(5):
 playRound()

