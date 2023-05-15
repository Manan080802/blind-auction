from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)

bids={}
while(True):
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $"))
  bids[name] = price
  should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n").lower()
  if(should_continue=="yes"):
    clear()
  elif(should_continue=="no"):
    max_amount=0
    holder_name=""
    for name in bids:
      if bids[name]>0:
        max_amount=bids[name]
        holder_name= name
    print(f"The winner is {holder_name} with a bid of ${max_amount}")
    break
  else:
    print("You write some worng")
    break
    
  
  
  