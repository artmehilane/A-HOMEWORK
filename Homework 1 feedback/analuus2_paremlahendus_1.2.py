def remove_element(numbers, value):
    while value in numbers:
        numbers.remove(value)
    return numbers

# Test
numbers = [4, 4, 4, 3, 2, 1, 5, 5, 5]
value = 5

result = remove_element(numbers, value)

print(result)
