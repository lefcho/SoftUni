def concatenate(*args, **kwargs):
    string = ''.join(args)
    if kwargs:
        for key, val in kwargs.items():
            if key in string:
                string = string.replace(key, val)

    return string

print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))