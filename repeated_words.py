"""
You are given n words. Some words may repeat. For each word, output its number of occurrences. The output order should correspond with the input order of appearance of the word. See the sample input/output for clarification.
Note: Each input line ends with a "\n" character.

Constraints:

The sum of the lengths of all the words do not exceed 
All the words are composed of lowercase English letters only.

Input Format

The first line contains the integer, .
The next  lines each contain a word.

Output Format

Output  lines.
On the first line, output the number of distinct words from the input.
On the second line, output the number of occurrences for each distinct word according to their appearance in the input.

Sample Input

4
bcdef
abcdefg
bcde
bcdef
Sample Output

3
2 1 1
"""

from collections import OrderedDict

quantity = input()
ordered = OrderedDict()
for i in range(int(quantity)):
    word = input()
    if ordered.get(word):
        ordered[word] = ordered[word] + 1 
    else:
        ordered[word] = 1

print(len(ordered))
for value in ordered.values():
    print(value, end=" ")

