import game
import turtle

def main():
    board = game.Game(mode=8)
    board.draw()
    board.start_game()
    import classroom

    turtle.done()


if __name__ == "__main__":
    main()