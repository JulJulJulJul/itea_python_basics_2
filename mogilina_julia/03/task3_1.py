a = list(input('Input array a '))
b = list(input('Input array b '))


def array_diff(a, b):
    """
    Difference function, which subtracts one list from another.
    
    :param a: first list with int elements
    :param b: second list with int elements
    :type a: list
    :type b: list
    :return: return value of element from a which isn't present in b
    :rtype: list
    """
    s = []
    for i in a:
        if i not in b:
            
            if i  not in s:
                s.append(i)
    return s


print(array_diff(a, b))

        
        
