list_of_counties = input().split(", ")
list_of_capitals = input().split(", ")

tuple_of_counties = zip(list_of_counties, list_of_capitals)

dictionary_of_counties = {key: value for (key, value) in tuple_of_counties}

for country, capital in dictionary_of_counties.items():
    print(f"{country} -> {capital}")