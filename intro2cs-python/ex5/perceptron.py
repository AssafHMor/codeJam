# ############################################################
# FILE : ex5.py
# WRITER : Assaf Mor , assafm04 , 036539096
# EXERCISE : intro2cs ex5
# DESCRIPTION:
# these are basic perceptron functions which check if a given data has a
# classifier as well as methods to check for errors on given bias and classifier
# ############################################################
MAX_ITERATIONS = 10  # the max iteration multiplier allowed
SQRT_POWER = 0.5  # the power of the square root
PLUS_SIGN = 1  # represents a positive sign
MINUS_SIGN = -1  # represents a negative sign


def dot(A, B):
    """
    this method computes the dot product of two given vectors represented by
    two lists A and B, by summing up the multiplication of the objects at the
    same place in each list
    :param A: first vector represented by a list of ints or floats
    :param B: second vector represented by a list of ints or floats
    :return: the dot product of the two vectors
    """
    dot_product = 0  # initialize to product
    for i in range(0, len(A)):
        dot_product += (A[i] * B[i])  # sum the product of two elements
    return dot_product


def new_w(w, data, label):
    """
    this method calculates the new w vector by adding to the old one the
    product of the label of the vector to its co-responding place
    :param w: the old w vector
    :param data: the current data vector to multiply
    :param label: the label of this vector
    :return: the new w vector as a list
    """
    for i in range(0, len(w)):
        w[i] = w[i] + data[i]*label
    return w


def sign(w, data, b):
    """
    this method will check if the sign plus('+') or minus ('-') of the dot
    product subtracting the current given bias ('b')
    :param w: the w vector
    :param data: the current data vector
    :param b: the current bias
    :return: '1' if the product is greater than 0 or '-1' if its less than zero
    """
    product = dot(w, data)-b
    if product > 0:
        return PLUS_SIGN
    elif product < 0:
        return MINUS_SIGN


def perceptron(data, labels):
    """
    this method will run over each vector in the data and check if the sign
    of the dot product of the current w, b and data vector
    co-respond to its given label if so it will do nothing, otherwise it will
    change the w vector according to the method new_w, also it will change
    the bias to be the old one minus the current label of the current data
    vector it runs on
    :param data: a list of vectors, each vector is a list of its own
    :param labels: a list of '1' and '-1' labeling the data vectors
    :return : a tuple of w and the bias if a linear separator was found
                otherwise return a tuple containing two None values
    """
    b = 0  # initialize the bias
    w = [0] * len(data[0])  # initialize the weight vector
    errors = 0  # the number of errors found
    linear = False  # default value to check if a linear separator exist

    # as long as the errors found do not exceed 10 times the length of the
    # data list, keep running
    while len(data)*MAX_ITERATIONS > errors-1:
        for i in range(0, len(data)):  # run on the vector in data
            # in case there is no match change the bias and w
            if sign(w, data[i], b) != labels[i]:
                errors += 1
                b = b - labels[i]
                w = new_w(w, data[i], labels[i])
        # check if a linear might exist at this point if not continue to the
        # next vector
        for j in range(0, len(data)):
            if sign(w, data[j], b) == labels[j]:
                linear = True
            else:
                linear = False
                break
        # if a linear was found return a tuple with w vector and the bias
        if linear:
            return (w, b)
    # if no linear was found return a tuple of 2 None's
    return (None, None)


def generalization_error(data, labels, w, b):
    """
    this methods checks to see if by a given set of vectors and their labels
    the given linear separator('w') and given bias really do separate the
    data in the correct way. if it was successful, the return list will
    display a '0' will in the place of the correct vector otherwise will be a
    '1' in the co-responding vector
    :param data: a list of lists containing the vectors
    :param labels: the labels of each vector. will be '1' or '-1'
    :param w: the linear separator
    :param b: the bias
    :return: a list of '0' and '1', where the '0' indicate a successful linear
    separation and the '1' indicates a failed one
    """
    error_list = []  # initiate the error list
    for i in range(0, len(data)):  # run over the data list
        # if the sign matches the add a 0 to the error list
        if sign(w, data[i], b) == labels[i]:
            error_list.append(0)
        # if the sign doesn't match add a 1 to the error list
        else:
            error_list.append(1)
    return error_list


def vector_to_matrix(vec):
    """
    this method converts a vector represented in a 1D array to a square matrix
    :param vec: a list (the vector) to convert
    :return: the square matrix representation of the array
    """
    matrix_size = int(len(vec)**SQRT_POWER)  # set the size of the matrix
    matrix = []
    for i in range(0, matrix_size):
        #add the vector as a list to the list named 'matrix'
        matrix.append(vec[i*matrix_size:matrix_size*(i+1)])
    return matrix


def classifier_4_7(data, labels):
    """
    this method classify if there is a separation between a number of '4' and
    the number 7 given as vectors with labels if there is a separation it
    will return a tuple with the linear separator ('w') and the bias
    otherwise will return a tuple with two None's
    :param data: a list of list containing the vectors
    :param labels: the vectors co-responding labels of '1' and '-1'
    :return: a tuple with the linear separator ('w') and the bias
    for good separation otherwise will return a tuple with two None's
    """
    return perceptron(data, labels)


def test_4_7(train_data, train_labels, test_data, test_labels):
    """
    this method will train on some data and will check if it can apply its
    answers on a test data. after finding a certain w and b on the train
    input the method will check if it fits with the test input.
    if no linear separator was found on the train data it will return a tuple of
    three None's,  otherwise it will find the errors in the test vectors if
    there are any at that case a w,b and list of errors will be returned
    :param train_data: a list of list of train vectors
    :param train_labels: a list of train labels
    :param test_data: a list of lists of test vectors
    :param test_labels: a list of test labels
    :return: a tuple containing either three None's of the w,b, and list of
    errors
    """
    train_classifier = perceptron(train_data, train_labels)  # get the w and b
    if train_classifier[0] == None:  # if no classifier was found return None's
        return (None, None, None)
    # if a classifier on the train data was found search for errors on the
    # test data and return the w, b and the error list of the test data
    else:
        return(train_classifier[0], train_classifier[1],
               generalization_error(test_data, test_labels,train_classifier[0]
                   ,train_classifier[1]))
