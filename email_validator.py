"""
You are given an integer n followed by n email addresses. Your task is to print a list containing only valid email addresses in lexicographical order.

- It must have the username@websitename.extension format type.
- The username can only contain letters, digits, dashes and underscores [a-z], [A-Z], [0-9], [-_].
- The website name can only have letters and digits [a-z], [A-Z], [0-9].
- The extension can only contain letters [a-z], [A-Z].
- The maximum length of the extension is 3.

Example

Complete the function fun in the editor below.

fun has the following paramters:

string s: the string to test
Returns

boolean: whether the string is a valid email or not
Input Format

The first line of input is the integer , the number of email addresses.
 lines follow, each containing a string.

Constraints
Each line is a non-empty string.

Sample Input
3
lara@hackerrank.com
brian-23@hackerrank.com
britts_54@hackerrank.com

Sample Output
['brian-23@hackerrank.com', 'britts_54@hackerrank.com', 'lara@hackerrank.com']
"""

import re

def fun(s):
    # return True if s is a valid email, else return False
    a_index = s.find("@")
    dot_index = len(s) -1 - s[::-1].find(".")

    username = s[:a_index]
    ext= s[dot_index +1:]
    website = s[a_index + 1:dot_index]
    
    if (
        not username or 
        not ext or 
        not website or
        not len(re.search("[a-zA-Z0-9-_]+", username).group()) == len(username) or
        not len(re.search("[a-zA-Z0-9]+", website).group()) == len(website) or
        not len(re.search("[a-zA-Z]+", ext).group()) == len(ext) or
        len(ext) > 3
    ):
        return False

    return True
