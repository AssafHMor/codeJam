# #############################################################################
# FILE : balanced_brackets.py
# WRITER : Assaf Mor , assafm04 , 036539096
# EXERCISE : intro2cs ex6
# DESCRIPTION:
# this file contains 3 main methods:
# 1: is_balanced - returns true if the parentheses are balanced in a given
# string, otherwise returns false
# 2: violated_balanced - if the parentheses are un-balanced: it returns the
# length of the string if its possible to add parentheses so it may become a
# balanced string, or the index of the unbalancing if there cannot be an adding
# such that the string will be balanced.
# if the string is balanced it returns -1
# 3. match brackets - if the string is balanced parentheses-wise, it
# calculates the distance between two matching parentheses and returns a list,
# where the distance is displayed at the index of each matching parentheses
# if the string is unbalanced it returns an empty list
# #############################################################################
SINGLE_BRACKET = 1  # a single bracket appearance
INDEX_COUNTER = 1  # a single movement in the string index
OPEN_BRACKET = "("  # an open bracket
CLOSE_BRACKET = ")"  # a close bracket


def is_balanced(s):
    """
    this methods checks if a string is balanced parentheses-wise
    for every opening parentheses there is a co-responding closing
    parentheses
    :param s: the string to check on the balance
    :return: true if balanced, false otherwise
    """
    balanced = 0  # counter to check all parentheses have a counter one
    # run over the entire string
    for bracket in s:
        if bracket == OPEN_BRACKET:
            balanced += SINGLE_BRACKET  # add 1 to the counter if its - (
        if bracket == CLOSE_BRACKET:
            balanced -= SINGLE_BRACKET  # subtract 1 from the counter if its -(
            if balanced < 0:
                return False  # in case the counter is negative return false
    return balanced == 0  # in case there is balance return true


def violated_balanced(s):
    """
    if the parentheses are un-balanced: this method returns the
    length of the string if its possible to add parentheses so it may become a
    balanced string, or the index of the unbalancing if there cannot be an
    adding such that the string will be balanced.
    if the string is balanced it returns -1
    it calls the recursive function violated_parentheses which returns the
    index of violation
    :param s: the string to check
    :return: -1 if the string is balanced, or in case the string is un-balanced
    the length of the string if it is possible to balance the whole string, or
    the index where the violation occurs
    """
    if is_balanced(s):  # check if s is balanced, if so return -1
        return -1
    # if s is un-balanced call violated_parentheses with default parameters
    # stack and index as zeros, it will return the violation index or
    # length of s
    return violated_parentheses(s, stack=0, index=0)


def violated_parentheses(s, stack, index):
    """
    this is a recursive method which checks for the violation of the
    parentheses balance and returns the index of violation or the length
    of the string if its possible to balance the whole string
    :param s: the string to check
    :param stack: the stack to follow the number of brackets appearances
    :param index: the current index of the character in the string
    :return: the length of the string or the index of violation
    """
    # the stopping condition - if the string has ended
    if len(s) == index:
        return index  # return the current index if string ended

    # if current index is ( all is good so far
    elif s[index] == OPEN_BRACKET:
        stack += SINGLE_BRACKET  # add 1 to stack to keep track
        index += INDEX_COUNTER  # advance on the string index
        # continue with the inquiry on the rest of the string with the new
        # updated stack
        return violated_parentheses(s, stack, index)

    # if current index is ) check for  two options
    elif s[index] == CLOSE_BRACKET:

        # if the stack is empty return the current index because it is not
        # possible to balance the whole string anymore
        if stack == 0:
            return index

        # if the stack is not empty
        else:
            stack -= SINGLE_BRACKET  # subtract 1 from the stack to keep track
            index += INDEX_COUNTER  # advance on the string index
            # continue with the inquiry on the rest of the string with the new
            # updated stack
            return violated_parentheses(s, stack, index)

    # if the next index is not a '(' or a ')'
    else:
        index += INDEX_COUNTER  # advance on the string index
        # continue with the inquiry on the rest of the string with the current
        # stack
        return violated_parentheses(s, stack, index)


def match_brackets(s):
    """
    this methods returns a list of distance from parentheses to it matching one
    if the string is balanced parentheses-wise, it calculates the distance
    between two matching parentheses and returns a list,
    where the distance is displayed at the index of each matching parentheses
    if the string is unbalanced it returns an empty list
    :param s: the string to check
    :return: a distances list of parentheses and its matching one if s is
    balanced, if s is not balanced returns an empty list
    """
    # in case s is balanced parentheses-wise
    if is_balanced(s):
        match_list = [0]*len(s)  # initialize a list of zeros the size of s
        # call the recursive method which finds pairs of matching parentheses
        # with the string an empty list of pairs, and a list of open brackets
        pairs = recursive_brackets_match(s, 0, pairs=[], open_b=[])
        # run over the list of pairs
        for i in range(0, len(pairs)):
            pair = pairs[i]  # the current pair
            distance = pair[1]-pair[0]  # the distance between the brackets
            match_list[pair[0]] = distance  # the value at the open bracket
            match_list[pair[1]] = -distance  # the value at the closing bracket
        return match_list

    # if the string is not balanced return an empty list
    else:
        return []


def recursive_brackets_match(s, index, pairs, open_b):
    """
    this method runs over a given string assuming its balanced parentheses-wise
    and finds pairs of matching open and close parentheses, each time it finds
    a pair, the two are put into a list where the open bracket is at the first
    place and the close bracket is at the second place after running on the
    whole string this method returns a list of lists of pairs.
    this method runs recursively on the given string
    :param s: the string to check
    :param index: the current index of the string
    :param pairs: a list of lists of pairs
    :param open_b: a stack to track the open brackets
    :return: a list of lists each inner list is of size two representing the
    index of the open bracket and it co-responding bracket's index
    """
    # the stopping condition - if the current index is equal to the length of s
    # if so return the list of pairs
    if index == len(s):
        return pairs
    # if the current index is '(' add its index to the open stack
    if s[index] == OPEN_BRACKET:
        open_b.append(index)
    # if the current index is ')' add its index and the last open index to the
    # pairs list, (the open index is poped from the open stack thus removed
    # from the stack to keep track of the next matching brackets)
    if s[index] == CLOSE_BRACKET:
        pairs.append([open_b.pop(), index])  # append the pair of indexes
    # call the recursive function with the new parameters
    return recursive_brackets_match(s, index++INDEX_COUNTER, pairs, open_b )


