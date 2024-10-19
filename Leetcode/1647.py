"""
A string s is called good if there are no two different characters in s that have the same frequency.

Given a string s, return the minimum number of characters you need to delete to make s good.

The frequency of a character in a string is the number of times it appears in the string. For example, in the string "aab", the frequency of 'a' is 2, while the frequency of 'b' is 1.



Example 1:

Input: s = "aab"
Output: 0
Explanation: s is already good.
Example 2:

Input: s = "aaabbbcc"
Output: 2
Explanation: You can delete two 'b's resulting in the good string "aaabcc".
Another way it to delete one 'b' and one 'c' resulting in the good string "aaabbc".
Example 3:

Input: s = "ceabaacb"
Output: 2
Explanation: You can delete both 'c's resulting in the good string "eabaab".
Note that we only care about characters that are still in the string at the end (i.e. frequency of 0 is ignored).
"""
class Solution:
    def minDeletions(self, s: str) -> int:
        char_cnt = [0] * (ord('z') - ord('a') + 1)
        for el in s:
            char_cnt[ord(el) - ord('a')] += 1
        res = set()
        res_cnt = 0
        for el in char_cnt:
            while el in res and el != 0:
                el -= 1
                res_cnt += 1
            if el != 0:
                res.add(el)


        return res_cnt

test_data = [("aab", 0), ("aaabbbcc", 2), ("ceabaacb", 2)]
sol = Solution()
fun = sol.minDeletions

for data in test_data:
    print(f"DATA = {data} RESULT = {fun(data[0])} EXPECT = {data[1]} PASSED = {fun(data[0]) == data[1]}")