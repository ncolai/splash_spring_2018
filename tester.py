#Reference solutions and tester function
#Please read these after class is over! 
import functions

#can you think of a way to reduce the number of lines of code even more? 
def fizzbuzz(number):
    if number % 15 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

#something to think about: what bugs, if any, might be in this code?
def factorial(i):
    if i <= 0:
        return 1
    else:
        return i * factorial(i - 1)

#something to think about: why would the greyed-out version of the recursive step
#be slower than the one listed below?
def fibonacci(i):
    if i == 1: 
        return 0
    elif i == 2:
        return 1
    else: #return fibonacci(i - 1) + fibonacci(i - 2)
        previous_fibonacci = 0
        cur_fibonacci = 1
        for next_number in range(i - 2):
            temp = previous_fibonacci + cur_fibonacci
            previous_fibonacci = cur_fibonacci
            cur_fibonacci = temp
        return cur_fibonacci

#tests whether two functions work the same on a range of outputs
def check_function(function1, function2, lower_lim, upper_lim):
    for number in range(lower_lim, upper_lim):
        if function1(number) != function2(number):
            print("Uh oh! Your function doesn't work on input {}".format(number))
            break
        else: 
            print("Yay, your function works on input {}!".format(number))

if __name__ == "__main__":
    functions = {fibonacci: functions.fibonacci, 
                fizzbuzz: functions.fizzbuzz,
                factorial: functions.factorial}
    test_function = input("Please enter a function to check: ")
    if test_function not in functions:
        print("Usage: put in either fibonacci, fizzbuzz, or factorial")
    else:
        check_function(test_function, functions[test_function], 1, 300)
