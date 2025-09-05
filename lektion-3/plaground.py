def test():

    n = 551
    steps = 1
    while n >= 0:
        n -= 8
        steps += 1
    return steps
print(test())