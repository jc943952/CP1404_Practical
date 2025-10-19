COLOUR_CODES = {
    'absolute zero' : '#0048ba',
    'acid green' : '#b0bf1a',
    'aliceblue' : '#f0f8ff',
    'alizarin crimson' : '#e32636',
    'amaranth' : '#e52b50',
    'amber' : '#ffbf00',
    'Aquamarine2': 	'#76eec6',
    'Arylide Yellow' : 	'#e9d66b',
    'Asparagus' : '	#87a96b',
    'Ash Grey' : '#b2beb5'
}
colour_name = input("Enter a colour name: ").lower()

while colour_name != "":
    code = COLOUR_CODES.get(colour_name)
    if code:
        print(f'The code for "{colour_name}" is {code}')
    else:
        print("Invalid colour name")
    colour_name = input("Enter a colour name: ").lower()