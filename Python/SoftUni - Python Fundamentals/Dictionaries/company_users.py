company_dict = {}

while True:
    command = input()
    if command == "End":
        break
    inp = command.split(" -> ")
    company = inp[0]
    id = inp[1]
    if company not in company_dict:
        company_dict[company] = []
        company_dict[company].append(id)
    elif id not in company_dict[company]:
        company_dict[company].append(id)

for company, ids in company_dict.items():
    print(company)
    for id in ids:
        print(f"-- {id}")
