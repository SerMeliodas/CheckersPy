from game import Game

from dotenv import load_dotenv
import os

if __name__ == "__main__":
    load_dotenv()

    BOARD_SIZE = int(os.getenv("BOARD_SIZE", '500'))
    game = Game(BOARD_SIZE, BOARD_SIZE)
    game.run()
