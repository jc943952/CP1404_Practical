"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
score = float(input("Enter score: "))
if score < 0:
    print("Invalid score")
elif score > 100:
    print("Invalid score")
else:
    if score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad, study more!")

# just another way to rewrite it for a broader grading system
if score < 0:
    print("Invalid score")
elif score > 100:
    print("Invalid score")
else:
    if score >= 85:
        print("HD")
    elif score >= 75:
        print("D")
    elif score >= 65:
        print("C")
    elif score >= 50:
        print("P")
    else:
        print("Bad, study more!")