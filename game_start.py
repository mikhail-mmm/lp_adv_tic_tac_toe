from random import randint
from utils import print_game_field, check_user_turn, victory_check, draw_check


def ai_turn(field, ai_noughts_crosses):
    while True:
        ai_turn = randint(0, 8)
        if type(field[ai_turn]) == int:
            field[ai_turn] = ai_noughts_crosses
            print('\nХод компьютера.')
            print_game_field(field)
            break
        else:
            pass
    return field


def user_turn(field, noughts_crosses):
    while True:
        user_turn = input('Ваш ход: ')
        if check_user_turn(user_turn, field) == False:
            print('Неверный ввод, попробуйте ещё раз!')
        else:
            break
    field[int(user_turn) - 1] = noughts_crosses
    print_game_field(field)
    return field


def game_start(noughts_crosses, field):
    if noughts_crosses == 'O':
        ai_noughts_crosses = 'X'
        field = ai_turn(field, ai_noughts_crosses)
    else:
        print_game_field(field)
        ai_noughts_crosses = 'O'
    while True:
        if victory_check(field) == True: 
            result = 'Вы проиграли!'
            break
        if draw_check(field) == True:
            result = 'Ничья'
            break
        field = user_turn(field, noughts_crosses)
        if victory_check(field) == True: 
            result = 'Вы выиграли!'
            break
        if draw_check(field) == True:
            result = 'Ничья'
            break
        field = ai_turn(field, ai_noughts_crosses)
    return result
