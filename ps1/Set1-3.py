"""
prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh

not-working version
"""

s = 'abcdeabcdefgh'

longestSub = s[0]
for i in range(0, len(s)):
    for j in range(i, len(s)-1):
        # print(i, j, (s[j] <= s[j+1]), (len(s[i:j+1]) >= len(longestSub)))
        if s[j] <= s[j+1] and len(s[i:j+1]) >= len(longestSub):
            longestSub = s[i:j+2]
        else:  # nested loop will break if the second check is not satisfied, causing code to not work properly
            break
print('Longest substring in alphabetical order is: ', longestSub)



"""
working version
"""

s = 'abcdeabcdefgh'

longestSub = s[0]
for i in range(0, len(s)):
    for j in range(i, len(s)-1):
        # print(i, j, (s[j] <= s[j+1]), (len(s[i:j+1]) >= len(longestSub)))
        if s[j] <= s[j+1] and len(s[i:j+1]) >= len(longestSub):
            longestSub = s[i:j+2]
        elif s[j] > s[j+1]:  # nested loop breaks only upon detecting non-alphabetically ordered letters
            break
print('Longest substring in alphabetical order is: ', longestSub)
