def find_substring_indexes( str1, str2 ):
    str1, str2 = str1.lower(), str2.lower()
    str1_l, str2_l = list( str1 ), list( str2 )
    indexes = []
    for i in range( len(str2) - len(str1) + 1 ):
        if str2_l[ i:len(str1)+i ] == str1_l:
            indexes.append(i)
    return indexes


def replace_substring_with_str( str1, str2, str3 ):
    str1_l, str2_l, str3_l = list( str1 ), list( str2 ), list( str3 )
    ss_indexes = find_substring_indexes( str1, str2 )
    for i in range(len(ss_indexes) -1, -1, -1):
        ind = ss_indexes[i]
        diff = 0
        if i == len(ss_indexes) - 1:
            str2_l[ind:ind+len(str1)] = str3_l
            continue
        else:
            diff = ss_indexes[i+1] - ss_indexes[i]
        if diff >= len(str1):
            str2_l[ind:ind+len(str1)] = str3_l
        else:
            str2_l[ind:ind+diff] = str3_l
    s =''
    return s.join(str2_l)


test_str3 = 'cool'

test1_str1 = 'iS'
test1_str2 = 'Is this the real life? Is this just fantasy?'
print(find_substring_indexes( test1_str1, test1_str2 ))
print(replace_substring_with_str( test1_str1, test1_str2, test_str3 ))

test2_str1 = 'oo'
test2_str2 = 'Never let you go let me go. Never let me go ooo'
print(find_substring_indexes( test2_str1, test2_str2 ))
test2_str2 = 'Never let you goooo let me goo. Never let me goo oooo'
print(replace_substring_with_str( test2_str1, test2_str2, test_str3 ))
