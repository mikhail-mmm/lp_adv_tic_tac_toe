from game_start import game_start
from random import randint

message = '''Игра в крестики-нолики.
Вам представлено игровое поле с цифрами от 1 до 9,
чтобы совершить ход введите цифру соответствующую 
месту куда Вы хотите поставить крестик/нолик.
Для выхода нажмите Ctrl + C
Игра началась!

'''


def tic_tac_toe():
    field = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    if randint(0, 1) == 0:
        noughts_crosses = 'O'
    else:
        noughts_crosses = 'X'
    print(f'{message}Вы играете {noughts_crosses}!')
    print(game_start(noughts_crosses, field))


if __name__ == '__main__':
    tic_tac_toe()
