def expand_around_center(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left + 1:right]
def longest_palindromic_substring(s):
    longest = ""
    for i in range(len(s)):
        palindrome1 = expand_around_center(s, i, i)
        palindrome2 = expand_around_center(s, i, i + 1)
        if len(palindrome1) > len(longest):
            longest = palindrome1
        if len(palindrome2) > len(longest):
            longest = palindrome2
    return longest
input1 = "aaaabaaa"
input2 = "abba"
output1 = longest_palindromic_substring(input1)
output2 = longest_palindromic_substring(input2)
print("Output 1:", output1)
print("Output 2:", output2)
