def read_from_file():
    """
    Extract a text from text.txt file

    :return: text read from file 
    :rtype: str
    """
    try:
        with open('text.txt', 'r') as file:
            text = file.read()
    except FileNotFoundError:
        print('No such file or directory')
    try:
        return text
    except UnboundLocalError:
        print('Local variable ''text'' referenced before assignment')
        return ''


def save_results(*args):
    """
    Save results to results.txt file
    
    :return: None
    :rtype: None
    """
    
    with open('result.txt', 'w') as file:
        file.writelines(args)
