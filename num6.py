import random


def roll():
    return random.randint(1, 6) + random.randint(1, 6)


def play_round(balance, bet):
    player_sum = roll()
    cpu_sum = roll()

    if player_sum > cpu_sum:
        new_balance = balance + bet
        result = "WIN"
    elif player_sum < cpu_sum:
        new_balance = balance - bet
        result = "LOSE"
    else:
        new_balance = balance
        result = "DRAW"

    return new_balance, result, player_sum, cpu_sum


def run_game(start_balance, rounds, bet_strategy):
    balance = start_balance

    for round_idx in range(1, rounds + 1):
        bet = bet_strategy(balance, round_idx)

        if bet <= 0 or bet > balance:
            print(f"R{round_idx}: Неверная ставка {bet}, баланс {balance}")
            continue

        new_balance, result, player_sum, cpu_sum = play_round(balance, bet)

        symbol = {"WIN": "+", "LOSE": "-", "DRAW": "="}[result]
        change = bet if result != "DRAW" else 0

        print(f"R{round_idx}: you={player_sum}, cpu={cpu_sum} → {symbol}{change}, balance={new_balance}")

        balance = new_balance

        if balance <= 0:
            print("Баланс исчерпан!")
            break

    print(f"Final balance: {balance}")
    return balance


if __name__ == "__main__":
    def test_strategy(balance, round_idx):
        if round_idx == 1:
            return 100
        elif balance > 1500:
            return 200
        else:
            return 50


    run_game(1000, 5, test_strategy)