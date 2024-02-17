from colorama import init, Style
import random

count = 0
g = "0"
c =0
view= "2"

def input1():
    print("press m for mainmenu and v for viewing score")      
    name = input("Enter your name:")
    print("Hi" + " " + f"{name}" + "!!! My name is ALEXA and I am going to play with you ")
    answ1 = int(input("ARE YOU READY (1/0):"))
    if answ1 == 1 or answ1 == 0:
      match answ1:
        case 1:
          start(name)
        case 0:
          exit()
        case _:
          raise ValueError("INVALID INPUT")

def start(name):
    global g
    global c
    print(f"\t\t\t\t\t\t\t\t\t\t\t\t\tWON:{count}")
    tt = ('Snake', 'Gun', 'Water')
    a1 = random.choice(tt)
    # print(a1)
    c=a1
    print("Enter your choice:"+f"<{tt[0]}>\t"   f"<{tt[1]}>\t"   f"<{tt[2]}>")
    guess1 = input("") 
    if a1 == "Water" and guess1.capitalize() == "Snake":
        winning(name)
    elif guess1.lower()=="m":
        main1()
    elif guess1.lower()=="v":
      view()
    elif guess1 == g:
        exit()
    elif guess1.capitalize() == a1:
        print("Draw!!!!")
        print("ALEXA chose"+f"{a1}")
        start(name)
    elif a1 == "Water" and guess1.capitalize() == "Gun":
        losing(name)
    elif a1 == "Gun" and guess1.capitalize() == "Snake":
        losing(name)
    elif a1 == "Snake" and guess1.capitalize() == "Water":
        losing(name)
    elif a1 == "Gun" and guess1.capitalize() == "Water":
        winning(name)
    elif a1 == "Snake" and guess1.capitalize() == "Gun":
        winning(name)
    else:
        raise ValueError("INVALID INPUT")

def winning(name):
    global count
    global c
    print(f"{name}" + " won!!!!!!")
    print("ALEXA chose: " + f"{c}")
    count += 1
    # print(f"{name}" + " won " + f"{count}" + " times")
    with open('victory.txt','a') as f:
      f.write("\n-------------------------\n")
      f.write("\n"f"{name}" + " won!!!!!! \n")
      f.write("ALEXA chose: " + f"{c}\n")
      f.write(f"{name}" + " won " + f"{count}" + " times \n")
      f.write("\n--------------------\n")
    start(name)
    

def losing(name):
    global c
    print("ALEXA chose: " + f"{c}")
    print("ALEXA won!!!!!!")
    with open('victory.txt','a') as f:
      f.write("\n-------------------------\n")
      f.write("\n"f"{name}" + " won!!!!!! \n")
      f.write("ALEXA chose: " + f"{c}\n")
      f.write(f"{name}" + " won " + f"{count}" + " times \n")
      f.write("\n--------------------\n")
    start(name)
    
  
def view():
  try:
      with open('victory.txt', 'r') as f:
          content = f.read()  # Read the content of the file
          print(content)  # Print the content
      input("Press any key to continue:")
      main1() 
  except Exception as e:  # Catch any exception
      print("No score yet")
      b=input("Press any key to continue:")
      main1()
  

def main1():
  init()
  a = "\033[1mWelcome To The Snake Water And Gun Game\033[0m"
  print(a.center(120))
  print("Rules of the game are very simple")
  print("1.Snake drink water")
  print("2.Water destroy gun")
  print("3.Gun kill snake")
  print("4.If you want to exit the game anytime then press 0")
  print("5.If you want to play the game then press 1")
  print("6.You will be given options to choose ")
  print("7.Press v for viewing score")
  print("8.Press m for main menu")
  c = Style.BRIGHT + "Best of luck" + Style.RESET_ALL
  print(c.center(120))
  b=input("Press key to continue:")
  if b.lower()=="v":
    view()  
  else:  
    input1()
main1()