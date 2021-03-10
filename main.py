from Player import Player
from Console import Console
from Board import Board
from GameRunner import GameRunner
from configparser import ConfigParser
from GameStatus import GameStatus
def dictionary_extract(location,section_name):
    config = ConfigParser()
    config.read(location)
    keys = list(config[section_name])
    values = []
    for iter in list(config[section_name]):
        values.append(config[section_name][iter])
    temp = {int(i): int(j) for i, j in zip(keys, values)}
    return temp

if __name__ == '__main__':
    location="venv/config.ini"
    snake=dictionary_extract(location,"snake")
    ladder=dictionary_extract(location,"ladder")
    config = ConfigParser()
    config.read(location)
    last_position=int(config["constants"]["last_position"])

    board = Board(int(last_position), snake, ladder)
    console=Console()
    player=Player(1, 500)
    game=GameRunner()
    game.Run(player, board, console)























































