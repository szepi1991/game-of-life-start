from game_of_life import lib
import time

board = lib.Board.from_string(
    """
..........
...X......
.X.X......
..XX......
..........    
..........
..........
..........
..........
"""
)


def main():
    for i in range(5):
        print(board)
        board.evolve()
        time.sleep(0.8)


if __name__ == "__main__":
    main()
