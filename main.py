import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbols_dict = {"A": 2, "B": 4, "C": 6, "D": 8}
symbols_value = {"A": 5, "B": 4, "C": 3, "D": 2}


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns


def print_slot_machine(cols):
    for row in range(len(cols[0])):
        for i, col in enumerate(cols):
            if i != len(col) - 1:
                print(col[row], end="|")
            else:
                print(col[row], end="")
        print()


def check_winnings(columns, lines, bet, values):
    winnings = 0
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol_to_check != symbol:
                break
        else:
            winnings += values[symbol] * bet
    return winnings


def deposit():
    while True:
        amount = input("How much would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("The deposit should be more than zero")
        else:
            print("The deposit should be a number")
    return amount


def get_number_of_lines():
    while True:
        lines = input(
            "How many lines would you like to bet on (1-" + str(MAX_LINES) + ")? "
        )
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines")
        else:
            print("Please enter a number")
    return lines


def get_bet():
    while True:
        bet = input("How much would you like to bet on each line? ")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Enter a valid number between {MIN_BET} and {MAX_BET}")
        else:
            print("Please enter a number")
    return bet


def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(
                f"Your total bet is {total_bet}, which exceeds your balance({balance})"
            )
        else:
            break
    print(f"You're betting {bet} on {lines} lines. You're total bet is {total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbols_dict)
    print_slot_machine(slots)
    winnings = check_winnings(slots, lines, bet, symbols_value)
    print(f"You won {winnings}")
    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f"Current balance is {balance}")
        answ = input("Press enter to play.(q to quit)")
        if answ == "q":
            break
        balance += spin(balance)


main()
