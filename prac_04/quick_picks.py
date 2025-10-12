import random

numbers_per_line = 6
maximum_number = 45
minimum_number = 1

def main():
    number_of_quick_picks = int(input("Enter the number of quick picks: "))
    for i in range(number_of_quick_picks):
        quick_pick = []
        for line in range (number_of_quick_picks):
