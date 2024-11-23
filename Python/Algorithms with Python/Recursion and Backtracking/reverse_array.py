def reverse_elements(idx, elements):
    if len(elements) // 2 == idx:
        return

    swap_idx = len(elements) - 1 - idx
    elements[idx], elements[swap_idx] = elements[swap_idx], elements[idx]
    reverse_elements(idx + 1, elements)


array = input().split()

reverse_elements(0, array)

print(" ".join(array))
