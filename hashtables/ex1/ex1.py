def get_indices_of_item_weights(weights, length, limit):

    weight_dict = {}

    for i in range (0, length-1):
        weight_dict[weights[i]] = i
    # print(weight_dict)

    for x in range (0, weight_dict:
        difference = limit - weight_dict[x]

        if difference in weight_dict:
            if weight_dict[difference] > weight_dict[x]:
                return (weight_dict[difference], weight_dict[x])
            else:
                return (weight_dict[x], weight_dict[difference])

    return None
