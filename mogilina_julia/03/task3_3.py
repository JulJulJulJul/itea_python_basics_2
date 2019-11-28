def custom_filt(func, seq):
    """
    Custom filter function.

    :param func: any function
    :param seq: sequence 
    :type func: function
    :type seq: list
    :return: return subset of intup data that satisfied input condition
    :rtype: list
    """
    result = []
    
    for i in seq:
         res = func(i)

         if func(i) == True:
            
             result.append(i)
             
    return result


# Test example
test = [2, 3, 4, 6, 7, 9]
func_lambda = lambda x: x % 2 == 0

print(custom_filt(func_lambda, test))


        
