'''
Parramont can live "max_age".
She can say only YES or NO.
How many questions We need to have now she age?
'''


import datetime
import random
import math
import complex_parrot_problem


def stopwatch(func):
    def watch(*args):
        x = datetime.datetime.now()
        a= func(*args)
        y = datetime.datetime.now()
        y=y-x
        print(f"The execution {func.__name__ }{args}  grass: {y} ")
        return a
    return watch


@stopwatch
def recursive_solution_age(max_age,age):
    return complex_parrot_problem.ara(max_age, age, int(max_age / 2))

@stopwatch
def recursive_solution(max_age):

    def ara(max_age,steps=0):
        if max_age>1:
            return ara(max_age//2, steps+1)
        else:
            return steps+1

    return ara(max_age)


@stopwatch
def digital_solution(max_age):
    return len("{0:b}".format(max_age))


@stopwatch
def logaritmic_solution(max_age):
    return math.ceil(math.log(max_age+1,2))


if __name__ == '__main__':
    import sys

    try:
        max_age = int( sys.argv[1] )
    except IndexError:
        print(f'''USAGE:
    {sys.executable} {sys.argv[0]} <maximum possible age of the bird.>

Example:
    {sys.executable} {sys.argv[0]} 100 
''')


    else:

        for func in [recursive_solution, digital_solution, logaritmic_solution]:

          print(f'\n>>> {func.__name__}')
          print(f"We need {func(max_age)} questions.")
          print("")

        try:

            age = int(sys.argv[2])
            if sys.gettrace():
                print(max_age,age)
            recursive_solution_age(max_age, age)

        except:
            if sys.gettrace():
                print(max_age)

            print("The age is drawn")
            print(recursive_solution_age(max_age, int((max_age+1)*random.random())))