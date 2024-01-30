#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    num = 10
    while(num > 0):
        print(num)
        num -= 1
    print('Happy New Year!')
    
    # for i in range(10, 0, -1):
    #     print(i)
    # print('Happy New Year!')
happy_new_year()


def square_integers(int_list):
    # code goes here!
    return [i**2 for i in int_list]
            # if i > 0 and i**0.5 % 1 == 0] - ignore 
    # new_list = []
    # for i in int_list:
    #     i = i**2
    #     new_list.append(i)
    # return new_list
print(square_integers([1, 2, 3, 4, 5]))

def fizzbuzz():
    # code goes here!
    for i in range(1, 101):
        if i%15 == 0:
            print('FizzBuzz')
        elif i%5 == 0:
            print('Buzz')
        elif i%3 == 0:
            print('Fizz')
        else:
            print(i)
fizzbuzz()

