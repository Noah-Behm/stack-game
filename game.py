from copy import deepcopy
import os


def print_state(current_state):
    print("Current state of your game:\n")
    print(f'{" " * 5}{current_state[0][0]:<16}{current_state[1][0]:<16}{current_state[2][0]:<16}')
    print(f'{" " * 5}{current_state[0][1]:<16}{current_state[1][1]:<16}{current_state[2][1]:<16}')
    print(f'{" " * 5}{current_state[0][2]:<16}{current_state[1][2]:<16}{current_state[2][2]:<16}')
    print("_" * 48)


def select_grab():
    done = False
    ret = ""

    while done is False:
        stack_select = input("Which stack would you like to take from? ")
        if stack_select not in ['1', '2', '3']:
            print("Please enter a valid choice... i.e. 1, 2, or 3")
        else:
            ret = stack_select
            done = True
    return int(ret)


def select_place():
    done = False
    ret = ""

    while done is False:
        stack_move = input("Which stack would you like to add to? ")
        if stack_move not in ['1', '2', '3']:
            print("Please enter a valid choice... i.e. 1, 2, or 3")
        else:
            ret = stack_move
            done = True
    return int(ret)


def check_column_remove(col, current):
    lst = current[col]
    ret = 0
    if lst == ["", "", ""]:
        print("You can't remove a ring from a stack with no rings!")
        input("Press enter to resume playing")
    else:
        for i in range(len(lst)):
            if lst[i] != "":
                ret = i
                break
    return int(ret)


def check_column_place(col, current):
    lst = current[col]
    ret = 2
    for i in range(len(lst)):
        if lst[i] != "":
            ret = i-1
            break
    return int(ret)


def check_win(current_state):
    ret = False
    win_condition = [small, medium, large]
    if current_state[2] == win_condition:
        ret = True
    return ret


def check_rules(current):
    ret = True
    for i in current:
        if len(i[0]) > (len(i[1]) or len(i[2])) or len(i[1]) > len(i[2]):
            ret = False
    return ret


def handle_illegal_move():
    print("Oops... that was an illegal move. The game state will be reverted.")
    input("Press enter to resume playing")


def handle_restart():
    done = False
    ret = ""

    while done is False:
        inp = input("Would you like to play again? [y/n] ")
        if inp == "y":
            ret = True
            done = True
        elif inp == "n":
            ret = False
            done = True
        else:
            print("Please enter either y or n.")

    return ret


if __name__ == '__main__':
    small = "  __"
    medium = " ____"
    large = "______"
    empty = ""
    cont = True
    current = [[small, medium, large], [empty, empty, empty], [empty, empty, empty]]
    proposed = [[small, medium, large], [empty, empty, empty], [empty, empty, empty]]

    while cont is True:
        print_state(current)
        select = select_grab() - 1  # will act as col index of current_state
        place = select_place() - 1

        remove = check_column_remove(select, current)  # will act as row index of current_state
        place_pos = check_column_place(place, current)

        element = current[select][remove]
        if element != "":
            proposed[select][remove] = empty
            proposed[place][place_pos] = element

            if check_rules(proposed) is True:
                current = deepcopy(proposed)
            else:
                handle_illegal_move()
                proposed = deepcopy(current)
    
            if check_win(current):
                os.system('cls' if os.name == 'nt' else 'clear')
                print_state(current)
                print("\n\nCONGRATULATIONS YOU WON!!!")
                if handle_restart():
                    current = [[small, medium, large], [empty, empty, empty], [empty, empty, empty]]
                    proposed = [[small, medium, large], [empty, empty, empty], [empty, empty, empty]]
                else:
                    cont = False
        os.system('cls' if os.name == 'nt' else 'clear')