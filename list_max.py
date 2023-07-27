# Author: Ashlyn Musgrave
# GitHub Username: ashlyn-musgrave
# Date: 7/26/2023
# Description: This program takes as its parameter a list of numbers and returns the maximum
# value in the list.
def list_max(user_defined_list):
    """This function defines the base case in the initial if statement
     The else statement calls the list_max function, asking it to compare each value starting
      at position 1 (referred to as result) to position 0. If the value at position 0 is larger
      than the result, the result will become the new value at position 0 """
    if len(user_defined_list) == 1:
        return user_defined_list[0]
    else:
        result = list_max(user_defined_list[1:])
        if user_defined_list[0] > result:
            result = user_defined_list[0]
        return result