def get_indices_of_item_weights(weights, length, limit):

    # Initialize an empty dictionary
    weight_dict = {}

    # Input the weights as keys and their list indices as values

    for idx in range (0, length):
        weight_dict[weights[idx]] = idx
    print("Weights Dictionary", weight_dict)


    # Loop through weight_dict, subtracting each key from the limit and checking to see if the difference is in weight_dict

    for idx in range (0, length):
        difference = limit - weights[idx]

        # Check if the difference is in weight_dict
        if difference in weight_dict:

            # Compare the indeces of the matched item weights
            # Place the larger index in a touple, followed by the smallest
            if weight_dict[difference] > idx:
                return (weight_dict[difference], idx)
                print ("Result", weight_dict[difference], idx)
            else:
                return (idx, weight_dict[difference])
                print ("Other Result", idx, weight_dict[difference])

    # If there is no pair of items that max out the limit, return None
    return None
