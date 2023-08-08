import random

MAX_LINES = 3 # Global const (all caps is the convention in Python for defining global variables)
MAX_BET = 100
MIN_BET = 1

# Rows and Cols for the slot machine
ROWS = 3
COLS = 3

# The symbols that are on each column of the slot machine
symbol_count = {
  "A": 2,
  "B": 4,
  "C": 6,
  "D": 8
}

# The multipliers for winning on different symbols
symbol_value = {
  "A": 2,
  "B": 4,
  "C": 6,
  "D": 8
}

def check_winnings(columns, lines, bet):

  
def get_slot_machine_spin(rows, cols, symbols):
  all_symbols = []
  for symbol, symbol_count in symbols.items(): # Loop through each symbol in our symbol_count dictionary
    for _ in range(symbol_count): # _ is used in place of the iterator var, just so we don't have an unused var
      all_symbols.append(symbol) # Will add the symbol as many times as the symbol count, so there will be 2 As etc.
      
  columns = []
  for _ in range(cols):
    column = []
    current_symbols = all_symbols[:] # : means copy all_symbols, so we can mutate current_symbols

    for _ in range(rows): #for every column, we need to generate a certain amount of symbols
      value = random.choice(all_symbols)
      current_symbols.remove(value) # Remove from current symbols
      column.append(value)
    columns.append(column)
  
  return columns

def print_slot_machine(columns):
  # Need to transpose as this will be a matrix (to get the column slots to display properly)
  for row in range(len(columns[0])):
    for i, column in enumerate(columns):
      if i != len(columns) - 1:
        print(column[row], end=" | ")
      else:
        print(column[row], end="")
        
    print() # Print on a new line
    
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
    
  slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
  print_slot_machine(slots)
  
  
  print(f"You are betting £{bet} on £{lines}, total bet is £{total_bet}. Your current balance is £{balance}")
main()