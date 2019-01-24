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
        self.letter = ''
        while not (self.letter == 'X' or self.letter == 'O'):
            print('Do you want User 1 to be X or O?')
            self.letter = input().upper()

        if self.letter == 'X':
            return ['X', 'O']
        else:
            return ['O', 'X']

    def whoGoesFirst(self):
        # Randomly choose who goes first.
        if random.randint(0, 1) == 0:
            return 'User 2'
        else:
            return 'User 1'

    def playAgain(self):
        # This function returns True if players want to play again, otherwise it returns False.
        print('Do you want to play again? (yes or no)')
        return input().lower().startswith('y')

    def makeMove(self,board, letter, move):
        board[move] = letter

    def isWinner(self,bo, le):
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

    def getPlayerMove(self,board, gameLetter):
        self.move = ' '
        while self.move not in '1 2 3 4 5 6 7 8 9'.split() or not self.isSpaceFree(board, int(self.move)):
            print("What is your (%s)'s next move? (1-9)" % gameLetter)
            self.move = input()
        return int(self.move)

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
                if self.turn == 'User 1':
                    Game.drawBoard(self,self.theBoard)
                    self.move = Game.getPlayerMove(self,self.theBoard, self.playerLetter)
                    
                    Game.makeMove(self,self.theBoard, self.playerLetter, self.move)

                    if Game.isWinner(self,self.theBoard, self.playerLetter):
                        Game.drawBoard(self,self.theBoard)
                        print('Hooray! User 1 has won the game!')
                        self.gameIsPlaying = False
                    elif Game.isBoardFull(self,self.theBoard):
                        Game.drawBoard(self,self.theBoard)
                        print('The game is a tie!')
                        break
                    else:
                        self.turn = 'User 2'

                else:
                    Game.drawBoard(self,self.theBoard)
                    self.move = Game.getPlayerMove(self,self.theBoard, self.computerLetter)
                    Game.makeMove(self,self.theBoard, self.computerLetter, self.move)

                    if Game.isWinner(self,self.theBoard, self.computerLetter):
                        Game.drawBoard(self,self.theBoard)
                        print('Hooray! User 2 has won the game!')
                        self.gameIsPlaying = False
                    elif Game.isBoardFull(self,self.theBoard):
                        Game.drawBoard(self,self.theBoard)
                        print('The game is a tie!')
                        break
                    else:
                        self.turn = 'User 1'

            if not Game.playAgain(self):
                break
entire= Game()
entire.run()

