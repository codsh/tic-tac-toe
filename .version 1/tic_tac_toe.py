import random
from tkinter import *
tic_tac_toe = Tk()
tic_tac_toe.title('Крестики-нолики.')
tic_tac_toe.geometry('800x800+200+75')
tic_tac_toe.iconbitmap('tic_tac_toe_icon.ico')
tic_tac_toe.resizable(width=False, height=False)

human_plays_for = Listbox(tic_tac_toe, font=('Arial', 14, 'bold'), fg='green', exportselection=0)
human_plays_for.insert(END, 'x (человек и бот)')
human_plays_for.insert(END, 'o (человек и бот)')
human_plays_for.insert(END, 'человек и человек')
human_plays_for.place(x=612, y=715, width=185, height=70)

bot_level = Listbox(tic_tac_toe, font=('Arial', 14, 'bold'), fg='green', exportselection=0)
bot_level.insert(END, 'легко')
bot_level.insert(END, 'нормально')
bot_level.insert(END, 'сложно!')
bot_level.insert(END, 'невозможно!!!')
bot_level.place(x=50, y=700, width=150, height=100)

indicator_switch = Listbox(tic_tac_toe, font=('Arial', 7, 'bold'), fg='green', exportselection=0)
indicator_switch.insert(END, '1')
indicator_switch.insert(END, 'o')
indicator_switch.place(x=5, y=575, width=10, height=28)

label_of_win = Label(tic_tac_toe, text='', font=('Arial', 40), fg='black', bg='light yellow')
label_of_win.place(x=10, y=10, height=80, width=780)

flag_of_move = 'x'
list_of_moves = ['', '', '',
                 '', '', '',
                 '', '', '']
history_of_game = [['', '', '', '', '', '', '', '', '']]


def check_the_win(game_position):
    if game_position.count('') >= 5:
        return None

    for i_tic_tac_you in [0, 1, 2]:
        if game_position[i_tic_tac_you] == game_position[i_tic_tac_you + 3] == game_position[i_tic_tac_you + 6]:
            if game_position[i_tic_tac_you] == 'x':
                return 10
            if game_position[i_tic_tac_you] == 'o':
                return -10
    for i_tic_tac_you in [0, 3, 6]:
        if game_position[i_tic_tac_you] == game_position[i_tic_tac_you + 1] == game_position[i_tic_tac_you + 2]:
            if game_position[i_tic_tac_you] == 'x':
                return 10
            if game_position[i_tic_tac_you] == 'o':
                return -10
    for i_tic_tac_you in [2, 4]:
        if game_position[4 - i_tic_tac_you] == game_position[4] == game_position[4 + i_tic_tac_you]:
            if game_position[4] == 'x':
                return 10
            if game_position[4] == 'o':
                return -10
            
    if game_position.count('') == 0:
        return 0
    
    return None


def move11():
    global flag_of_move, list_of_moves
    if btn11.cget('text') == '':
        if flag_of_move == 'x':
            btn11.config(text='x', fg='red', activeforeground='red')
            flag_of_move = 'o'
            list_of_moves[0] = 'x'
        else:
            btn11.config(text='o', fg='blue', activeforeground='blue')
            flag_of_move = 'x'
            list_of_moves[0] = 'o'
        alert_about_win()


def move12():
    global flag_of_move, list_of_moves
    if btn12.cget('text') == '':
        if flag_of_move == 'x':
            btn12.config(text='x', fg='red', activeforeground='red')
            flag_of_move = 'o'
            list_of_moves[1] = 'x'
        else:
            btn12.config(text='o', fg='blue', activeforeground='blue')
            flag_of_move = 'x'
            list_of_moves[1] = 'o'
        alert_about_win()


def move13():
    global flag_of_move, list_of_moves
    if btn13.cget('text') == '':
        if flag_of_move == 'x':
            btn13.config(text='x', fg='red', activeforeground='red')
            flag_of_move = 'o'
            list_of_moves[2] = 'x'
        else:
            btn13.config(text='o', fg='blue', activeforeground='blue')
            flag_of_move = 'x'
            list_of_moves[2] = 'o'
        alert_about_win()


def move21():
    global flag_of_move, list_of_moves
    if btn21.cget('text') == '':
        if flag_of_move == 'x':
            btn21.config(text='x', fg='red', activeforeground='red')
            flag_of_move = 'o'
            list_of_moves[3] = 'x'
        else:
            btn21.config(text='o', fg='blue', activeforeground='blue')
            flag_of_move = 'x'
            list_of_moves[3] = 'o'
        alert_about_win()


def move22():
    global flag_of_move, list_of_moves
    if btn22.cget('text') == '':
        if flag_of_move == 'x':
            btn22.config(text='x', fg='red', activeforeground='red')
            flag_of_move = 'o'
            list_of_moves[4] = 'x'
        else:
            btn22.config(text='o', fg='blue', activeforeground='blue')
            flag_of_move = 'x'
            list_of_moves[4] = 'o'
        alert_about_win()


def move23():
    global flag_of_move, list_of_moves
    if btn23.cget('text') == '':
        if flag_of_move == 'x':
            btn23.config(text='x', fg='red', activeforeground='red')
            flag_of_move = 'o'
            list_of_moves[5] = 'x'
        else:
            btn23.config(text='o', fg='blue', activeforeground='blue')
            flag_of_move = 'x'
            list_of_moves[5] = 'o'
        alert_about_win()


def move31():
    global flag_of_move, list_of_moves
    if btn31.cget('text') == '':
        if flag_of_move == 'x':
            btn31.config(text='x', fg='red', activeforeground='red')
            flag_of_move = 'o'
            list_of_moves[6] = 'x'
        else:
            btn31.config(text='o', fg='blue', activeforeground='blue')
            flag_of_move = 'x'
            list_of_moves[6] = 'o'
        alert_about_win()


def move32():
    global flag_of_move, list_of_moves
    if btn32.cget('text') == '':
        if flag_of_move == 'x':
            btn32.config(text='x', fg='red', activeforeground='red')
            flag_of_move = 'o'
            list_of_moves[7] = 'x'
        else:
            btn32.config(text='o', fg='blue', activeforeground='blue')
            flag_of_move = 'x'
            list_of_moves[7] = 'o'
        alert_about_win()


def move33():
    global flag_of_move, list_of_moves
    if btn33.cget('text') == '':
        if flag_of_move == 'x':
            btn33.config(text='x', fg='red', activeforeground='red')
            flag_of_move = 'o'
            list_of_moves[8] = 'x'
        else:
            btn33.config(text='o', fg='blue', activeforeground='blue')
            flag_of_move = 'x'
            list_of_moves[8] = 'o'
        alert_about_win()


btn11 = Button(tic_tac_toe, bg='light yellow', text='', font=('Arial', 100, 'bold'), fg='red', activeforeground='red',
               activebackground='light yellow', command=move11)
btn11.place(x=100, y=100, width=200, height=200)

btn12 = Button(tic_tac_toe, bg='light yellow', text='', font=('Arial', 100, 'bold'), fg='red', activeforeground='red',
               activebackground='light yellow', command=move12)
btn12.place(x=300, y=100, width=200, height=200)

btn13 = Button(tic_tac_toe, bg='light yellow', text='', font=('Arial', 100, 'bold'), fg='red', activeforeground='red',
               activebackground='light yellow', command=move13)
btn13.place(x=500, y=100, width=200, height=200)

btn21 = Button(tic_tac_toe, bg='light yellow', text='', font=('Arial', 100, 'bold'), fg='red', activeforeground='red',
               activebackground='light yellow', command=move21)
btn21.place(x=100, y=300, width=200, height=200)

btn22 = Button(tic_tac_toe, bg='light yellow', text='', font=('Arial', 100, 'bold'), fg='red', activeforeground='red',
               activebackground='light yellow', command=move22)
btn22.place(x=300, y=300, width=200, height=200)

btn23 = Button(tic_tac_toe, bg='light yellow', text='', font=('Arial', 100, 'bold'), fg='red', activeforeground='red',
               activebackground='light yellow', command=move23)
btn23.place(x=500, y=300, width=200, height=200)

btn31 = Button(tic_tac_toe, bg='light yellow', text='', font=('Arial', 100, 'bold'), fg='red', activeforeground='red',
               activebackground='light yellow', command=move31)
btn31.place(x=100, y=500, width=200, height=200)

btn32 = Button(tic_tac_toe, bg='light yellow', text='', font=('Arial', 100, 'bold'), fg='red', activeforeground='red',
               activebackground='light yellow', command=move32)
btn32.place(x=300, y=500, width=200, height=200)

btn33 = Button(tic_tac_toe, bg='light yellow', text='', font=('Arial', 100, 'bold'), fg='red', activeforeground='red',
               activebackground='light yellow', command=move33)
btn33.place(x=500, y=500, width=200, height=200)


def x_bot_move():
    global random_list, random_result
    if random_list[random_result] == 0:
        btn11.config(text='x', fg='red', activeforeground='red')
    elif random_list[random_result] == 1:
        btn12.config(text='x', fg='red', activeforeground='red')
    elif random_list[random_result] == 2:
        btn13.config(text='x', fg='red', activeforeground='red')
    elif random_list[random_result] == 3:
        btn21.config(text='x', fg='red', activeforeground='red')
    elif random_list[random_result] == 4:
        btn22.config(text='x', fg='red', activeforeground='red')
    elif random_list[random_result] == 5:
        btn23.config(text='x', fg='red', activeforeground='red')
    elif random_list[random_result] == 6:
        btn31.config(text='x', fg='red', activeforeground='red')
    elif random_list[random_result] == 7:
        btn32.config(text='x', fg='red', activeforeground='red')
    else:
        btn33.config(text='x', fg='red', activeforeground='red')


def o_bot_move():
    global random_list, random_result
    if random_list[random_result] == 0:
        btn11.config(text='o', fg='blue', activeforeground='blue')
    elif random_list[random_result] == 1:
        btn12.config(text='o', fg='blue', activeforeground='blue')
    elif random_list[random_result] == 2:
        btn13.config(text='o', fg='blue', activeforeground='blue')
    elif random_list[random_result] == 3:
        btn21.config(text='o', fg='blue', activeforeground='blue')
    elif random_list[random_result] == 4:
        btn22.config(text='o', fg='blue', activeforeground='blue')
    elif random_list[random_result] == 5:
        btn23.config(text='o', fg='blue', activeforeground='blue')
    elif random_list[random_result] == 6:
        btn31.config(text='o', fg='blue', activeforeground='blue')
    elif random_list[random_result] == 7:
        btn32.config(text='o', fg='blue', activeforeground='blue')
    else:
        btn33.config(text='o', fg='blue', activeforeground='blue')


def start_lighting_the_best_moves():
    global random_list, random_result, list_of_moves
    if list_of_moves.count('') in [2, 4, 6, 8]:
        if random_list[random_result] == 0:
            btn11.config(activebackground='light cyan', background='light cyan')
        elif random_list[random_result] == 1:
            btn12.config(activebackground='light cyan', background='light cyan')
        elif random_list[random_result] == 2:
            btn13.config(activebackground='light cyan', background='light cyan')
        elif random_list[random_result] == 3:
            btn21.config(activebackground='light cyan', background='light cyan')
        elif random_list[random_result] == 4:
            btn22.config(activebackground='light cyan', background='light cyan')
        elif random_list[random_result] == 5:
            btn23.config(activebackground='light cyan', background='light cyan')
        elif random_list[random_result] == 6:
            btn31.config(activebackground='light cyan', background='light cyan')
        elif random_list[random_result] == 7:
            btn32.config(activebackground='light cyan', background='light cyan')
        else:
            btn33.config(activebackground='light cyan', background='light cyan')
    else:
        if random_list[random_result] == 0:
            btn11.config(activebackground='mistyrose', background='mistyrose')
        elif random_list[random_result] == 1:
            btn12.config(activebackground='mistyrose', background='mistyrose')
        elif random_list[random_result] == 2:
            btn13.config(activebackground='mistyrose', background='mistyrose')
        elif random_list[random_result] == 3:
            btn21.config(activebackground='mistyrose', background='mistyrose')
        elif random_list[random_result] == 4:
            btn22.config(activebackground='mistyrose', background='mistyrose')
        elif random_list[random_result] == 5:
            btn23.config(activebackground='mistyrose', background='mistyrose')
        elif random_list[random_result] == 6:
            btn31.config(activebackground='mistyrose', background='mistyrose')
        elif random_list[random_result] == 7:
            btn32.config(activebackground='mistyrose', background='mistyrose')
        else:
            btn33.config(activebackground='mistyrose', background='mistyrose')
        
        
def stop_lighting_the_best_moves():
    global random_list, random_result
    btn11.config(activebackground='light yellow', background='light yellow')
    btn12.config(activebackground='light yellow', background='light yellow')
    btn13.config(activebackground='light yellow', background='light yellow')
    btn21.config(activebackground='light yellow', background='light yellow')
    btn22.config(activebackground='light yellow', background='light yellow')
    btn23.config(activebackground='light yellow', background='light yellow')
    btn31.config(activebackground='light yellow', background='light yellow')
    btn32.config(activebackground='light yellow', background='light yellow')
    btn33.config(activebackground='light yellow', background='light yellow')
    hint_button['state'] = NORMAL
    start_button['state'] = NORMAL
    cancel_move_button['state'] = NORMAL


def max_algo(the_position, limit_of_counter, counter):
    if check_the_win(the_position) == 10:
        return 512
    if check_the_win(the_position) == -10:
        return -512
    if check_the_win(the_position) == 0:
        return 0
    if counter >= limit_of_counter:
        return 0
    list_of_all_def_moves = []
    for i in range(len(the_position)):
        if the_position[i] != '':
            continue
        else:
            the_position[i] = 'x'
            list_of_all_def_moves.append(min_algo(the_position[:4] + the_position[4:], limit_of_counter, counter + 1))
            the_position[i] = ''
    return max(list_of_all_def_moves) / 2


def min_algo(the_position, limit_of_counter, counter):
    if check_the_win(the_position) == 10:
        return 512
    if check_the_win(the_position) == -10:
        return -512
    if check_the_win(the_position) == 0:
        return 0
    if counter >= limit_of_counter:
        return 0
    list_of_all_def_moves = []
    for i in range(len(the_position)):
        if the_position[i] != '':
            continue
        else:
            the_position[i] = 'o'
            list_of_all_def_moves.append(max_algo(the_position[:4] + the_position[4:], limit_of_counter, counter + 1))
            the_position[i] = ''
    return min(list_of_all_def_moves) / 2


def indicator_calculations(evaluate_the_position):
    if evaluate_the_position.count('') == 9:
        return 'x = o'
    elif check_the_win(evaluate_the_position) == 10:
        return 'x, W'
    elif check_the_win(evaluate_the_position) == -10:
        return 'o, W'
    elif evaluate_the_position.count('') == 0:
        return 'ничья'
    elif evaluate_the_position.count('') in [1, 3, 5, 7]:
        exponent_evaluation = max_algo(evaluate_the_position, 10, 0)
        if exponent_evaluation == 0:
            return 'x = o'
        elif 512 / exponent_evaluation > 0:
            for i in range(9):
                if 2 ** i == 512 / exponent_evaluation:
                    if i % 2 == 1:
                        return f'x, W{i}'
                    else:
                        return f'x, W{i}'
        else:
            for i in range(9):
                if 2 ** i == -512 / exponent_evaluation:
                    if i % 2 == 1:
                        return f'o, W{i}'
                    else:
                        return f'o, W{i}'
    elif evaluate_the_position.count('') in [2, 4, 6, 8]:
        exponent_evaluation = min_algo(evaluate_the_position, 10, 0)
        if exponent_evaluation == 0:
            return 'x = o'
        elif 512 / exponent_evaluation > 0:
            for i in range(9):
                if 2 ** i == 512 / exponent_evaluation:
                    if i % 2 == 1:
                        return f'x, W{i}'
                    else:
                        return f'x, W{i}'
        else:
            for i in range(9):
                if 2 ** i == -512 / exponent_evaluation:
                    if i % 2 == 1:
                        return f'o, W{i}'
                    else:
                        return f'o, W{i}'
    else:
        return 'x = o'


def indicator_text():
    indicator_info = indicator_calculations(list_of_moves)

    if indicator_info.count('x') == indicator_info.count('o') == 1 or indicator_info == 'ничья':
        indicator_of_situation.config(fg='green')
    elif indicator_info.count('o') == 1:
        indicator_of_situation.config(fg='blue')
    elif indicator_info.count('x') == 1:
        indicator_of_situation.config(fg='red')
    else:
        indicator_of_situation.config(fg='green')
    indicator_of_situation.config(text=indicator_info)
    

def bot_calculations():
    global flag_of_move, list_of_moves, random_list, random_result, limit_moves_depth

    possible_position = list_of_moves

    limit_moves_depth = 0

    if bot_level.get(ANCHOR) == 'легко':
        limit_moves_depth = 0
    if bot_level.get(ANCHOR) == 'нормально':
        limit_moves_depth = 2
    if bot_level.get(ANCHOR) == 'сложно!':
        limit_moves_depth = 4
    if bot_level.get(ANCHOR) == 'невозможно!!!':
        limit_moves_depth = 10

    if human_plays_for.get(ANCHOR) == 'o (человек и бот)' and list_of_moves.count('') % 2 == 1:
        if list_of_moves.count('') == 9:
            random_list = [1, 3, 5, 7] + 2 * [0, 2, 6, 8] + 4 * [4]
            random_result = random.randint(0, len(random_list) - 1)
        if list_of_moves.count('') in [1, 3, 5, 7]:
            good_positions = []
            position_list = []
            f_from_position_list = []
            for i in range(len(possible_position)):
                if possible_position[i] != '':
                    continue
                else:
                    possible_position[i] = 'x'
                    position_list.append(possible_position[:4] + possible_position[4:])
                    f_from_position_list.append(min_algo(possible_position[:4] + possible_position[4:],
                                                         limit_moves_depth, 0))
                    possible_position[i] = ''
            for j in range(len(f_from_position_list)):
                if f_from_position_list[j] == max(f_from_position_list):
                    good_positions.append(position_list[j])

            random_list = []
            for k in range(len(possible_position)):
                if possible_position[k] != '':
                    continue
                else:
                    possible_position[k] = 'x'
                    if possible_position in good_positions:
                        random_list.append(k)
                    possible_position[k] = ''

            if len(random_list) > 1:
                random_result = random.randint(0, len(random_list) - 1)
            else:
                random_result = 0

        list_of_moves[random_list[random_result]] = 'x'
        x_bot_move()

        alert_about_win()
        flag_of_move = 'o'

    if human_plays_for.get(ANCHOR) == 'x (человек и бот)' and list_of_moves.count('') in [2, 4, 6, 8]:
        good_positions = []
        position_list = []
        f_from_position_list = []
        for i in range(len(possible_position)):
            if possible_position[i] != '':
                continue
            else:
                possible_position[i] = 'o'
                position_list.append(possible_position[:4] + possible_position[4:])
                f_from_position_list.append(max_algo(possible_position[:4] + possible_position[4:],
                                                     limit_moves_depth, 0))
                possible_position[i] = ''
        for j in range(len(f_from_position_list)):
            if f_from_position_list[j] == min(f_from_position_list):
                good_positions.append(position_list[j])

        random_list = []
        for k in range(len(possible_position)):
            if possible_position[k] != '':
                continue
            else:
                possible_position[k] = 'o'
                if possible_position in good_positions:
                    random_list.append(k)
                possible_position[k] = ''
        if len(random_list) > 1:
            random_result = random.randint(0, len(random_list) - 1)
        else:
            random_result = 0

        list_of_moves[random_list[random_result]] = 'o'
        o_bot_move()

        alert_about_win()
        flag_of_move = 'x'


def alert_about_win():
    global list_of_moves, history_of_game

    history_of_game += [list_of_moves[:4] + list_of_moves[4:]]

    if check_the_win(list_of_moves) in [10, -10]:
        for is_question in range(len(list_of_moves)):
            if list_of_moves[is_question] == '':
                if is_question == 0:
                    btn11['state'] = DISABLED
                if is_question == 1:
                    btn12['state'] = DISABLED
                if is_question == 2:
                    btn13['state'] = DISABLED
                if is_question == 3:
                    btn21['state'] = DISABLED
                if is_question == 4:
                    btn22['state'] = DISABLED
                if is_question == 5:
                    btn23['state'] = DISABLED
                if is_question == 6:
                    btn31['state'] = DISABLED
                if is_question == 7:
                    btn32['state'] = DISABLED
                if is_question == 8:
                    btn33['state'] = DISABLED

    if check_the_win(list_of_moves) == 10:
        label_of_win.config(text='Крестики победили!', fg='red', activeforeground='red')
    elif check_the_win(list_of_moves) == -10:
        label_of_win.config(text='Нолики победили!', fg='blue', activeforeground='blue')
    elif list_of_moves.count('') == 0:
        label_of_win.config(text='Ничья!', fg='green')
    else:
        bot_calculations()

    if indicator_switch.get(ANCHOR) == '1':
        indicator_text()
    else:
        indicator_of_situation.config(text='')


def hint_calculation():
    global flag_of_move, list_of_moves, random_list, random_result, limit_moves_depth

    hint_button['state'] = DISABLED
    start_button['state'] = DISABLED
    cancel_move_button['state'] = DISABLED
    
    possible_position = list_of_moves

    limit_moves_depth = 12

    if check_the_win(possible_position) is None:
        if list_of_moves.count('') == 9:
            random_list = [1, 3, 5, 7] + 2 * [0, 2, 6, 8] + 4 * [4]
            for random_result in range(len(random_list)):
                start_lighting_the_best_moves()
            tic_tac_toe.after(1500, stop_lighting_the_best_moves)
    
        elif list_of_moves.count('') in [1, 3, 5, 7]:
            good_positions = []
            position_list = []
            f_from_position_list = []
            for i in range(len(possible_position)):
                if possible_position[i] != '':
                    continue
                else:
                    possible_position[i] = 'x'
                    position_list.append(possible_position[:4] + possible_position[4:])
                    f_from_position_list.append(min_algo(possible_position[:4] + possible_position[4:],
                                                         limit_moves_depth, 0))
                    possible_position[i] = ''
            for j in range(len(f_from_position_list)):
                if f_from_position_list[j] == max(f_from_position_list):
                    good_positions.append(position_list[j])
    
            random_list = []
            for k in range(len(possible_position)):
                if possible_position[k] != '':
                    continue
                else:
                    possible_position[k] = 'x'
                    if possible_position in good_positions:
                        random_list.append(k)
                    possible_position[k] = ''
    
            if len(random_list) > 1:
                for random_result in range(len(random_list)):
                    start_lighting_the_best_moves()
            else:
                random_result = 0
                start_lighting_the_best_moves()
            tic_tac_toe.after(1500, stop_lighting_the_best_moves)
    
        elif list_of_moves.count('') in [2, 4, 6, 8]:
            good_positions = []
            position_list = []
            f_from_position_list = []
            for i in range(len(possible_position)):
                if possible_position[i] != '':
                    continue
                else:
                    possible_position[i] = 'o'
                    position_list.append(possible_position[:4] + possible_position[4:])
                    f_from_position_list.append(max_algo(possible_position[:4] + possible_position[4:],
                                                         limit_moves_depth, 0))
                    possible_position[i] = ''
            for j in range(len(f_from_position_list)):
                if f_from_position_list[j] == min(f_from_position_list):
                    good_positions.append(position_list[j])
    
            random_list = []
            for k in range(len(possible_position)):
                if possible_position[k] != '':
                    continue
                else:
                    possible_position[k] = 'o'
                    if possible_position in good_positions:
                        random_list.append(k)
                    possible_position[k] = ''
            if len(random_list) > 1:
                for random_result in range(len(random_list)):
                    start_lighting_the_best_moves()
            else:
                random_result = 0
                start_lighting_the_best_moves()
            tic_tac_toe.after(1500, stop_lighting_the_best_moves)

        else:
            hint_button['state'] = NORMAL
            start_button['state'] = NORMAL
            cancel_move_button['state'] = NORMAL

    else:
        hint_button['state'] = NORMAL
        start_button['state'] = NORMAL
        cancel_move_button['state'] = NORMAL
        

def start_the_game():
    global flag_of_move, list_of_moves, label_of_win, history_of_game
    btn11['state'] = NORMAL
    btn12['state'] = NORMAL
    btn13['state'] = NORMAL
    btn21['state'] = NORMAL
    btn22['state'] = NORMAL
    btn23['state'] = NORMAL
    btn31['state'] = NORMAL
    btn32['state'] = NORMAL
    btn33['state'] = NORMAL
    btn11.config(text='')
    btn12.config(text='')
    btn13.config(text='')
    btn21.config(text='')
    btn22.config(text='')
    btn23.config(text='')
    btn31.config(text='')
    btn32.config(text='')
    btn33.config(text='')
    list_of_moves = ['', '', '',
                     '', '', '',
                     '', '', '']

    flag_of_move = 'x'

    history_of_game = [['', '', '', '', '', '', '', '', '']]

    label_of_win.config(text='', fg='black')

    bot_calculations()

    if indicator_switch.get(ANCHOR) == '1':
        indicator_text()
    else:
        indicator_of_situation.config(text='')


def past_position():
    global list_of_moves
    btn11.config(text=list_of_moves[0])
    btn12.config(text=list_of_moves[1])
    btn13.config(text=list_of_moves[2])
    btn21.config(text=list_of_moves[3])
    btn22.config(text=list_of_moves[4])
    btn23.config(text=list_of_moves[5])
    btn31.config(text=list_of_moves[6])
    btn32.config(text=list_of_moves[7])
    btn33.config(text=list_of_moves[8])
    if btn11.cget('text') == 'x':
        btn11.config(fg='red', activeforeground='red')
    elif btn11.cget('text') == 'o':
        btn11.config(fg='blue', activeforeground='blue')
    else:
        pass
    if btn12.cget('text') == 'x':
        btn12.config(fg='red', activeforeground='red')
    elif btn12.cget('text') == 'o':
        btn12.config(fg='blue', activeforeground='blue')
    else:
        pass
    if btn13.cget('text') == 'x':
        btn13.config(fg='red', activeforeground='red')
    elif btn13.cget('text') == 'o':
        btn13.config(fg='blue', activeforeground='blue')
    else:
        pass
    if btn21.cget('text') == 'x':
        btn21.config(fg='red', activeforeground='red')
    elif btn21.cget('text') == 'o':
        btn21.config(fg='blue', activeforeground='blue')
    else:
        pass
    if btn22.cget('text') == 'x':
        btn22.config(fg='red', activeforeground='red')
    elif btn22.cget('text') == 'o':
        btn22.config(fg='blue', activeforeground='blue')
    else:
        pass
    if btn23.cget('text') == 'x':
        btn23.config(fg='red', activeforeground='red')
    elif btn23.cget('text') == 'o':
        btn23.config(fg='blue', activeforeground='blue')
    else:
        pass
    if btn31.cget('text') == 'x':
        btn31.config(fg='red', activeforeground='red')
    elif btn31.cget('text') == 'o':
        btn31.config(fg='blue', activeforeground='blue')
    else:
        pass
    if btn32.cget('text') == 'x':
        btn32.config(fg='red', activeforeground='red')
    elif btn32.cget('text') == 'o':
        btn32.config(fg='blue', activeforeground='blue')
    else:
        pass
    if btn33.cget('text') == 'x':
        btn33.config(fg='red', activeforeground='red')
    elif btn33.cget('text') == 'o':
        btn33.config(fg='blue', activeforeground='blue')
    else:
        pass
    

def cancel_the_move():
    global history_of_game, list_of_moves, flag_of_move

    label_of_win.config(text='')
    btn11['state'] = NORMAL
    btn12['state'] = NORMAL
    btn13['state'] = NORMAL
    btn21['state'] = NORMAL
    btn22['state'] = NORMAL
    btn23['state'] = NORMAL
    btn31['state'] = NORMAL
    btn32['state'] = NORMAL
    btn33['state'] = NORMAL

    if human_plays_for.get(ANCHOR) in ['o (человек и бот)', 'x (человек и бот)'] and \
            bot_level.get(ANCHOR) in ['легко', 'нормально', 'сложно!', 'невозможно!!!']:
        if (human_plays_for.get(ANCHOR) == 'x (человек и бот)' and
                check_the_win(list_of_moves) == 10 or
                human_plays_for.get(ANCHOR) == 'o (человек и бот)' and
                check_the_win(list_of_moves) == -10):
            history_of_game = history_of_game[:-1]
            list_of_moves = history_of_game[-1][:4] + history_of_game[-1][4:]
            if flag_of_move == 'x':
                flag_of_move = 'o'
            elif flag_of_move == 'o':
                flag_of_move = 'x'
            else:
                pass
        elif len(history_of_game) == 2 or len(history_of_game) == 10:
            history_of_game = history_of_game[:-1]
            list_of_moves = history_of_game[-1][:4] + history_of_game[-1][4:]
            if flag_of_move == 'x':
                flag_of_move = 'o'
            elif flag_of_move == 'o':
                flag_of_move = 'x'
            else:
                pass
        elif 9 >= len(history_of_game) >= 3:
            history_of_game = history_of_game[:-2]
            list_of_moves = history_of_game[-1][:4] + history_of_game[-1][4:]
        else:
            pass
    elif human_plays_for.get(ANCHOR) not in ['o (человек и бот)', 'x (человек и бот)'] and len(history_of_game) >= 2:
        history_of_game = history_of_game[:-1]
        list_of_moves = history_of_game[-1][:4] + history_of_game[-1][4:]
        if flag_of_move == 'x':
            flag_of_move = 'o'
        elif flag_of_move == 'o':
            flag_of_move = 'x'
        else:
            pass
    else:
        list_of_moves = history_of_game[-1][:4] + history_of_game[-1][4:]

    past_position()
    if indicator_switch.get(ANCHOR) == '1':
        indicator_text()
    else:
        indicator_of_situation.config(text='')


indicator_of_situation = Label(tic_tac_toe, fg='green', bg='yellow', font=('Arial', 16, 'bold'))
indicator_of_situation.place(x=25, y=575, width=70, height=28)

cancel_move_button = Button(tic_tac_toe, text='отмена\nхода', fg='lime', bg='light yellow', font=('Arial', 14),
                            justify='center', command=cancel_the_move)
cancel_move_button.place(x=5, y=605, width=90, height=45)

start_button = Button(tic_tac_toe, text='начать заново!', fg='lime', bg='light yellow', font=('Arial', 40),
                      justify='center', command=start_the_game)
start_button.place(x=200, y=710, height=80)

hint_button = Button(tic_tac_toe, text='совет', fg='lime', bg='light yellow', font=('Arial', 20),
                     justify='center', command=hint_calculation)
hint_button.place(x=5, y=650, width=90, height=40)

tic_tac_toe.mainloop()
