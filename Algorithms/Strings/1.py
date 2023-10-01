def reverseWords(s: str) -> str:
    return " ".join([str(word[::-1]) for word in s.split(" ")])


print(reverseWords("fsdfds fds fds f fds"))