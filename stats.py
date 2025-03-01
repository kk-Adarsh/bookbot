def get_file_content(file_path):
    with open(file_path) as f:
        content =  f.read()
        return content

def get_alpha_count_dict(long_string):
    alpha_dict = {}
    for alpha in long_string:
        if alpha.isalpha():
            alpha = alpha.lower()
            alpha_dict[alpha] = alpha_dict.get(alpha, 0) + 1
    return sort_char_dict(alpha_dict)
    
def sort_on(dict):
    return dict['count']

def sort_char_dict(dict):
    char_dict_array = []
    for x,y in dict.items():
        char_dict_array.append({'name': x, "count": y})
    char_dict_array.sort(reverse=True, key=sort_on)
    return char_dict_array


