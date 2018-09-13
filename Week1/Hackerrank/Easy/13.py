def swap_case(s):
    line = str(s)
    result = ""
    for i in line:
        if i.isalpha():
            if i.islower():
                result += i.upper()
            else:
                result += i.lower()
        else:
            result += i
    return result