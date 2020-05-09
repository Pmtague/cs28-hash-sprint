def intersection(arrays):

    # Initialize and empty dict, an empty list and a counter variable for the number of lists
    first_list = {}
    result = []
    list_count = 1

    # Input the first list into the dictionary with value as the key and an initial count of 1 as the value

    for idx in range (0, len(arrays[0])):
        # item_count = 1
        first_list[arrays[0][idx]] = 1

    # Check each item in all other lists to see if their values are in the dictionary
    # Each time a value shows up in a list, add it to the value as a count

    for list_idx in range (1, len(arrays)):
        for ind in range (0, len(arrays[list_idx])):
            target = arrays[list_idx][ind]
            if target in first_list:
                first_list[target] += 1
        list_count += 1
    
    # Loop through the dictionary
    # Each key that has a value equal to the number of lists should be added to the result list

    for num in first_list:
        if first_list[num] == len(arrays):
            result.append(num)

    # Return the result
    return result 


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000,2000000)) + [1,2,3])
    arrays.append(list(range(2000000,3000000)) + [1,2,3])
    arrays.append(list(range(3000000,4000000)) + [1,2,3])

    print(intersection(arrays))
