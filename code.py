def armstrong_check(number) :
        result = 0
        digits = str(number)
        for digit in digits:
            result += int(digit) ** len(digits)
        return result == number


def armstrong_series_check(start,stop) :
    series = []
    key_value = 0
    for i in range(start,stop+1) :
        temp_res = armstrong_check(i)
        if temp_res is True :
            series.append(i)
            key_value += 1
        else :
            key_value += 0
    print(series)
    print(key_value)

armstrong_series_check()

