"""
CP1404/CP5632 - Practical
Program to determine score status
"""
import random

def determine_score(score):
    if score < 0 or score > 100:
        return"Invalid score"
    elif score >= 90:
        return"Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

def main():
    score = int(input("Enter score: "))
    result = determine_score(score)
    print (result)

    random_score = random.randint(0, 100)
    print(f'random score: {random_score}')
    print(determine_score(random_score))

if __name__ == '__main__':
    main()