# #############################################################################
# FILE : palindrome.py
# WRITER : Assaf Mor , assafm04 , 036539096
# EXERCISE : intro2cs ex6
# DESCRIPTION:
# these two functions find if a given string is a palindrome and if its a
# palindrome between two given indexes, both functions work recursively
# #############################################################################
def is_palindrome_1(s):
    """
    this method checks if a given string is palindrome in a recursive way
    :param s: the string to check
    :return: true if s is a palindrome, false otherwise
    """
    # if the length is 1 or 0 return true because its a palindrome
    if len(s) == 0 or len(s) == 1:
        return True
    # if the two ends of the string match call the function recursively with
    # the two ends of the string cut as the new string parameter
    elif s[0] == s[-1:]:
        return is_palindrome_1(s[1:-1])
    # any other case indicates the string is not a palindrome
    else:
        return False


def is_palindrome_2(s, i, j):
    """
    this method checks if a substring is a palindrome between two given index recursively
    :param s: the string to check
    :param i: the starting index of the substring
    :param j: the ending point of the substring
    :return: true if the substring is a palindrome, false otherwise
    """
    # if the current string is empty its a palindrome
    if s == "":
        return True
    # if the subtraction iof the two indexes is 0 or less return true
    if j-i <= 0:
        return True
    # if the characters at the indexes match - call the function with the new
    # string, and indexes
    elif s[i] == s[j]:
        return is_palindrome_2(s, i+1, j-1)
    # any other case fails the return false
    else:
        return False

