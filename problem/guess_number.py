from random import * 
n = randint(1,10)
print("Number of guesses is limited to only 9 times: ") 
number_of_guesses = 0

while(number_of_guesses<= 9):
  guess_number = int(input("Guess the number : ")) 
  if guess_number<n :
    print("you entered lesser number please input greater number :\n") 
  elif guess_number>n :
    print("you entered greater number please input smaller number :\n") 
  else:
    print("You won!")

    print(number_of_guesses," number of guesses you took to finish")
    break

  print(f"9 - {number_of_guesses} no of guesses Left") 
  number_of_guesses = number_of_guesses + 1
if(number_of_guesses> 9): 
  print("Game Over")
