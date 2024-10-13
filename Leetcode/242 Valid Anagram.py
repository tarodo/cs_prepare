"""
Given two strings s and t, return true if t is an
anagram
 of s, and false otherwise.



Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false



Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.


Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
"""

def isAnagram(s, t):
    if len(s) != len(t):
        return False

    s_dict = {}
    for idx, c in enumerate(s):
        if c in s_dict:
            s_dict[c] += 1
        else:
            s_dict[c] = 1
        if t[idx] in s_dict:
            s_dict[t[idx]] -= 1
        else:
            s_dict[t[idx]] = -1
    return all([v == 0 for v in s_dict.values()])


def isAnagram2(s, t):
    if len(s) != len(t):
        return False
    return sorted(s) == sorted(t)


def isAnagram3(s, t):
    from collections import Counter
    if len(s) != len(t):
        return False
    return Counter(s) == Counter(t)


def isAnagram4(s, t):
    if len(s) != len(t):
        return False
    from collections import defaultdict

    s_dict = defaultdict(int)
    for idx, c in enumerate(s):
        s_dict[c] += 1
        s_dict[t[idx]] -= 1
    return all([v == 0 for v in s_dict.values()])


input_data = [
    ["anagram", "nagaram"],
    ["rat", "car"]
]

for data in input_data:
    s, t = data
    # print(f"input = {s}, {t} => isAnagram = {isAnagram(s, t)}")
    print(f"input = {s}, {t} => isAnagram4 = {isAnagram4(s, t)}")
