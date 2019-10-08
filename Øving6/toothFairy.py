teeth = [95,103,71,99,114,64,95,53,97,114,109,11,2,21,45,2,26,81,54,14,118,108,117,27,115,43,70,58,107]
coinage = [20, 10, 5, 1]


def tooth_coins( tooth, coins ):
    ans = []
    for c in coins:
        count = tooth // c
        ans.append( count )
        tooth -= c*count
    return ans


def tooth_coins_list( teeth, coins ):
    tmp = []
    for t in teeth:
        tmp.append(tooth_coins(t, coins))
    return tmp


print(tooth_coins_list( teeth, coinage ))
