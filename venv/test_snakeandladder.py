from GameStatus import GameStatus
from Player import Player
from Board import Board
from GameStatus import GameStatus

def test_when_the_player_is_moved_then_player_is_in_right_position():
    player1 = Player(1, 500)
    player1.MoveTo(5)
    assert player1._position == 5


    A='''
    player1.AddMoney(50)
    assert player1._money_available == 550
    player1.RemoveMoney(50)
    assert player1._money_available == 500
    assert player1.IsMoneyAvailable() == True
    player2 = Player(49, 500)
    board1 = Board()
    assert board1.GameStatus(player2) == GameStatus(1)
    player3 = Player(1, 500)
    board2 = Board()
    player3.RemoveMoney(550)
    assert board2.GameStatus(player3) == GameStatus(-1)

    def test_laddercheck():
    test2 = Player(1,500)
    Board.Play(test2,4)
    assert test2._position == 10
    assert test2._money_available == 600
    
    '''

