from member.python_pratice import game
from member.python_pratice import shop


def turn_on():
    print('=Turn on game=')

    while True:
        choice = input('What would you like to do \n 1: Go to Shop')
        if choice == '0':
            break
        elif choice == '1':
            shop.buy_item()
        elif choice == '2':
            game.play_game()
        else:
            print('Choice not exist')

    print('Turn off game')


if __name__ == '__main__':
    turn_on()
