import sys
from src.twenty_four import TwentyFour

def main():
    game = TwentyFour()

    print("Starting the 24-game!")
    game.play_game()
    print("Thanks for playing!")


if __name__ == '__main__':
    sys.exit(main())
    