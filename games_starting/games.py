import random

money = 100

#Write your game of chance functions here

def headsOrTails(choice, bet):
  toss = ''
  num = random.randint(1, 2)
  if(num ==1):
    toss = 'Heads'
  else: 
    toss = 'Tails'

  global money
  if(money < bet):
    print('You don\'t have enough cash. Maybe you should call it a night and come back tomorrow')
  elif(bet < 1):
    print('This isn\'t Monopoly, we play with real cash here.')
  elif(choice == toss): 
    money += (bet*2)
    print ("You've just won £" + str(bet*2))
  else:
    money -= bet
    print ("You've just lost £" + str(bet * -1))
  print ("Total money: £" + str(money))

def choHan(guess, bet):
  result = ''
  dice1 = random.randint(1, 6)
  dice2 = random.randint(1, 6)
  total = dice1 + dice2
  if(total%2 == 0):
    result = 'Even'
  else:
    result = 'Odd'

  global money
  if(money < bet):
    print('You don\'t have enough cash. Maybe you should call it a night and come back tomorrow')
  elif(bet < 1):
    print('This isn\'t Monopoly, we play with real cash here.')
  elif(guess == result):
    money += (bet*2)
    print ("You've just won £" + str(bet*2))
  else:
    money -= bet
    print ("You've just lost £" + str(bet * -1))
  print ("Total money: £" + str(money))

def pickACard(bet):
  player1 = random.randint(1, 13)
  player2 = random.randint(1, 13)

  global money
  if(money < bet):
    print('You don\'t have enough cash. Maybe you should call it a night and come back tomorrow')
  elif(bet < 1):
    print('This isn\'t Monopoly, we play with real cash here.')
  elif(player1 > player2):
    money += (bet*2)
    print ("You've just won £" + str(bet*2))
  elif(player1 == player2):
    print ('You got the same card! No money won or lost')
  else:
    money -= bet
    print ("You've just lost £" + str(bet * -1))
  print ("Total money: £" + str(money))


  
def roulette(guess, bet):
  
  oddOrEven = ''
  result = random.randint(1, 36)
  if(result%2 == 0):
    oddOrEven = 'Even'
  else:
    oddOrEven = 'Odd'
  
  global money
  if(money < bet):
    print('You don\'t have enough cash. Maybe you should call it a night and come back tomorrow')
  elif(bet < 1):
    print('This isn\'t Monopoly, we play with real cash here.')
  elif(type(guess) == str and guess == oddOrEven):
    money += (bet*2)
    print ("You've just won £" + str(bet*2))
    print ("The result was " + str(result) + " which is " + str(oddOrEven))
  elif(type(guess) == str and guess != oddOrEven):
    money -= bet
    print ("You've just lost £" + str(bet * -1))
    print ("The result was " + str(result) + " which is " + str(oddOrEven))
  elif(type(guess) == int and guess == result):
    money += (bet*35)
    print ("You've just won £" + str(bet*35))
    print ("The result was " + str(result) + " which is " + str(oddOrEven))
  else:
    money -= bet
    print ("You've just lost £" + str(bet * -1))
    print ("The result was " + str(result) + " which is " + str(oddOrEven))
  print ("Total money: £" + str(money))

#Call your game of chance functions here
headsOrTails('Tails', 350)
choHan('Odd', 20)
pickACard(30)
roulette('Even', -5)