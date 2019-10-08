import random


def draw_numbers(nums, n):
    nums = nums.copy()
    draw = []
    for i in range(n):
        r = random.randint(0,len(nums)-1)
        draw.append(nums.pop(r))
    return draw


def list_num(n):
    foo = []
    for i in range(n):
        foo.append(i+1)
    return foo


def comp_list( l1, l2 ):
    foo = 0
    for i in l1:
        if i in l2:
            foo += 1
    return foo


def winnings( main, extra ):
    if main is 7:
        return 2749455
    elif main is 6 and extra > 0:
        return 102110
    elif main is 6:
        return 3385
    elif main is 5:
        return 95
    elif main is 4 and extra > 0:
        return 45
    else:
        return 0

def main(n):
    tot = 0
    for i in range(n):
        draw = draw_numbers(n34, 10)
        success = [comp_list(my_guess, draw[:7]), comp_list(my_guess, draw[7:])]
        tot += (winnings(success[0], success[1]) - 5)
    print(tot)


n34 = list_num(34)
my_guess = [1,2,3,4,5,6,7]


main(1)
main(1000000)
