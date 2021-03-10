from GameStatus import GameStatus
from Player import Player
from Board import Board
from GameStatus import GameStatus
from configparser import ConfigParser

#----------------------------------------------------------------

def dictionary_extract(location,section_name):
    config = ConfigParser()
    config.read(location)
    keys = list(config[section_name])
    values = []
    for iter in list(config[section_name]):
        values.append(config[section_name][iter])
    temp = {int(i): int(j) for i, j in zip(keys, values)}
    return temp
location = 'C:\\Users\\subra\\PycharmProjects\\pythonProject\\pythonProjectlatest66\\SnakeLadderMarch10\\venv\\config.ini'
snake = dictionary_extract(location, "snake")
ladder = dictionary_extract(location, "ladder")
config = ConfigParser()
config.read(location)
last_position = int(config["constants"]["last_position"])

board = Board(last_position, snake, ladder)

# --------------------------------

def test_when_the_player_is_moved_then_player_is_in_right_position():
    player1 = Player(1, 500)
    player1.MoveTo(5)
    assert player1._position == 5
    del player1
def test_when_money_is_added_does_money_get_added():
    player1 = Player(1, 500)
    player1.AddMoney(50)
    assert player1._money_available == 550
    del player1

def test_when_money_is_removed_does_money_get_removed_correctly():
    player1 = Player(1, 500)
    player1.RemoveMoney(50)
    assert player1._money_available == 450
    del player1

def test_when_there_is_zero_or_less_money_is_money_available_false():
    player1 = Player(1, 0)
    assert player1.IsMoneyAvailable()==False
    del player1
    player1 = Player(1, 0)
    player1.RemoveMoney(50)
    assert player1.IsMoneyAvailable()==False
    del player1

def test_when_there_some_money_is_money_available_false():
    player1 = Player(1, 500)
    assert player1.IsMoneyAvailable()==True
    del player1

def test_when_player_diceroll_are_provided_does_play_work_correctly():
    player1 = Player(1, 500)
    diceroll=2
    board.Play(player1,diceroll)
    assert player1._position == 3
    assert player1._money_available == 500
    del player1

def test_when_player_lands_on_ladder5_does_money_and_position_change():
    player1 = Player(4, 500)
    diceroll=1
    board.Play(player1, diceroll)
    assert player1._position == 10
    assert player1._money_available == 600
    del player1

def test_when_player_lands_on_ladder12_does_money_and_position_change():
    player1 = Player(11, 500)
    diceroll=1
    board.Play(player1, diceroll)
    assert player1._position == 26
    assert player1._money_available == 600

def test_when_player_lands_on_ladder16_does_money_and_position_change():
    player1 = Player(15, 500)
    diceroll=1
    board.Play(player1, diceroll)
    assert player1._position == 29
    assert player1._money_available == 600
    del player1

def test_when_player_lands_on_ladder19_does_money_and_position_change():
    player1 = Player(18, 500)
    diceroll=1
    board.Play(player1, diceroll)
    assert player1._position == 33
    assert player1._money_available == 600
    del player1

def test_when_player_lands_on_ladder35_does_money_and_position_change():
    player1 = Player(34, 500)
    diceroll=1
    board.Play(player1, diceroll)
    assert player1._position == 36
    assert player1._money_available == 600
    del player1

def test_when_player_lands_on_ladder40_does_money_and_position_change():
    player1 = Player(38, 500)
    diceroll=2
    board.Play(player1, diceroll)
    assert player1._position == 45
    assert player1._money_available == 600
    del player1

def test_when_player_lands_on_snake14_does_money_and_position_change():
    player1 = Player(13, 500)
    diceroll=1
    board.Play(player1, diceroll)
    assert player1._position == 2
    assert player1._money_available == 400
    del player1

def test_when_player_lands_on_snake23_does_money_and_position_change():
    player1 = Player(21, 500)
    diceroll=2
    board.Play(player1, diceroll)
    assert player1._position == 8
    assert player1._money_available == 400
    del player1

def test_when_player_lands_on_snake47_does_money_and_position_change():
    player1 = Player(46, 500)
    diceroll=1
    board.Play(player1, diceroll)
    assert player1._position == 37
    assert player1._money_available == 400
    del player1

def test_when_player_lands_on_snake47_does_money_and_position_change():
    player1 = Player(42, 500)
    diceroll=1
    board.Play(player1, diceroll)
    assert player1._position == 41
    assert player1._money_available == 400
    del player1


def test_when_game_is_yet_to_be_completed_does_game_status_indicate_the_same():
    player1 = Player(42, 500)
    assert board.GameStatus(player1)==GameStatus.PLAYING
    del player1

def test_when_game_has_been_won_does_game_status_indicate_the_same():
    player1 = Player(49, 500)
    assert board.GameStatus(player1)==GameStatus.WON
    del player1

def test_when_game_has_been_lost_does_game_status_indicate_the_same():
    player1 = Player(49,0)
    assert board.GameStatus(player1)==GameStatus.LOST
    del player1

def test_when_player_cannot_move_within_the_board_does_player_position_change_correctly():
    player1 = Player(48, 500)
    diceroll = 4
    board.Play(player1,diceroll)















