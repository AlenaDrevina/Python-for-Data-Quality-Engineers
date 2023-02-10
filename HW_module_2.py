import string
import random

# create a list of random number of dicts (from 2 to 10)

dict_List = []                                             # empty list
for x in range(random.randint(2, 10)):                     # random number of dictionaries
#    size = random.randint(1,26)                          # random dictionary size
    size = 3                                               # the size of dictionary
    keys = random.sample(string.ascii_lowercase, size)     # random lowercase letters in key parameters
    values = (random.randint(1, 50) for y in range(size))  # random numbers in value parameters
    one_Dict = dict(zip(keys, values))                      #the dictionary can be created by pairing up the letters
                                                            # with a list of random numbers using zip()
    dict_List.append(one_Dict)                              # add it to the list

print(dict_List)                                           # view the result

# get previously generated list of dicts and create one common dict

distinct_keys = []                          # create an empty list of distinct letters from all dictionaries in our list
duplicated_keys = []                        # create an empty list of distinct letters which have duplicates

for z in dict_List:                         # go through each dictionary
    for key in z:                           # go through each key in specified dictionary
        if key not in distinct_keys:        # check whether we already have the specified key in "distinct_keys" list
            distinct_keys.append(key)       # populate this list with each letter only once
        elif key not in duplicated_keys:    # if we have duplicated key we should populate
            duplicated_keys.append(key)     # "duplicated_keys" list only once using append()


distinct_keys.sort()                        # sort "distinct_keys" list in alphabetical order
duplicated_keys.sort()                      # sort "duplicated_keys" list in alphabetical order
print('Distinct_keys: ', distinct_keys)     # view distinct_keys
print('Duplicated_keys: ', duplicated_keys) # view duplicated_keys

one_common_dict = {}                        # create an empty common dictionary

for key in distinct_keys:                   # go through each letter from "distinct_keys" list
    if key in duplicated_keys:              # if this letter is in "duplicated_keys" list
        max_value = 0                       # then let's define max value for each key (the default is zero)
        dict_number = 0                     # define the number of the dictionary in the list
        for i, rand_dict in enumerate(dict_List):  # iterate over each dictionary and its index from the list using the function enumerate()
            if key in rand_dict and rand_dict[key] > max_value:  # check if the specified key is in the specified dictionary
                                                                 # AND the key's value is bigger than max value
                max_value = rand_dict[key]  # then update max value
                dict_number = i + 1         # then update the number of the dictionary (started by 1)
        key_final = key + '_' + str(dict_number)  # create the key
        one_common_dict.setdefault(key_final, max_value)  # insert key and its max value in the one_common_dict
    if key not in duplicated_keys:          # if this letter is NOT in "duplicated_keys" list, then...
        for rand_dict in dict_List:          # iterate over each dictionary
            if key in rand_dict:            # check if the specified key is in the specified dictionary
                one_common_dict.setdefault(key, rand_dict[key])  # insert key and its value in the one_common_dict

print('Common dictionary: ', one_common_dict)  # show final sorted common dictionary
