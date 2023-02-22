import string
import random

# create a list of random number of dicts (from 2 to 10)
def create_list_of_dict(a, b, c=4, e=5, f=1):
    dict_List = []
    for x in range(random.randint(a, b)):
        size = c
        keys = random.sample(string.ascii_lowercase, size)
        values = (random.randint(f, e) for y in range(size))
        one_Dict = dict(zip(keys, values))

        dict_List.append(one_Dict)
    return dict_List

dict_List = create_list_of_dict(a=2, b=10, e=50)               # call the function with parameters
print('Initial list of dictionaries: ', dict_List)

# get previously generated list of dicts and create one common dict
# create the function with 1 parameter for dict_List
def create_lists_with_keys(lst):
    distinct_keys = []
    duplicated_keys = []

    for z in dict_List:
        for key in z:
             if key not in distinct_keys:
                 distinct_keys.append(key)
             elif key not in duplicated_keys:
                 duplicated_keys.append(key)
    distinct_keys.sort()
    duplicated_keys.sort()
    return distinct_keys, duplicated_keys

distinct_keys, duplicated_keys = create_lists_with_keys(dict_List)  # call the function create_list_of_dict with parameter dict_List

# create the function with 3 parameters for distinct_keys, duplicated_keys, list_of_dict
def create_one_common_dict(dist_k, dupl_k, lst):
    one_common_dict = {}
    for key in distinct_keys:
        if key in duplicated_keys:
            max_value = 0
            dict_number = 0
            for i, rand_dict in enumerate(dict_List):
                if key in rand_dict and rand_dict[key] > max_value:

                    max_value = rand_dict[key]
                    dict_number = i + 1
            key_final = key + '_' + str(dict_number)
            one_common_dict.setdefault(key_final, max_value)
        if key not in duplicated_keys:
            for rand_dict in dict_List:
                if key in rand_dict:
                    one_common_dict.setdefault(key, rand_dict[key])
    return one_common_dict

# call the function with 3 parameters
one_common_dict_final = create_one_common_dict(distinct_keys, duplicated_keys, dict_List)
print('Common dictionary: ', one_common_dict_final)  # show final sorted common dictionary
