dict_of_contacts = {}

while True:
    command = input()
    if "-" in command:
        current_contact = command.split("-")
        name = current_contact[0]
        phone_number = current_contact[1]
        dict_of_contacts[name] = phone_number
    else:
        number_of_searches = int(command)
        for search in range(number_of_searches):
            current_search = input()
            if current_search in dict_of_contacts:
                print(f"{current_search} -> {dict_of_contacts[current_search]}")
            else:
                print(f"Contact {current_search} does not exist.")
        break
