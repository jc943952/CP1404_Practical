"""
Program: emails
Author: Joshua
Date: 19/10/2025
Estimated time: 30 minutes
Actual time: 24 minutes
"""
def main():
    emails_to_name = {}
    email = input('Enter your email: ')
    while email !='':
        name = get_name_from_email(email)
        confirm = input('is this name? (y/n): ').strip().lower()
        if confirm !='' and confirm != 'y':
            name = input('Enter your name: ').title()
        emails_to_name[email] = name
        email = input('Enter your email: ')

    for email, name in emails_to_name.items():
        print(f'{name}: {email}')

def get_name_from_email(email):
    name_parts = email.split('@')[0]
    name = ''.join(name_parts).title()
    return name

if __name__ == '__main__':
    main()
