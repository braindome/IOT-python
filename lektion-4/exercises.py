"""
Lab 3 - Functions

In THIS FILE you should write your code.
Compare with the solutions in `answers.py`.

Run with:
    python functions_lab_exercises.py
"""

import math

# ----------------------
# Section 1: Basic functions
# ----------------------

def ex_1_1():
    """
    Exercise 1.1 (1p)
    Create a function that returns the sum of all numbers between two chosen numbers.
    For example, 10 and 20 should return 10+11+12+...+20.
    """
    # TODO: Write your code here
    def sum_everything(x, y):
        return sum(range (x, y+1))
    return sum_everything


def ex_1_2():
    """
    Exercise 1.2 (1p)
    Create a function that returns the color of a given fruit:
    banana -> yellow
    apple  -> green
    kiwi   -> green
    plum   -> red
    """
    # TODO: Write your code here
    def return_color(fruit: str):
        match fruit:
            case "banana": return "yellow"
            case "apple": return "green"
            case "kiwi": return "green"
            case "plum": return "red"
            case _: return "Not implemented"
    
    return return_color("apple")


def ex_1_3():
    """
    Exercise 1.3 (1p)
    Create a function that returns a comma-separated string of numbers from range_start to range_stop. """
    # TODO: Write your code here
    def formatted_nums(range_start, range_stop):
        return ",".join(str(i) for i in range(range_start, range_stop + 1))
    return formatted_nums(2, 23)
        


def ex_1_4():
    """
    Exercise 1.4 (1p)
    Create a function that returns a comma-separated string of numbers from range_start down to range_stop.    """
    # TODO: Write your code here
    def formatted_nums(range_start, range_stop):
        return ",".join(str(i) for i in range(range_start, range_stop - 1, -1))
    return formatted_nums(2, 23)


def ex_1_5():
    """
    Exercise 1.5 (1p)
    Create a function that returns a comma-separated string of numbers between two values,
    handling both ascending and descending ranges.
    """
    # TODO: Write your code here
    def formatted_nums(start, stop):
        if start <= stop:
            return ",".join(str(i) for i in range(start, stop + 1))
        else:
            return ",".join(str(i) for i in range(start, stop - 1. -1))
    return formatted_nums(83, 121)


def ex_1_6():
    """
    Exercise 1.6 (1p)
    Create a function that returns a string repeated a specified number of times.
    """
    # TODO: Write your code here
    def repeat_string(s, times):
        return s * times
    return repeat_string("marble", 5)

def ex_1_7():
    """
    Exercise 1.7 (1p)
    Create a function (that takes three arguments: range_start, range_stop, value) that returns True if a value is strictly between two given numbers,
    otherwise False.
    """
    # TODO: Write your code here
    def num_validation(range_start, range_stop, value):
        lower = min(range_start, range_stop)
        upper = max(range_start, range_stop)
        return lower < value < upper

    return num_validation(22, 44, 23)



def ex_1_8():
    """
    Exercise 1.9 (1p)
    Create a function called `degrees_to_radians()` that should take one
    argument, a degree value. The function should convert the value to radians
    and return the result with max 4 decimals    """
    # TODO: Write your code here
    def degrees_to_radians(degrees):
        return round(degrees * (math.pi/180), 4)
    return degrees_to_radians(93)


def ex_1_9():
    """
    Exercise 1.10 (1p)
     Create a function called `fizz_buzz()` that takes two arguments `start` and
     `stop` and returns a comma-separated string.
    
     The arguments represents the starting point and stop point of the game
     `Fizz Buzz` (http://en.wikipedia.org/wiki/Fizz_buzz). The function should
     run from start to stop and add `Fizz`, `Buzz` or both to your
     result-variable at appropriate numbers.
    
     Each entry to your result should be comma-separated. If `stop` is equal or
     lower than `start`, the function should return an appropriate error
     message.
    """
    # TODO: Write your code here
    def fizz_buzz(start, stop):
        if stop <= start:
            return "Error! End number can't be lower than starting number!"
        result = []
        for i in range(start, stop + 1):
            entry = ""
            if i % 3 == 0:
                entry += "Fizz"
            if i % 5 == 0:
                entry += "Buzz"
            if i % 5 == 0 and i % 3 == 0:
                entry += "Fizz Buzz"
            if not entry:
                entry = str(i)
            result.append(entry)
        return ", ".join(result)
    
    fizz_buzz(2, 54)



# ----------------------
# Section 2: Extra assignments
# ----------------------

def ex_2_1():
    """
    Exercise 2.1 (3p)
    
    Create a function that takes two variables: the sum of the player's hand 
    and the sum of the dealer's hand.
    
    Player's hand: 4, 10, 3
    Dealer's hand: 3, 6, 11
    
    The function should return a string in the format:
    'Player: 17, Dealer: 20'
    
    Test your function with these values.
    """
    # TODO: Write your code here
    def print_sums(player_hand: list[int], dealer_hand: list[int]) -> str:
        return f"Player: {sum(player_hand)}, Dealer: {sum(dealer_hand)}"
    return print_sums([4, 10, 3], [3, 6, 11])


def ex_2_2():
    """
    Exercise 2.2 (3p)
    
    Create a function that takes two variables: the sum of the player's hand
    and the sum of the dealer's hand.
    
    Player's hand: 4, 10, 3
    Dealer's hand: 3, 6, 11
    
    Include a status check:
      - Player <21: "safe"
      - Player =21: "black jack"
      - Player >21: "busted"
      - Dealer <17: "safe"
      - Dealer >=17 and <21: "stop"
      - Dealer =21: "black jack"
      - Dealer >21: "busted"
    
    Return a string in the format: 'Player: safe, Dealer: busted'
    
    """
    # TODO: Write your code here
    def print_sums(player_hand: list[int], dealer_hand: list[int]) -> str:
        player_sum = sum(player_hand)
        dealer_sum = sum(dealer_hand)
        player_status = ""
        dealer_status = ""
        if player_sum < 21:
            player_status = "safe"
        elif player_sum == 21:
            player_status = "black jack"
        elif player_sum > 21:
            player_status = "busted"
        
        if dealer_sum < 17:
            dealer_status = "safe"
        elif 17 <= dealer_sum < 21:
            dealer_status = "stop"
        elif dealer_sum == 21:
            dealer_status = "black jack"
        elif dealer_sum > 21:
            dealer_status = "busted"
        return f"Player: {player_status}, Dealer: {dealer_status}"
    
    return print_sums([4, 10, 3], [3, 6, 11])

        


# ----------------------
# Helper runner for testing
# ----------------------

def _run_and_print(fn, label):
    try:
        result = fn()
        print(f"{label}: {result}")
    except NotImplementedError:
        print(f"{label}: (not implemented)")


def main():
    print("Running Lab 3 - Functions exercises...\n")
    _run_and_print(ex_1_1, "1.1")
    _run_and_print(ex_1_2, "1.2")
    _run_and_print(ex_1_3, "1.3")
    _run_and_print(ex_1_4, "1.4")
    _run_and_print(ex_1_5, "1.5")
    _run_and_print(ex_1_6, "1.6")
    _run_and_print(ex_1_7, "1.7")
    _run_and_print(ex_1_8, "1.8")
    _run_and_print(ex_1_9, "1.9")
    _run_and_print(ex_2_1, "2.1")
    _run_and_print(ex_2_2, "2.2")


if __name__ == "__main__":
    main()