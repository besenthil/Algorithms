# O(n^3) - time
# O(1) - space

def longestPalindromicSubstring(string):
    longest_palindrome = ""
    for idx, char in enumerate(string):
        for inner_idx in range(idx, len(string)):
            if is_palindrome(string, idx, inner_idx):
                substring = string[idx:inner_idx + 1]
                longest_palindrome = substring if len(longest_palindrome) < len(substring) else longest_palindrome
    return (longest_palindrome)


def is_palindrome(string, idx, inner_idx):
    return string[idx:inner_idx + 1] == "".join(reversed(string[idx:inner_idx + 1]))
