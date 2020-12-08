import random
from IPython.display import clear_output


#board display and design
def display_board(board):
    print("       |       |     ")
    print(f"  {board[1]}    |  {board[2]}    | {board[3]} ")
    print("_______|_______|_____")
    print("       |       |     ")
    print(f"  {board[4]}    |  {board[5]}    | {board[6]} ")
    print("_______|_______|_____")
    print("       |       |     ")
    print(f"  {board[7]}    |  {board[8]}    | {board[9]} ")
    print("       |       |     ")

#prompt input from user to choose marker
def player_input():
    choice='WRONG'
    acceptable_choice=['X','O','x','o']
    
    while choice not in acceptable_choice:
        choice=input("For player 1, do you want to use marker X or O?")
        choice=choice.upper()
        if choice not in acceptable_choice:
            print("Sorry, please choose either X or O")
    return choice    

#function to place marker at specified position on the board
def place_marker(board, marker, position):
    
    board[position]=marker

#check if there's a win!
def win_check(board, mark):
    
    if set(mark) == set(board[1] + board[2] + board[3]) or set(mark) == set(board[4] + board[5] + board[6]) or set(mark) == set(board[7] + board[8] + board[9]) or set(mark) == set(board[1] + board[4] + board[7]) or set(mark) == set(board[2] + board[5] + board[8]) or set(mark) == set(board[3] + board[6] + board[9]) or set(mark) == set(board[1] + board[5] + board[9]) or set(mark) == set(board[3] + board[5] + board[7]):
        print(f"Congratulations! Player {mark} win!")
        return True
    else:
        return False

#choose randomly which player goes first
def choose_first():
    first=random.randint(1,2)
    print(f"Player {first} go first.")
    return first

#check if a position on the board is occupied
def space_check(board, position):
    if board[position]==" ":
        return True
    else:
        return False
  
#check if every position on the board is occupied
def full_board_check(board):
    full=False
    for i in [1,2,3,4,5,6,7,8,9]:
        full=full+space_check(board,i)
    return full

#prompt input from user which position does the user want to mark at
def player_choice(board):
    
    pos_choice='wrong'
    acceptable_range=[1,2,3,4,5,6,7,8,9]
    while pos_choice not in acceptable_range:
        try:
            pos_choice=input("Which position do you want to mark at?")
            pos_choice=int(pos_choice)
        except:
            pass
        if pos_choice not in acceptable_range:
            print("Please pick position 1-9")
        if pos_choice in acceptable_range:
            if space_check(board, pos_choice)==False:
                pos_choice='wrong'
                print("Sorry, the position is occupied. Please pick an unoccupied position.")
                
            else:
                break
    return pos_choice

#ask users if they want to play again
def replay():
    again='wrong'
    acceptable=['Y','N', 'y', 'n']
    while again not in acceptable:
        again=input("Do you wanna play again? (Y or N)")
        again=again.upper()
        if again not in acceptable:
            print("Choose Y or N")
    return again

#play tictac, compiled
def tictac():
    print('Welcome to Tic Tac Toe! \n')
    board=['#','1','2','3','4','5','6','7','8','9']
    display_board(board)
    print("\n \n")
    playing=True
    
    while playing==True:
        if playing==True:
            board=['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
            display_board(board)
            player1=player_input()
           
            if player1=='X':
                player2='O'
            else:
                player2='X'
            
            if choose_first()==1:
                marker=player1
            else:
                marker=player2
        
            while playing==True:
                
                position=player_choice(board)
                place_marker(board, marker, position)
                display_board(board)
                
                if full_board_check(board)==0:
                    print("The game is draw!")
                    playing==False
                    break

                if win_check(board,marker)==True:
                    playing==False
                    break
                    
                if marker==player1:
                    marker=player2
                else:
                    marker=player1
    
                
            
        if replay()=='N':
            playing==False
            break
        else:
            playing==True

if __name__ == '__main__':
	tictac()                                         