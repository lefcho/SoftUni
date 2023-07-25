import re

string = input()
pattern = r"\b_([a-zA-Z0-9]+)\b"
valid_names = re.findall(pattern, string)
print(",".join(valid_names))
