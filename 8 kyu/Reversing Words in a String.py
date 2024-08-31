"""
You need to write a function that reverses the words in a given string. Words are always separated by a single space.

As the input may have trailing spaces, you will also need to ignore unneccesary whitespace.

Example (Input --> Output)

"Hello World" --> "World Hello"
"Hi There." --> "There. Hi"
"""

def reverse(st):
    words = st.split()
    reversed_words = words[::-1]
    result = ' '.join(reversed_words)
    return result
