#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):

# Initialize an empty dictionary
    ticket_hash = {}
# Initialize an empty list to store the final route
    route = []
    
# Input each ticket instance into the dictionary
    for i in range (0, length):
        ticket_hash[tickets[i].source] = tickets[i].destination
    print("Ticket Dictionairy", ticket_hash)

# Retrieve the destination with the source "None" and put it into the first place in the initialized list

    if "NONE" in ticket_hash:
        route.append(ticket_hash.get("NONE"))

    for t in range (0, length-1):
        if route[t] in ticket_hash:
            route.append(ticket_hash.get(route[t]))
    print("Route", route)

# Retreive the dict entries with the same source as the previous destination (looking like a linked list) and add them to the list in the order they are retrieved

# Return the list (route)
    return route
