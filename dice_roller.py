import random

def main():
  dice_rolls= int(input(' How Many dice would you like to Roll? '))
  dice_size = int(input('How many sides to this muthaflippin dice?'))
  dice_sum=0
  for _ in range (0,dice_rolls):
    roll = random.randint(1,dice_size)
    if roll ==1:
      print (f"You rolled a {roll}! Critical Fail")
    elif roll ==dice_size:
      print (f"You rolled a {roll}! Great Success!")
    else:
      print (f"You rolled a {roll}")
    dice_sum+= roll
  print (f'You rolled a total of {dice_sum}')

if __name__== "__main__":
  main()