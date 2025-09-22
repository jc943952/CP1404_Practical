"""
using for loops to step in 10s to 100, counting down from 20, printing a number of
stars and printing star as they increase each line, prac 1 'loops'
"""
# Part A 0-100 in 10s
for i in range(0,101,10):
    print(i)

# Part B 20 - 0 Downwards
for i in range(20,0,-1):
    print(i)

# Part C Number of stars
number_of_stars_C = input("Enter a number between 0 and 50: ")
stars_C = int(number_of_stars_C)
for i in range(stars_C):
    print('*')

# Part D increasing stars per line by one
number_of_stars_D = input("Enter a number between 0 and 50: ")
stars_D = int(number_of_stars_D)
for i in range(1 ,stars_D + 1):
    print('*' * i)