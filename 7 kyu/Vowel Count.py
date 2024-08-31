"""
Description:
Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces.
"""
def count_vowels(input_string):
    vowels = "aeiou"
    count = 0
    for char in input_string:
        if char in vowels:
            count += 1
    return count