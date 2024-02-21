import random
X_Score = 0
O_Score = 0
def inarow_Neast(ch, r_start, c_start, A, N):
    """check for a N-in-a-row eastward of element ch, return 
    True or False, as appropriate"""
    H = len(A)
    W = len(A[0])
    if r_start < 0 or r_start > H - 1:
        return False            
    if c_start < 0 or c_start + (N-1) > W - 1:
        return False            
    for i in range(N):
        if A[r_start][c_start+i] != ch: 
            return False
    return True               

def inarow_Nsouth(ch, r_start, c_start, A, N):
    """This should start from r_start and c_start and check for 
    N-in-a-row  southward of element ch, 
    returning True or False, as appropriate
    """
    H = len(A)
    W = len(A[0])
    if r_start < 0 or r_start + (N-1) > H - 1:
        return False 
    if c_start < 0 or c_start > W - 1:
        return False 
    for i in range(N):
        if A[r_start+i][c_start] != ch: 
            return False
    return True               

def inarow_Nnortheast(ch, r_start, c_start, A, N):
    """This should start from r_start and c_start and check for 
    N-in-a-row  southeastward of element ch, 
    returning True or False, as appropriate
    """
    H = len(A)
    W = len(A[0])
    if r_start - (N-1) < 0 or r_start > H - 1:
        return False 
    if c_start < 0 or c_start + (N-1) > W - 1:
        return False 
    for i in range(N):
        if A[r_start-i][c_start+i] != ch: 
            return False
    return True                 

def inarow_Nsoutheast(ch, r_start, c_start, A, N):
    """This should start from r_start and c_start and check for 
    N-in-a-row  northeastward of element ch, 
    returning True or False, as appropriate
    """
    H = len(A)
    W = len(A[0])
    if r_start < 0 or r_start + (N-1) > H - 1:
        return False            
    if c_start < 0 or c_start + (N-1) > W - 1:
        return False            
    for i in range(N):
        if A[r_start+i][c_start+i] != ch: 
            return False
    return True                 

class Board:
    """A data type representing a Tik-Tac-Toe board
       with an 3 rows and 3 columns.
    """

    def __init__(self, width, height):
        """Construct objects of type Board, with the given width and height."""
        self.width = width
        self.height = height
        self.data = [[' ']*width for row in range(height)]


    def __repr__(self):
        """This method returns a string representation
           for an object of type Board.
        """
        s = ''                         
        for row in range(0, self.height):
            s += ' ' + (2*self.width + 1) * '-' + "\n" 
            s += str(row)
            s += '|'
            for col in range(0, self.width):
                s += self.data[row][col] + '|'
            s += '\n'

        s += ' ' + (2*self.width + 1) * '-' + "\n"   

        s += '  ' + str(0) + ' ' + str(1) + ' ' + str(2)

        return s       
    
    def addMove(self, row, col, ox):
        """This method takes three argument  col, represents the index of 
        the column to which the checker will be added. 
        The second argument, row which represents the index of the
        row that the checker will be added. The third argument 
        represents the checker of the player
        """
        self.data[row][col] = ox

    def clear(self):
        """This method should clear the board
        """
        for row in range(0, self.height):
            for col in range(0, self.width):
                if self.data[row][col] == 'X' or self.data[row][col == 'O']:
                    self.data[row][col] = ' '
    
    def allowsMove(self, r, c):
        """This method should return True if the calling object does 
        allow a move into column C. It returns False if the column c
        is not a legal column number for the calling object
        """
        H = self.height
        W = self.width
        D = self.data
        if c < 0 or c >= W:
            return False
        if r < 0 or r > 2:
            return False
        elif D[r][c] == 'X' or D[r][c] == 'O':
            return False
        else:
            return True
    
    def isFull(self):
        """This method should return True if the calling object is 
        completely full of checkers and return False otherwise
        """
        for col in range(self.width):
            for row in range(self.height):
                if self.allowsMove(row, col) == True:
                    return False
        return True
    
    def delMove(self, r, c):
        """This method should do the opposite of addMove. It should
        remove the checker from the column c and row r. if column is empty
        then delMove should do nothing
        """
        if self.data[r][c] == 'X' or self.data[r][c] == 'O':
                self.data[r][c] = ' '
                return
    
    def winsFor(self, ox):
        """This method's argument ox is a 1-character checker:
        either 'X' or 'O'. It should return True if there are three
        checkers of type ox in a row on the board. It should return
        False otherwise
        """
        H = self.height
        W = self.width
        D = self.data

        for row in range(H):
            for col in range(W):
                if inarow_Neast(ox, row, col, D, 3) == True:
                    return True
                if inarow_Nnortheast(ox, row, col, D, 3) == True:
                    return True
                if inarow_Nsouth(ox, row, col, D, 3) == True:
                    return True
                if inarow_Nsoutheast(ox, row, col, D, 3) == True:
                    return True
        return False

    def colsToWin(self, ox):
        """This method should take one argument ox and return the list
        of columns where ox can move in the next turn in order to win
        and finish the game"""
        colList = []
        for col in range(self.width):
            for row in range(self.height):
                if self.allowsMove(row, col) == True:
                    self.addMove(row, col, ox)
                    if self.winsFor(ox) == True:
                        colList += [[row, col]]
                    self.delMove(row, col)
        return colList
    
    def aiMove(self, ox):
        """This method should return a winning move for either ox 
        or block an opponent from winning."""
        if len(self.colsToWin(ox))>0:
            return random.choice(self.colsToWin(ox))
        if ox == 'X':
            if len(self.colsToWin(ox)) == 0 and len(self.colsToWin('O'))>0:
                return random.choice(self.colsToWin('O'))
            else:
                return [random.choice(range(3)), random.choice(range(3))]
        if ox == 'O':
            if len(self.colsToWin(ox)) == 0 and len(self.colsToWin('X'))>0:
                return random.choice(self.colsToWin('X'))
            else:
                return [random.choice(range(3)), random.choice(range(3))]
    
    
    def hostGame2Player(self):
        """This game of hosts a game of tik-tac-toe, using all the methods
        above. It should alternate turns between X and O and ask the user
        to input a column number for each move
        """
        while True:
            print(b)
            user_row = -1
            user_column = -1
            while self.allowsMove(user_row, user_column) == False:
                user_stringRow = input("Choose a row: ")
                user_stringColumn = input("Choose a column: ")
                try:
                    user_row = int(user_stringRow)
                    user_column = int(user_stringColumn)
                except ValueError:
                    user_row = -1
                    user_column = -1
            self.addMove(user_row, user_column, 'X')
            if self.winsFor('X') == True:
                print(b)
                print("X has won")
                global X_Score
                X_Score += 1
                self.clear()
                break
            if self.isFull() == True:
                print(b)
                print("It is a tie")
                self.clear()
                break
            print(b)
            user_row = -1
            user_column = -1
            while self.allowsMove(user_row, user_column) == False:
                user_stringRow = input("Choose a row: ")
                user_stringColumn = input("Choose a column: ")
                try:
                    user_row = int(user_stringRow)
                    user_column = int(user_stringColumn)
                except ValueError:
                    user_row = -1
                    user_column = -1
            self.addMove(user_row, user_column, 'O')
            if self.winsFor('O') == True:
                print(b)
                print("O has won")
                global O_Score
                O_Score += 1
                self.clear()
                break
            if self.isFull() == True:
                print(b)
                print("It is a tie")
                self.clear()
                break
    
    def hostGame1PlayerX(self):
        """This game of hosts a game of tik-tac-toe, using all the methods
        above. It should alternate turns between X and O and ask the user
        to input a column number for X and Ai moves for O
        """
        while True:
            print(b)
            user_row = -1
            user_column = -1
            while self.allowsMove(user_row, user_column) == False:
                user_stringRow = input("Choose a row: ")
                user_stringColumn = input("Choose a column: ")
                try:
                    user_row = int(user_stringRow)
                    user_column = int(user_stringColumn)
                except ValueError:
                    user_row = -1
                    user_column = -1
            self.addMove(user_row, user_column, 'X')
            if self.winsFor('X') == True:
                print(b)
                print("X has won")
                global X_Score
                X_Score += 1
                self.clear()
                break
            if self.isFull() == True:
                print(b)
                print("It is a tie")
                self.clear()
                break
            print(b)
            ai_row = -1
            ai_column = -1
            while self.allowsMove(ai_row, ai_column) == False:
                ai_row, ai_column = self.aiMove('O')
            self.addMove(ai_row, ai_column, 'O')
            if self.winsFor('O') == True:
                print(b)
                print("O has won")
                global O_Score
                O_Score += 1
                self.clear()
                break
            if self.isFull() == True:
                print(b)
                print("It is a tie")
                self.clear()
                break

    def hostGame1PlayerO(self):
        """This game of hosts a game of tik-tac-toe, using all the methods
        above. It should alternate turns between X and O and ask the user
        to input a column number for O and Ai moves for X
        """
        while True:
            print(b)
            ai_row = -1
            ai_column = -1
            while self.allowsMove(ai_row, ai_column) == False:
                ai_row, ai_column = self.aiMove('X')
            self.addMove(ai_row, ai_column, 'X')
            if self.winsFor('X') == True:
                print(b)
                print("X has won")
                global X_Score 
                X_Score += 1
                self.clear()
                break
            if self.isFull() == True:
                print(b)
                print("It is a tie")
                self.clear()
                break
            print(b)
            user_row = -1
            user_column = -1
            while self.allowsMove(user_row, user_column) == False:
                user_stringRow = input("Choose a row: ")
                user_stringColumn = input("Choose a column: ")
                try:
                    user_row = int(user_stringRow)
                    user_column = int(user_stringColumn)
                except ValueError:
                    user_row = -1
                    user_column = -1
            self.addMove(user_row, user_column, 'O')
            if self.winsFor('O') == True:
                print(b)
                print("O has won")
                global O_Score
                O_Score += 1
                self.clear()
                break
            if self.isFull() == True:
                print(b)
                print("It is a tie")
                self.clear()
                break
    
    def hostGame0Player(self):
        """This game of hosts a game of tik-tac-toe, using all the methods
        above. It should alternate turns between X and O and have an two Ais' 
        playing each other
        """
        while True:
            print(b)
            ai_row = -1
            ai_column = -1
            while self.allowsMove(ai_row, ai_column) == False:
                ai_row, ai_column = self.aiMove('X')
            self.addMove(ai_row, ai_column, 'X')
            if self.winsFor('X') == True:
                print(b)
                print("X has won")
                global X_Score
                X_Score += 1
                self.clear()
                break
            if self.isFull() == True:
                print(b)
                print("It is a tie")
                self.clear()
                break
            print(b)
            ai_row = -1
            ai_column = -1
            while self.allowsMove(ai_row, ai_column) == False:
                ai_row, ai_column = self.aiMove('O')
            self.addMove(ai_row, ai_column, 'O')
            if self.winsFor('O') == True:
                print(b)
                print("O has won")
                global O_Score
                O_Score += 1
                self.clear()
                break
            if self.isFull() == True:
                print(b)
                print("It is a tie")
                self.clear()
                break
    
    def menu(self):
        """Prints the menu"""
        print()
        print("Menu:")
        print("  (1) Player vs Player")
        print("  (2) Player vs AI")
        print("  (3) AI vs AI")
        print("  (4) ScoreBoard")
        print("  (5) Quit")
        print() 
        userChoice = input("Your Choice: ")
        while userChoice not in ['1', '2', '3', '4', '5']:
            try:
                if userChoice not in ['1', '2', '3', '4', '5']:
                    print ("Didn't recongnize input")
                    userChoice = input("Your Choice: ")
            except ValueError:
                print("Didn't understand that input")
                print("Choose a number between 1 and 5")
        while True:     
            if userChoice == '1':
                self.hostGame2Player()
                return self.menu()
                
            if userChoice == '2':
                startInput = input("X or O? ")
                if startInput == 'X':
                    self.hostGame1PlayerX()
                    return self.menu()
                if startInput == 'O':
                    self.hostGame1PlayerO()
                    return self.menu()
                
            if userChoice == '3':
                self.hostGame0Player()
                return self.menu()

            if userChoice == '4':
                global X_Score
                global O_Score
                print("X Score is " + str(X_Score))
                print("O Score is " + str(O_Score))
                return self.menu()
            
            if userChoice == '5':
                break
        



    

b = Board(3,3)
    