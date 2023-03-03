
"""""
27. Remove Element

Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of the elements may be changed.
Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums.
More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result.
It does not matter what you leave beyond the first k elements.
Return k after placing the final result in the first k slots of nums.

Used language:
Python 3.9

Testing method:
Running a line of code to test input value with the newly created function

Coding question from LeetCode:
https://leetcode.com/problems/remove-element/description/
"""""


def remove_element(numbers, value):
    numbers_array = []

    for number in numbers:

        if number != value:
            numbers_array.append(number)

    return numbers_array

    print(numbers_arra)



#Test

numbers = [4, 4, 4, 3, 2, 1, 5, 5, 5]

value = 5

result = remove_element(numbers, value)

print(result)