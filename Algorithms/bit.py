def find_single(arr):
    result = 0
    for num in arr:
        result ^= num
    return result


print(find_single([1, 4, 2, 1, 3, 2, 3]))
print(find_single([7, 9, 7, 9, 9]))


a = 6
b = 9
a = a ^ b
b = a ^ b
a = a ^ b

print(a, b)
