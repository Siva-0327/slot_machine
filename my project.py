import sys
import random
MAX_LINES=3 #MAX_LINES is a global vaariable we can call this at any place in the program
MAX_BET=300 #MAX_BET is a global vaariable we can call this at any place in the prograM
MIN_BET=100 #MIN_BET is a global vaariable we can call this at any place in the prograM
rows=3   #MY SLOT MACHINE CONTAINS  3 ROWS
columns=3 #IT CINTAINS 3 COLUNMS
'''It's like A|C|B
             B|C|D
             C|C|C
IN THIS SCENARIO I WON ON 1 LINE'''
             
while True:
    name=input("please enter username :")# here name is global variable
    if not name.isdigit():
        break
    else:
        print("please enter valid input")
print(f" Hi! {name} .you are good go ")
print("you can earn $100 coins for 5 rupees")
def play_again():
    while True:
        again = input("Do you want to play again? (yes/No): ")
        if again.lower() == 'yes':
            return True
        elif again.lower() == 'no':
            break
        else:
            print("Please enter 'yes' or 'no'.")
symbols={'A':3,'B':3,'C':2,'D':4}# here i declare the values to spin there is 4 'A's to spin.    
def get_game(rows, columns, symbols):
    symbol_values = []# here i created a list to store values
    for key, value in symbols.items():
        #key means A like that & value means 4 like that in dictonaries
        symbol_values.extend([key] * value)
        # here  i'm entering keys into list how many times it has like we have 4 'A'S   
    column = []# creating a list to store values in columns 
    for _ in range(columns):# cretaing the column for 3 times
        random.shuffle(symbol_values)# shuffle the keys randomly it is main motive of game 
        row = []# creating a list to store values in rows
        for _ in range(rows):#creating the rows for 3 times
            row.append(symbol_values.pop())# appending the values randomly ands deleting the entered value after entering
        column.append(row)# appending rows to fill columns.
    return column
def print_game(column):# here we are calling columns which is stored by values
    for row in column:
        print(' | '.join(row))
def won(column, lines, bet, balance):
    symbol = column[0][0]== column[0][1]== column[0][2]
    check = column[1][0]==column[1][1]==column[1][2]
    var = column[2][0]==column[2][1]==column[2][2]
    winings=0
    if lines==1:
        if symbol or check or var:
            winings=lines*bet+balance
        else:
            winings=balance-bet
    if lines==2:
        if symbol and check or symbol and var or check and var:
            winings=lines*bet+balance
        else:
            winings=balance-bet
    if lines==3:
        if symbol and check and var:
            winings=lines*bet+balance
        else:
            winings=balance-bet
            
        
    return winings
            
            
def money():
    while True:
        amount=input("how much AMOUNT you want to deposit?$")
        # we have to check the input is number or not
        if amount.isdigit():
            amount=int(amount)
            if amount>0:
                if  amount>MAX_BET or amount<MIN_BET:
                    print(f"Please enter amount between ${MIN_BET}-${MAX_BET}.")
                    #here f means we are using frozen set                
                else:
                    if amount!=0:
                        print("you have to pay ",amount/20)
                        break
                                            
            else:
                print("please enter amount greater than 0")
                
        else:
            print("please enter a number")
    return amount
def get_lines():
    while True:
        lines=input("how many lines you want to bet(1-"+ str(MAX_LINES)+")$ ")
        #here we did concodnation
        if lines.isdigit():
            lines=int(lines)
            if lines<=MAX_LINES and lines>0:
                break
            else:
                print("please enter valid number of lines.")
        else:
            print("please enter valid number")
    return lines
def get_bet(balance):
    while True:
        bet=input("please enter how  much amount  you want to bet on line $:")
        if bet.isdigit():
            bet=int(bet)
            if bet>0:
                if bet>balance:
                    print(f"please enter amount between '0'to ${balance}.")
                else:
                    break
            else:
                print("you can't bet with amount ^0^.")
            
        else:
            print("please enter valid amount to bet.")
    return bet
def upi():
    while True:
        upi_id=input("Please enter your upi id:")
        if not upi_id.isdigit():
            break
        else:
            print("please enter valid id")
        

def main():
    while True:
        balance=money()# here we are calling the money that we deposit
        while True:
            lines=get_lines()
            bet=get_bet(balance)
            total_bet=lines*bet
            print(f"you bet on {lines} lines with amount {bet} on each so bet is equal to",total_bet)
            game = get_game(rows, columns, symbols)
            print_game(game)#here we are calling to print the game
            win=won(game,lines,bet,balance)
            print("your current balance is $",win) 
            
            choice=play_again()            
            if choice:
                balance=win
                if balance<1:
                    print("you don't have enough balance to bet")
                    break
                continue  # Restart the game
            else:
                print("you left with ",win)
                print("Thanks for playing!")
                upi()
                print("you get ",win/20)
                print(f"Mr.{name} money has been credited your account")
                sys.exit() 
 
main()
