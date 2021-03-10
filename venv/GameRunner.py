from GameStatus import GameStatus
class GameRunner:
    def Run(self, player, board, console):
        while (board.GameStatus(player) == GameStatus.PLAYING):
            rolled_number = console.GetDiceRoll(player)
            board.Play(player, rolled_number)

        status = board.GameStatus(player)
        if (status == GameStatus.WON):
            console.DisplayWinningTheGame()
            return
        elif (status == GameStatus.LOST):
            console.DisplayLosingTheGame()
            return
        else:
            raise Exception("This is not supposed to happen")