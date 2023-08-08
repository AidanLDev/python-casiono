MAX_LINES = 3 # Global const (all caps is the convention in Python for defining global variables)
MAX_BET = 100
MIN_BET = 1

def deposit():
  while True: # Keep asking for a deposit until a valid deposit is entered
    amount = input("How much do you want to deposit? £")
    if amount.isdigit():
      amount = int(amount) # convert to int now we know it's a valid number
      if amount > 0:
        break
      else:
        print("Amount must be greater than 0.")
    else:
      print('Please enter a number.')
  return amount

def get_number_of_lines():
  while True: # Keep asking for a deposit until a valid deposit is entered
    lines = input("How many lines do you want to bet on? (1 - " + str(MAX_LINES) + ") ")
    if lines.isdigit():
      lines = int(lines) # convert to int now we know it's a valid number
      if 1 <= lines <= MAX_LINES:
        break
      else:
        print("Enter a valid number of lines.")
    else:
      print('Please enter a number.')
  return lines

def get_bet():
  while True:
    bet = input("How much would you like to bet on each line? £")
    if bet.isdigit():
      bet = int(bet)
      if MIN_BET <= bet <= MAX_BET:
        break
      else:
        print(f"Amount must be between £{MIN_BET} - £{MAX_BET}.")
    else: print("Please enter a number")
  return bet

def main():
  balance = deposit()
  lines = get_number_of_lines()
  while True:
    bet = get_bet()
    total_bet = bet * lines
    
    if total_bet > balance:
      print(f"You do not have a sufficient deposit to bet that amount, your current balance is: £{balance}")
    else:
      break
  
  
  print(f"You are betting £{bet} on £{lines}, total bet is £{total_bet}. Your current balance is £{balance}")
main()