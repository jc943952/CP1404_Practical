"""
Program: Champions Data Processor
Author: Joshua
Date: 19/10/2025
Estimated time: 60 minutes
Actual time: 50 - 60 minutes
"""

FILENAME = 'wimbeldon.csv'
def main():
    data = read_file()
    number_of_champions = process_champions_data(data)
    countries = process_countries_data(data)

    print('Champions and number of wins:')
    for champion, wins in number_of_champions.items():
        print(f'{champion}: {wins}')


    print('\nCountries of champions (alphabetical):')
    print(f' {countries}')

def read_file(filename = FILENAME):
    data = []
    with open(filename, 'r', encoding = 'utf-8-sig') as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.split(',')
            data.append(parts)
        return data

def process_champions_data(data):
    number_of_champions = {}
    for row in data:
        champion_name = row[2]
        number_of_champions[champion_name] = number_of_champions.get(champion_name, 0) + 1
    return number_of_champions


def process_countries_data(data):
    countries = {row[3] for row in data}
    return sorted(countries)

if __name__ == '__main__':
    main()




