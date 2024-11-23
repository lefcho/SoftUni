def nested_loops(indx, arr):
    if indx >= len(arr):
        print(*arr, sep=' ')
        return
    for num in range(1, len(arr) + 1):
        arr[indx] = num
        nested_loops(indx + 1, arr)


n = int(input())
array = [None] * n


nested_loops(0, array)