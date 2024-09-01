"""
Task
You are given a string s. It's an equation such as "a+b=c", where a, b, c are numbers made up of the digits 0 to 9. This includes possible leading or trailing zeros. The equations will not contain any spaces.

Your task is to determine whether s is a valid Turing equation. Return true or false, respectively, in Turing's interpretation, i.e. the numbers being read backwards.

Still struggling to understand the task? Look at the following examples ;-)

Examples
For s = "73+42=16", the output should be true.
"""

def is_turing_equation(s):
    a, rest = s.split('+')
    b, c = rest.split('=')
    
    a_rev = int(a[::-1])
    b_rev = int(b[::-1])
    c_rev = int(c[::-1])
    
    return a_rev + b_rev == c_rev

import re
def is_turing_equation(s):
    a, b, c = (int(n[::-1]) for n in re.split('[+=]', s))
    return a + b == c