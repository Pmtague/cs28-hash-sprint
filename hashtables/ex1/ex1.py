def get_indices_of_item_weights(weights, length, limit):

    # Initialize an empty dictionary
    weight_dict = {}

    # Input the weights as keys and their list indices as values

    for i in range (0, length):
        weight_dict[weights[i]] = i
        print("Weights Dictionary", weight_dict)


    # Loop through weight_dict, subtracting each key from the limit and checking to see if the difference is in weight_dict

    for x in weight_dict:
        difference = limit - x

        # If the difference is in weight_dict
        if difference in weight_dict:

            # Compare the indeces of the matched item weights
            # Place the larger index in a touple, followed by the smallest
            if difference == x:
                return ()
            if weight_dict[difference] > weight_dict[x]:
                return (weight_dict[difference], weight_dict[x])
                print ("Result", weight_dict[difference], weight_dict[x])
            else:
                return (weight_dict[x], weight_dict[difference])
                print ("Other Result", weight_dict[x], weight_dict[difference])

    # If there is no pair of items that max out the limit, return None
    return None
