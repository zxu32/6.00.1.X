def vowelCount(s):
    count = 0
    vowel = ['a', 'e', 'i', 'o', 'u']
    for letter in s:
        if letter in vowel:
            count += 1
    print('Number of vowels: ', count)