import re

string = input()
pattern = r"[@#]+([a-z]{3,})[@#]+\W*/+([0-9]+)/+"
list_of_matches = re.findall(pattern, string)

for match in list_of_matches:
    color = match[0]
    amount = match[1]
    print(f"You found {amount} {color} eggs!")
