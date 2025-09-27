from score import determine_score
MENU = """
(G)et a valid score 0-100
(P)int score 
(S)how stars
(Q)uit 
"""
print(MENU)

def get_valid_score():
    score_value = float(input("Enter the score: "))
    while score_value < 0 or score_value > 100:
        print("Invalid choice, please try again")
        score_value = float(input("Enter the score: "))
    return score_value

def determine_score_result(score_value):
    result = determine_score(score_value)
    return result

def print_stars(score_value):
    print("*" * int(score_value))

def main():
    score_value = get_valid_score()
    choice = input("Enter your choice: ")
    while choice != 'Q':
        if choice == 'G':
            score_value = get_valid_score()
        elif choice == 'P':
                print(determine_score_result(score_value))
        elif choice == 'S':
                print_stars(score_value)
        else:
            print("Invalid choice, please try again")
        print(MENU)
        choice = input("Enter your choice: ")
    print("see ya later")

main()
