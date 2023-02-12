def print_game_field(field):
    game_field = f'''{field[0]} {field[1]} {field[2]}
{field[3]} {field[4]} {field[5]}
{field[6]} {field[7]} {field[8]}'''
    print(game_field)


def check_user_turn(user_turn, field):
    try:
        user_turn = int(user_turn)
    except ValueError:
        return False
    if user_turn > 9 or user_turn < 0:
        return False
    elif field[user_turn - 1] == 'X' or field[user_turn - 1] == 'O':
        return False
    else:
        return True


def victory_check(field):
    if field[0] == 'O' and field[1] == 'O' and field[2] == 'O':
        return True
    elif field[3] == 'O' and field[4] == 'O' and field[5] == 'O':
        return True
    elif field[6] == 'O' and field[7] == 'O' and field[8] == 'O':
        return True
    elif field[0] == 'O' and field[3] == 'O' and field[6] == 'O':
        return True
    elif field[1] == 'O' and field[4] == 'O' and field[7] == 'O':
        return True
    elif field[2] == 'O' and field[5] == 'O' and field[8] == 'O':
        return True
    elif field[0] == 'O' and field[4] == 'O' and field[8] == 'O':
        return True
    elif field[2] == 'O' and field[4] == 'O' and field[6] == 'O':
        return True
    elif field[0] == 'X' and field[1] == 'X' and field[2] == 'X':
        return True
    elif field[3] == 'X' and field[4] == 'X' and field[5] == 'X':
        return True
    elif field[6] == 'X' and field[7] == 'X' and field[8] == 'X':
        return True
    elif field[0] == 'X' and field[3] == 'X' and field[6] == 'X':
        return True
    elif field[1] == 'X' and field[4] == 'X' and field[7] == 'X':
        return True
    elif field[2] == 'X' and field[5] == 'X' and field[8] == 'X':
        return True
    elif field[0] == 'X' and field[4] == 'X' and field[8] == 'X':
        return True
    elif field[2] == 'X' and field[4] == 'X' and field[6] == 'X':
        return True
    else:
        return False


def draw_check(field):
    n = 0
    for el in field:
        if type(el) == str:
            n += 1
    if n == 9:
        return True
