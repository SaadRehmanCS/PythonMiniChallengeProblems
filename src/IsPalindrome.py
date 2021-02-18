def reverse(number):
    reverse = ""
    number = str(number)
    for i in range(len(number)-1, -1, -1):
        reverse += number[i]
    return eval(reverse)


def isPalindrome(number):
    if number == reverse(number):
        return True
    else:
        return False

print(isPalindrome(227722))