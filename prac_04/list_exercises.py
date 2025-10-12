number = []

for i in range(5):
    numbers = float(input("Enter a number: "))
    number.append(numbers)

print("first number:", number[0])
print("last number:", number[-1])
print("smallest number:", min(number))
print("largest number:", max(number))
print("average number:", sum(number)/len(number))

usernames = ['jimbo', 'giltson98', 'derekf',
            'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', ''
            'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
            'bob']
username = input("Enter a username: ")
if username in usernames:
    print("access granted")
else:
    print("access denied")

