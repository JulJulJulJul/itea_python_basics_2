def custom_map(custom_func, custom_seq):
    """
    Custom map function.
    
    :param custom_func: any function
    :param custom_seq: sequence 
    :type custom_func: function
    :type custom_seq: list
    :return: return custom_func values applied to custom_seq
    :rtype: list
    """
    result = []
    for i in custom_seq:
        custom_func(i)
        result.append(custom_func(i))

    return result


# Test example
def foo(x):
    return x ** 3 

custom_seq = [1, 2, 3]

print(custom_map(foo, custom_seq))
        
    
    
