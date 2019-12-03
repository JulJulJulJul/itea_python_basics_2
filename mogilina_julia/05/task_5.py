from file_utils import read_from_file, save_results


STOP_WORDS = (
    'as', 'a', 'i', 'an', 'to', 'is', 'are', 'was', 'were', 'will', 'his',
    'in', 'would', 'could', 'and', 'or', 'if', 'he', 'she', 'it', 'these',
    'my', 'etc', 'me', 'you', 'the', 'your', 'of', 'by', 'for'
)
PUNCTUATION = '''!"#$%&'()*+,-./:;<=>?@\n\t[\]^_`{|}~'''


def text_format(text):
    """
    Format text function. Delete punctuation.

    :param text: any str
    :type text: str
    :return: return text in lower case and without punctuation
    :rtype: list
    """
    text = text.lower()
    
    for char in PUNCTUATION:
        if char in text:
            text = text.replace(char, ' ')
        
    text = text.split(' ')
    for i in range(text.count('')):
        text.remove('')
    
    return text


def words_quantity(text_to_count):
    """
    Words quantity function. Calculate words quantity

    :param text_to_count: list
    :type text: list
    :return: return words quantity
    :rtype: int
    """
    text = text_to_count[:]
    for words in text:
        if words in STOP_WORDS:
            text_to_count.remove(words)
    quantity = len(text_to_count)
    return quantity


def unique_words(text):
    """
    Unique words function.Extract text dictionary - unique words

    :param text: list
    :type text: list
    :return: return unique words
    :rtype: list
    """
    text_to_set = set(text)
    unique_list = (list(text_to_set))
            
    return unique_list


def top_words(text):
    """
    Top words function. Find keywords - top 3 most frequent words.

    :param text: list
    :type text: list
    :return: return top 3 most frequent words
    :rtype: dict
    """
    text = sorted(text, key=lambda i: text.count(i), reverse=True)
    text_dict = {}
     
    for words in text:
        if words in text_dict.keys():
            text_dict[words] += 1
        elif len(text_dict) < 3:
            text_dict[words] = 1
        else:
            break
                 
    return text_dict


def frequency_of_words(text):
    """
    Calculate frequency for each word

    :param text: list
    :type text: list
    :return: return frequency for each word 
    :rtype: dict
    """
    quantity = words_quantity(text)
    text = sorted(text, key=lambda i: text.count(i), reverse=True)
    text_dict = {}
     
    for words in text:
        if words in text_dict.keys():
            text_dict[words] += 1
        else:
            text_dict[words] = 1
            final_dictionary = {
                key: value * 100 // quantity
                for (key, value) in text_dict.items()
            }
        
    try:
        return final_dictionary
    
    except UnboundLocalError:
        final_dictionary = dict()
        return final_dictionary


if __name__ == '__main__':    
    text = read_from_file()
    new_text = text_format(text)

    quantity = f'Words quantity: {words_quantity(new_text)}\n' 
    unique = f'Unique words: {unique_words(new_text)}\n'
    top_w = f'Top 3 keywords: {top_words(new_text)}\n'
    f = frequency_of_words(new_text)
    f_text = f'Words frequency: {f}\n'

    result = save_results(quantity, unique, top_w, f_text)

    print(f'Words quantity: {words_quantity(new_text)}')    
    print(f'Unique words: {unique_words(new_text)}')
    print(f'Top 3 keywords: {top_words(new_text)}')
    print(f'Words frequency:')
    for (k, v) in f.items():
        print(f'\t{k}: {v}%')
