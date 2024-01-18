# Given an integer x, return true if x is a


def isPalindrome(x):
    length = str(x)
    rev_length = length[::-1]

    if length == rev_length:
        return True
    else:
        return False


x = int(input("Enter a number: "))
print(isPalindrome(x))
