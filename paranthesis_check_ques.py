def is_valid_parantheis(ip_string):
    key_dict = {}

    key_dict['('] = 0
    key_dict[')'] = 0

    for token in ip_string:
        if  key_dict['('] >= key_dict[')']:
            key_dict[token] = key_dict[token] + 1
        else :
            return(False)
       
    if (key_dict['('] > key_dict[')']):
        return False
    else:
        return True