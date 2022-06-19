from random import randint  
number = input( "Please enter some number: " )
randint( 1, 10 )
def guessingNumber(number):
    num=randint( 1, 10 )
    if (number>num):
        print('too big')
    elif  (number<num):
      print('too small')
    else:
      print('You are SUPER')
guessingNumber(int(number))