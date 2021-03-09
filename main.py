from Player import Player
from Console import Console
from Board import Board
from GameRunner import GameRunner

from GameStatus import GameStatus
if __name__ == '__main__':
    board1=Board()
    console1=Console()
    player1=Player(1,500)
    game1=GameRunner()
    game1.Run(player1,board1,console1)




