from GameStatus import GameStatus
from Player import Player
from Board import Board
from GameStatus import GameStatus
from configparser import ConfigParser

#----------------------------------------------------------------
last_position = 49
snake={14:2,23:8,47:37,43:41}
ladder={5:10,12:26,16:29,19:33,35:36,40:45}
board = Board(last_position, snake, ladder)

# --------------------------------

def test_when_the_player_is_moved_then_player_is_in_right_position():
    player = Player(1, 500)
    player.MoveTo(5)
    assert player._position == 5

def test_when_money_is_added_does_money_get_added():
    player = Player(1, 500)
    player.AddMoney(50)
    assert player._money_available == 550


def test_when_money_is_removed_does_money_get_removed_correctly():
    player = Player(1, 500)
    player.RemoveMoney(50)
    assert player._money_available == 450


def test_when_there_is_zero_or_less_money_is_money_available_false():
    player = Player(1, 0)
    assert player.IsMoneyAvailable()==False
    player = Player(1, 0)
    player.RemoveMoney(50)
    assert player.IsMoneyAvailable()==False


def test_when_there_some_money_is_money_available_false():
    player = Player(1, 500)
    assert player.IsMoneyAvailable()==True


def test_when_player_diceroll_are_provided_does_play_work_correctly():
    player = Player(1, 500)
    diceroll=2
    board.Play(player,diceroll)
    assert player._position == 3
    assert player._money_available == 500


def test_when_player_lands_on_ladder5_does_money_and_position_change():
    player = Player(4, 500)
    diceroll=1
    board.Play(player, diceroll)
    assert player._position == 10
    assert player._money_available == 600


def test_when_player_lands_on_ladder12_does_money_and_position_change():
    player = Player(11, 500)
    diceroll=1
    board.Play(player, diceroll)
    assert player._position == 26
    assert player._money_available == 600

def test_when_player_lands_on_ladder16_does_money_and_position_change():
    player = Player(15, 500)
    diceroll=1
    board.Play(player, diceroll)
    assert player._position == 29
    assert player._money_available == 600

def test_when_player_lands_on_ladder19_does_money_and_position_change():
    player = Player(18, 500)
    diceroll=1
    board.Play(player, diceroll)
    assert player._position == 33
    assert player._money_available == 600


def test_when_player_lands_on_ladder35_does_money_and_position_change():
    player = Player(34, 500)
    diceroll=1
    board.Play(player, diceroll)
    assert player._position == 36
    assert player._money_available == 600


def test_when_player_lands_on_ladder40_does_money_and_position_change():
    player = Player(38, 500)
    diceroll=2
    board.Play(player, diceroll)
    assert player._position == 45
    assert player._money_available == 600


def test_when_player_lands_on_snake14_does_money_and_position_change():
    player = Player(13, 500)
    diceroll=1
    board.Play(player, diceroll)
    assert player._position == 2
    assert player._money_available == 400


def test_when_player_lands_on_snake23_does_money_and_position_change():
    player = Player(21, 500)
    diceroll=2
    board.Play(player, diceroll)
    assert player._position == 8
    assert player._money_available == 400


def test_when_player_lands_on_snake47_does_money_and_position_change():
    player = Player(46, 500)
    diceroll=1
    board.Play(player, diceroll)
    assert player._position == 37
    assert player._money_available == 400


def test_when_player_lands_on_snake47_does_money_and_position_change():
    player = Player(42, 500)
    diceroll=1
    board.Play(player, diceroll)
    assert player._position == 41
    assert player._money_available == 400



def test_when_game_is_yet_to_be_completed_does_game_status_indicate_the_same():
    player = Player(42, 500)
    assert board.GameStatus(player)==GameStatus.PLAYING


def test_when_game_has_been_won_does_game_status_indicate_the_same():
    player = Player(49, 500)
    assert board.GameStatus(player)==GameStatus.WON


def test_when_game_has_been_lost_does_game_status_indicate_the_same():
    player = Player(49,0)
    assert board.GameStatus(player)==GameStatus.LOST


def test_when_player_cannot_move_within_the_board_does_player_position_change_correctly():
    player = Player(48, 500)
    diceroll = 4
    board.Play(player,diceroll)
    assert player._position == 48
    assert player._money_available == 490
