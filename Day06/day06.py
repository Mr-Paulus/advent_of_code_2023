import time
import math

start = time.time()

def CalculateWins(Time, Distance):
    Mid = math.ceil(Time / 2)

    for x in range(1, Mid + 1, 1):
        if (x * (Time - x)) > Distance:
            return (Time - x - x + 1)

    return 0

# Question A
print(CalculateWins(46, 208) * CalculateWins(85, 1412) * CalculateWins(75, 1257) * CalculateWins(82, 1410))

# Question B
print(CalculateWins(46857582, 208141212571410))

end = time.time()

print(end - start)