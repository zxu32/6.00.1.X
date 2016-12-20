def convert_to_mandarin(us_num):
    '''
    us_num, a string representing a US number 0 to 99
    returns the string mandarin representation of us_num
    '''

    trans = {'0': 'ling', '1': 'yi', '2': 'er', '3': 'san', '4': 'si',
         '5': 'wu', '6': 'liu', '7': 'qi', '8': 'ba', '9': 'jiu', '10': 'shi'}

    if 0 <= int(us_num) <= 10:
        return trans[us_num]
    elif 11 <= int(us_num) <= 19:
        return 'shi ' + trans[str(int(us_num)-10)]
    elif 20 <= int(us_num) <= 99:
        if int(us_num) % 10 != 0:
            return trans[str(int(us_num)//10)] + ' shi ' + trans[str(int(us_num) % 10)]
        elif int(us_num) % 10 == 0:
            return trans[str(int(us_num) // 10)] + ' shi'
    else:
        return 'invalid number'
