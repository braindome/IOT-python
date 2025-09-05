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
            # if i % 5 == 0 and i % 3 == 0:
            #     entry += "Fizz Buzz"
            if not entry:
                entry = str(i)
            result.append(entry)
        return ", ".join(result)
    
    return fizz_buzz(2, 54)


print(ex_1_9())