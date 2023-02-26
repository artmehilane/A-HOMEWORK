

"""""
Valid Parentheses

Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

Testing method:
Running a line of code to test different input values with the newly created function

Coding question from LeetCode:
https://leetcode.com/problems/valid-parentheses/description/
"""""




def check_validity(input_string):

    while input_string:

        if "()" in input_string:
            input_string = input_string.replace("()", "")

        elif "[]" in input_string:
            input_string = input_string.replace("[]", "")

        elif "{}" in input_string:
            input_string = input_string.replace("{}", "")

        else:
            return False
    return True


tests = [
    "[()[]{}]",
    "{]",
    "()",
    "()[]{}",
    "([{}])",
    "[(])",
    "{[()]}"
]

for test in tests:

    print(check_validity(test))

