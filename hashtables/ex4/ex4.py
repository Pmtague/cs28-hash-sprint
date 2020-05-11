def has_negatives(a):

    # Initialize an empty dictionary, result list and temp list
    positives = {}
    result = []
    temp_list = []

    # Loop through the list (a)
    for idx in range (0, len(a)):
        pos = a[idx]
        # Add all positive numbers to the dictionary
        if pos > 0:
            positives[pos] = False
        # Add the negative numbers to a temporary list
        elif pos < 0:
            temp_list.append(pos)

    # Loop through the temp list and get the absolute value of each item
    for ind in range (0, len(temp_list)):
        p = temp_list[ind]

        # Check the dictionary for the absolute value of each item from the temp list
        if abs(p) in positives:
            # If the positive compliment is in the dictionary, add that compliment to the result list
            result.append(abs(p))
    print(result)
    # Return the result
    return result


if __name__ == "__main__":
    print(has_negatives([-1,-2,1,2,3,4,-4]))
