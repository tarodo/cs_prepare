# Make your own implementation of the zip function in Python

def custom_zip(*iterables):
    iterators = [iter(it) for it in iterables]
    while True:
        try:
            yield tuple(next(it) for it in iterators)
        except StopIteration:
            return


# Example usage
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
list3 = [4.5, 5.5, 6.5]

for item in custom_zip(list1, list2, list3):
    print(item)
