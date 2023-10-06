from functools import cache


def integerBreak(n: int) -> int:
    if n <= 3:
        return n - 1

    @cache
    def rec(num):
        if num <= 3:
            return num

        ans = num
        for i in range(2, num):
            ans = max(ans, i * rec(num - i))

        return ans

    return rec(n)


print(integerBreak(10))