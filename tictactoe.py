# Tic Tac Toe

import random

class Game:
    def drawBoard(self,board):
        # This function prints out the board that it was passed.

        # "board" is a list of 10 strings representing the board (ignore index 0)
        print('   |   |')
        print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
        print('   |   |')

    def inputPlayerLetter(self):
        # Lets the user type which letter they want Computer 1 to be want to be.
        # Returns a list with the Computer 1's letter as the first item, and the Computer 2's letter as the second.
        self.letter = ''
        while not (self.letter == 'X' or self.letter == 'O'):
            print('Do you want Computer 1 to be X or O?')
            self.letter = input().upper()

        # the first element in the tuple is the Computer 1's letter, the second is the computer's letter.
        if self.letter == 'X':
            return ['X', 'O']
        else:
            return ['O', 'X']

    def whoGoesFirst(self):
        # Randomly choose the Computer who goes first.
        if random.randint(0, 1) == 0:
            return 'Computer 2'
        else:
            return 'Computer 1'

    def playAgain(self):
        # This function returns True if the Computer 1 wants to play again, otherwise it returns False.
        print('Do you want to play again? (yes or no)')
        return input().lower().startswith('y')

    def makeMove(self,board, letter, move):
        board[move] = letter

    def isWinner(self,bo, le):
        # Given a board and a Computer 1's letter, this function returns True if that Computer 1 has won.
        # We use bo instead of board and le instead of letter so we don't have to type as much.
        return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
        (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle
        (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom
        (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side
        (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle
        (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side
        (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
        (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal

    def getBoardCopy(self,board):
        # Make a duplicate of the board list and return it the duplicate.
        self.dupeBoard = []

        for i in board:
            self.dupeBoard.append(i)

        return self.dupeBoard

    def isSpaceFree(self,board, move):
        # Return true if the passed move is free on the passed board.
        return board[move] == ' '

    def getPlayerMove(self,board):
        # Let the Computer 1 type in his move.
        self.move = ' '
        while self.move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(self.move)):
            print('What is your next move? (1-9)')
            self.move = input()
        return int(self.move)

    def chooseRandomMoveFromList(self,board, movesList):
        # Returns a valid move from the passed list on the passed board.
        # Returns None if there is no valid move.
        possibleMoves = []
        for i in movesList:
            if Game.isSpaceFree(self,board, i):
                possibleMoves.append(i)

        if len(possibleMoves) != 0:
            return random.choice(possibleMoves)
        else:
            return None

    def getComputerMove(self,board, computerLetter):
        # Given a board and the computer's letter, determine where to move and return that move.
        if computerLetter == 'X':
            playerLetter = 'O'
        else:
            playerLetter = 'X'

        # Here is our algorithm for our Tic Tac Toe AI:
        # First, check if we can win in the next move
        for i in range(1, 10):
            copy = Game.getBoardCopy(self,board)
            if Game.isSpaceFree(self,copy, i):
                Game.makeMove(self,copy, computerLetter, i)
                if Game.isWinner(self,copy, computerLetter):
                    return i

        # Check if the Computer 1 could win on his next move, and block them.
        for i in range(1, 10):
            copy = Game.getBoardCopy(self,board)
            if Game.isSpaceFree(self,copy, i):
                Game.makeMove(self,copy, playerLetter, i)
                if Game.isWinner(self,copy, playerLetter):
                    return i

        # Try to take one of the corners, if they are free.
        self.move = Game.chooseRandomMoveFromList(self,board, [1, 3, 7, 9])
        if self.move != None:
            return self.move

        # Try to take the center, if it is free.
        if Game.isSpaceFree(self,board, 5):
            return 5

        # Move on one of the sides.
        return Game.chooseRandomMoveFromList(self,board, [2, 4, 6, 8])

    def isBoardFull(self,board):
        # Return True if every space on the board has been taken. Otherwise return False.
        for i in range(1, 10):
            if Game.isSpaceFree(self,board, i):
                return False
        return True

    def run(self):
        print('Welcome to Tic Tac Toe!')

        while True:
            # Reset the board
            self.theBoard = [' '] * 10
            self.playerLetter, self.computerLetter = Game.inputPlayerLetter(self)
            self.turn = Game.whoGoesFirst(self)
            print('The ' + self.turn + ' will go first.')
            self.gameIsPlaying = True

            while self.gameIsPlaying:
                if self.turn == 'Computer 1':
                    # Computer 1's turn.
                    self.move = Game.getComputerMove(self,self.theBoard, self.playerLetter)
                    Game.makeMove(self,self.theBoard, self.playerLetter, self.move)

                    if Game.isWinner(self,self.theBoard, self.playerLetter):
                        Game.drawBoard(self,self.theBoard)
                        print('Hooray! Computer 1 has won the game!')
                        self.gameIsPlaying = False
                    else:
                        if Game.isBoardFull(self,self.theBoard):
                            Game.drawBoard(self,self.theBoard)
                            print('The game is a tie!')
                            break
                        else:
                            self.turn = 'Computer 2'

                else:
                    # Computer 2's turn.
                    self.move = Game.getComputerMove(self,self.theBoard, self.computerLetter)
                    Game.makeMove(self,self.theBoard, self.computerLetter, self.move)

                    if Game.isWinner(self,self.theBoard, self.computerLetter):
                        Game.drawBoard(self,self.theBoard)
                        print('Hooray! Computer 2 has won the game!')
                        self.gameIsPlaying = False
                    else:
                        if Game.isBoardFull(self,self.theBoard):
                            Game.drawBoard(self,self.theBoard)
                            print('The game is a tie!')
                            break
                        else:
                            self.turn = 'Computer 1'

            if not Game.playAgain(self):
                break
entire= Game()
entire.run()
