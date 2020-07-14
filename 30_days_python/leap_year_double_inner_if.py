def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
            else:
                leap = False

        else:
            leap = True
    else:
        leap = False

    # check if the years is divisible by 4, if not,  your are out anyway, so go ahead and leap = False If not,
    # then you are in unless you are a bad guy. We need to see if you are a bad guy by checking if you are divisible
    # by 100, then you are out, is there is anything that     # you could do, yes,  your only redemption is if you
    # are divisible by 400

    return leap


year = int(input())
print(is_leap(year))