
import sys


def ara(max_age, age, max, steps=0):
    """
    This is a classical solution

    :param max_age: the parrot cannot be older 
    :param age: age parrot
    :param max: parrot rejuvenation variable
    :param steps: nesting will trigger recursion
    :return: the sum of steps
    """

    if max_age >= 1:
        if sys.gettrace():
            #print(max_age,age,max,steps)
            print(f"Ara you have {max} years or mor ?")
        if age >= max:
            if sys.gettrace():
                print("Ara tell YES")
                print(f"If you by {max} years yonger ")
            age -= max
        else:
            if sys.gettrace():
                print("Ara tell NO")
        max -= int(max / 2)
        return ara(int(max_age / 2), age, max, steps + 1)
    else:
        return steps


