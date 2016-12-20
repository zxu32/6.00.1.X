s = 'oboboobobobobbobobbobbobobokobwgooboobobbboobobooni'

count = 0
name = 'bob'
for i in range(0, len(s)):
    #index = s.index(letter)
    print(i, s[i])
    #print(index)
    if s[i:i+3] == name:
        #print(s[index])
        #print(s[index:index+3])
        count += 1
print('Number of times bob occurs is: ', count)

